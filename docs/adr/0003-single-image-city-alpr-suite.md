# ADR 0003 — Single-container city-local ALPR suite (Axis reference, twin mode)

**Status:** Accepted  
**Date:** 2026-05-15  
**Depends on:** ADR 0002 (simulation philosophy), technical spec Q1805-LE reference

## Context

Bloomington requires **local custody**: one deployable unit on a **city rack** should become useful as soon as **RTSP camera URLs** are attached—without mandating separate broker/installer VMs for a pilot. Engineering needs a **digital twin** mode that mirrors N concurrent feeds to validate capacity before poles land.

## Decision

1. Ship **`suite/`** as a **single OCI image** (`mitc/city-alpr-suite` pattern) running **supervisord** with:
   - **MediaMTX** (RTSP broker / compatibility with Axis `rtsp://…` pull patterns),
   - optional **in-container synthetic twin publishers** (FFmpeg `lavfi` → RTSP) for `MITC_TWIN_COUNT` channels,
   - **FastAPI** application: SQLite metadata, **stub ALPR** (timestamped reads + thumbnails) demonstrating full modular **ingestion → storage → API → UI** loop,
   - static **dashboard** for council demos.

2. **Modular attachment model:** cameras are declared in **`cameras.yaml`** (`rtsp_url` per channel). **Twin mode** defaults URLs to `rtsp://127.0.0.1:8554/twin_cam_XX`. **Production** replaces each URL with **[AXIS Q1805-LE](https://www.axis.com/products/axis-q1805-le)**-style endpoints (or any ONVIF RTSP peer); **no image rebuild** required—only volume mount or ConfigMap swap.

3. **Stub vs production inference:** this ADR intentionally ships a **deterministic stub** (evident in UI/API) so municipalities can audit plumbing without licensing third-party weights; ONNX/YOLO integration is a future ADR.

## Success criteria

- One `docker run …` exposes **8080** (HTTP API/UI) and **8554** (RTSP, twin + relay),
- `pytest` covers config render + HTTP contract without Docker,
- README documents twin count, Axis URL substitution, and resource cautions for N≈40,

## Consequences

- Image size is **large** (FFmpeg + MediaMTX + Python); acceptable for server class hardware.
- **PostgreSQL / MinIO** are not bundled here—SQLite + local FS match “single image pilot”; HA variants later split stateful tiers per future ADR.
