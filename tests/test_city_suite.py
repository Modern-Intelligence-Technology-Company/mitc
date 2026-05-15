"""Tests for the single-image city ALPR suite (no Docker required)."""

from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import create_app
from app.mediamtx_render import render_mediamtx_config


def test_mediamtx_render_includes_expected_paths() -> None:
    yml = render_mediamtx_config(twin_count=3, rtsp_port=8554)
    assert "twin_cam_01" in yml and "twin_cam_03" in yml
    assert "twin_cam_04" not in yml
    assert "8554" in yml


@pytest.fixture()
def api_client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("MITC_DATA_DIR", str(tmp_path))
    cfg = Path(__file__).resolve().parent / "fixtures" / "cameras_min.yaml"
    monkeypatch.setenv("MITC_CAMERAS_FILE", str(cfg))
    monkeypatch.setenv("MITC_ENABLE_WORKER", "0")
    with TestClient(create_app()) as client:
        yield client


def test_healthz(api_client: TestClient) -> None:
    r = api_client.get("/healthz")
    assert r.status_code == 200
    assert r.json().get("status") == "ok"


def test_cameras_lists_configured_channels(api_client: TestClient) -> None:
    r = api_client.get("/api/v1/cameras")
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 2
    assert {c["id"] for c in body["cameras"]} == {"twin-001", "twin-002"}


def test_reads_empty_initially(api_client: TestClient) -> None:
    r = api_client.get("/api/v1/reads")
    assert r.status_code == 200
    assert r.json()["count"] == 0
