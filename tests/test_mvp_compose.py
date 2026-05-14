"""
Verify the lab MVP ingest stack is defined and structurally valid.

These checks ensure contributors cannot accidentally remove the simulation path
from the repository without test failure.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
COMPOSE = ROOT / "mvp" / "docker-compose.yml"
MEDIAMTX = ROOT / "mvp" / "mediamtx.yml"


def test_mvp_compose_exists() -> None:
    assert COMPOSE.is_file(), f"Expected {COMPOSE}"


STREAMGEN_SH = ROOT / "mvp" / "docker" / "ffmpeg-runner" / "streamgen.sh"


def test_mvp_compose_declares_mediamtx_and_streamgen() -> None:
    data = yaml.safe_load(COMPOSE.read_text())
    services = data.get("services", {})
    assert "mediamtx" in services, "MediaMTX is the RTSP broker for lab simulation"
    assert "streamgen" in services, "FFmpeg publishes synthetic video into MediaMTX"


def test_streamgen_build_context_and_script_reference_axis_path() -> None:
    """Published path name aligns with MVP README (simulated_axis == stand-in for Axis URL)."""
    data = yaml.safe_load(COMPOSE.read_text())
    sg = data["services"]["streamgen"]
    assert "build" in sg
    assert "simulated_axis" in STREAMGEN_SH.read_text()


def test_mediamtx_config_has_publisher_path() -> None:
    assert MEDIAMTX.is_file()
    cfg = yaml.safe_load(MEDIAMTX.read_text())
    paths = cfg.get("paths", {})
    assert "simulated_axis" in paths
    assert paths["simulated_axis"].get("source") == "publisher"
