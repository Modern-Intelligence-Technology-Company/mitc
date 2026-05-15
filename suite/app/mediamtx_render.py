"""Generate MediaMTX YAML for in-container twin RTSP publishers."""

from __future__ import annotations


def render_mediamtx_config(twin_count: int, rtsp_port: int = 8554) -> str:
    """
    Emit a minimal mediamtx.yml declaring twin_cam_XX paths as publisher sinks.

    FFMpeg processes publish to rtsp://127.0.0.1:{port}/twin_cam_XX matching
    AXIS-class client URLs used in cameras.yaml (digital twin mode).
    """
    if twin_count < 0 or twin_count > 96:
        raise ValueError("twin_count must be 0..96")
    lines = log_and_api_lines(rtsp_port)
    lines.append("paths:")
    if twin_count == 0:
        lines.append("  placeholder:")
        lines.append("    source: publisher")
    for i in range(1, twin_count + 1):
        name = f"twin_cam_{i:02d}"
        lines.append(f"  {name}:")
        lines.append("    source: publisher")
    return "\n".join(lines) + "\n"


def log_and_api_lines(rtsp_port: int) -> list[str]:
    """Minimal globals compatible with mediamtx v1.9.x open-source builds."""
    return [
        "logLevel: info",
        f"rtspAddress: :{rtsp_port}",
        "",
    ]
