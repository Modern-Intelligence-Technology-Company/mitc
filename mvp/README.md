# MITC lab MVP — simulated RTSP without field hardware

This stack **mimics** how production ingests **H.264 over RTSP/TCP** from a commodity camera. The **reference SKU** for integration ergonomics is **[AXIS Q1805-LE](https://www.axis.com/products/axis-q1805-le)** (ONVIF + RTSP + unusually complete public documentation; swap the synthetic URL for the camera’s `rtsp://…` string when hardware is on-air).

## Open protocol anchors (build before you wire poles)

| Layer | Specification / project | Role |
|-------|--------------------------|------|
| Transport | **RTSP** ([RFC 2326](https://www.rfc-editor.org/rfc/rfc2326)), **RTP** ([RFC 3550](https://www.rfc-editor.org/rfc/rfc3550)) | Negotiation and framing of video streams — implemented by FFmpeg, GStreamer, and every serious VMS. |
| Codec | **H.264 / H.265** (ITU-T / ISO IEC) | What encoders emit; decoders are commodity. |
| Device API | **[ONVIF](https://www.onvif.org/specs/)** (downloadable specs) | Profiles **S** and **T** for streaming/control — **not** FOSS firmware, but a **free, vendor-neutral contract** for automation and discovery. |
| Lab broker | **[MediaMTX](https://github.com/bluenviron/mediamtx)** (Apache-2.0) | Acts as RTSP **server** so developers can publish synthetic video exactly like a camera would be **pulled** in production. |

You **do not** need vendor binaries on the laptop to simulate ingest: only **Docker**, **FFmpeg**, and this repo.

## Quick start

```bash
cd mvp
docker compose build
docker compose up
```

- **Published stream (read path):** `rtsp://127.0.0.1:8554/simulated_axis` (TCP; match `-rtsp_transport tcp` in `ffprobe`/FFmpeg clients the way you would for Axis on congested links).
- **Smoke check:** `docker compose up --abort-on-container-exit ingest-smoke` — runs `ffprobe` once and exits **0** if the stream decodes (**requires** `docker compose build` first for `mitc/ffmpeg-runner:local`).

## Mapping to AXIS Q1805-LE in production

Replace the synthetic URL with the camera’s RTSP URL from Axis docs or ONVIF media profile (exact string varies by firmware and profile). Development against **MediaMTX + FFmpeg** stays valid: only the **URL and credentials** change.

## Citywide budget scenarios

Illustrative **CAPEX** tables (19 / 30 / 40 / 50 channels, low–mid–high) live in **`docs/budget-citywide-install.md`**, generated from the audited model in **`mvp/budget/calculator.py`**.

```bash
pip install -r requirements-dev.txt
pytest
python scripts/render_budget_tables.py   # refresh Markdown tables if assumptions change
```
