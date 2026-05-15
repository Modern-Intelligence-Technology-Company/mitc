"""Load cameras.yaml — modular attachment of RTSP endpoints (twin or live Axis)."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class CameraSpec:
    """One ingest channel (digital twin URL or production pole)."""

    id: str
    name: str
    rtsp_url: str
    role: str


def default_cameras_path() -> Path:
    return Path(os.environ.get("MITC_CAMERAS_FILE", "/app/config/cameras.twin.yaml"))


def load_cameras(path: Path | None = None) -> tuple[str | None, list[CameraSpec]]:
    """
    Returns (reference_camera_model, cameras).

    reference_camera_model documents the BOM reference (e.g. AXIS Q1805-LE).
    """
    p = path or default_cameras_path()
    raw = yaml.safe_load(p.read_text())
    if not isinstance(raw, dict):
        raise ValueError("cameras file must be a mapping at top level")
    ref = raw.get("reference_camera_model")
    ref_s = str(ref) if ref else None
    cams_raw: list[dict[str, Any]] = raw.get("cameras", [])
    out: list[CameraSpec] = []
    for row in cams_raw:
        out.append(
            CameraSpec(
                id=str(row["id"]),
                name=str(row.get("name", row["id"])),
                rtsp_url=str(row["rtsp_url"]),
                role=str(row.get("role", "live")),
            )
        )
    return ref_s, out
