"""MITC single-image city ALPR suite — HTTP API + dashboard."""

from __future__ import annotations

import logging
import os
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles

from app import db
from app.config_loader import load_cameras
from app.worker import start_ingest_worker, stop_ingest_worker

logging.basicConfig(level=os.environ.get("MITC_LOG_LEVEL", "INFO"))
log = logging.getLogger(__name__)

_STATIC = Path(__file__).resolve().parent / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    if os.environ.get("MITC_ENABLE_WORKER", "1") not in ("0", "false", "False"):
        start_ingest_worker()
    else:
        log.info("ingest worker disabled (MITC_ENABLE_WORKER=0)")
    yield
    stop_ingest_worker()


def create_app() -> FastAPI:
    """Application factory — tests call this with fresh env without importlib hacks."""

    application = FastAPI(
        title="MITC City ALPR Suite",
        version="0.1.0",
        lifespan=lifespan,
        description="Local custody ALPR pilot — twin RTSP or live AXIS Q1805-LE class endpoints",
    )

    @application.get("/healthz")
    def healthz() -> dict[str, str]:
        return {
            "status": "ok",
            "suite": "mitc-city-alpr-suite",
            "worker": os.environ.get("MITC_ENABLE_WORKER", "1"),
        }

    @application.get("/api/v1/cameras")
    def api_cameras() -> JSONResponse:
        ref, cams = load_cameras()
        payload = {
            "reference_camera_model": ref,
            "count": len(cams),
            "cameras": [{"id": c.id, "name": c.name, "rtsp_url": c.rtsp_url, "role": c.role} for c in cams],
        }
        return JSONResponse(payload)

    @application.get("/api/v1/reads")
    def api_reads(limit: int = 50) -> JSONResponse:
        rows = db.list_reads(limit=limit)
        return JSONResponse({"count": len(rows), "reads": rows})

    @application.get("/", response_class=HTMLResponse, response_model=None)
    def dashboard() -> Response:
        index = _STATIC / "index.html"
        if index.is_file():
            return FileResponse(index)
        return HTMLResponse("<p>MITC suite: missing static/index.html</p>", status_code=500)

    if _STATIC.is_dir():
        application.mount("/static", StaticFiles(directory=str(_STATIC)), name="static")

    return application


app = create_app()


def reset_runtime_state() -> None:
    """Reserved for operational hooks; tests use create_app() factory instead."""
    stop_ingest_worker()
