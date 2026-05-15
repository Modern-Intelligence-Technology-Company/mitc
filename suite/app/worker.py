"""Background RTSP ingest + deterministic ALPR stub (proves end-to-end plumbing)."""

from __future__ import annotations

import logging
import os
import subprocess
import threading
import time
import uuid
from pathlib import Path

from app import db
from app.config_loader import CameraSpec, load_cameras

log = logging.getLogger(__name__)

_stop = threading.Event()
_thread: threading.Thread | None = None


def start_ingest_worker() -> None:
    global _thread
    if _thread is not None and _thread.is_alive():
        return
    _stop.clear()
    _thread = threading.Thread(target=_ingest_loop, name="mitc-ingest", daemon=True)
    _thread.start()
    log.info("ingest worker started")


def stop_ingest_worker() -> None:
    _stop.set()
    global _thread
    if _thread is not None:
        _thread.join(timeout=8)
        _thread = None
    log.info("ingest worker stopped")


def _ingest_loop() -> None:
    interval = float(os.environ.get("MITC_INGEST_INTERVAL_SEC", "10"))
    while not _stop.is_set():
        try:
            _, cameras = load_cameras()
            for cam in cameras:
                if _stop.is_set():
                    break
                _process_camera(cam)
        except Exception:
            log.exception("ingest tick failed")
        if _stop.wait(interval):
            break


def _process_camera(cam: CameraSpec) -> None:
    ts = time.time()
    thumb = db.data_dir() / "thumbs" / f"{cam.id}_{int(ts)}.jpg"
    ok = _ffmpeg_snapshot(cam.rtsp_url, thumb)
    if not ok:
        log.warning("snapshot failed for %s (%s)", cam.id, cam.rtsp_url)
        return
    plate = f"SIM-{cam.id.upper()}-{uuid.uuid4().hex[:6].upper()}"
    note = "stub-alpr-v0 (deterministic demo; replace with ONNX/YOLO+OCR per pilot ADR)"
    rel = None
    if thumb.is_file():
        try:
            rel = str(thumb.relative_to(db.data_dir()))
        except ValueError:
            rel = str(thumb)
    db.insert_read(
        camera_id=cam.id,
        ts=ts,
        plate_text=plate,
        confidence=0.0,
        thumb_path=rel,
        source_note=note,
    )
    log.info("recorded stub read %s for camera %s", plate, cam.id)


def _ffmpeg_snapshot(rtsp_url: str, out_jpg: Path) -> bool:
    out_jpg.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-rtsp_transport",
        "tcp",
        "-i",
        rtsp_url,
        "-frames:v",
        "1",
        "-q:v",
        "5",
        "-y",
        str(out_jpg),
    ]
    try:
        r = subprocess.run(cmd, timeout=20, capture_output=True, check=False)
    except subprocess.TimeoutExpired:
        return False
    return r.returncode == 0 and out_jpg.is_file() and out_jpg.stat().st_size > 100
