# MITC City ALPR Suite — single-container pilot

**ADR:** [docs/adr/0003-single-image-city-alpr-suite.md](../docs/adr/0003-single-image-city-alpr-suite.md)  
**Reference camera (modular RTSP):** [AXIS Q1805-LE](https://www.axis.com/products/axis-q1805-le)

This image runs **entirely on the city server**: **MediaMTX** (RTSP), **synthetic twin publishers** (FFmpeg), **FastAPI** (REST + dashboard), and **SQLite** + JPEG thumbnails under `MITC_DATA_DIR`. **No cloud dependency** is required for ingest metadata in pilot mode.

## What “connection modularity” means

1. **Digital twin (default):** `MITC_TWIN_COUNT` FFmpeg processes publish **`twin_cam_01` … `twin_cam_NN`** into MediaMTX (`rtsp://127.0.0.1:8554/...` inside the container). The bundled **`config/cameras.twin.yaml`** lists matching `rtsp_url` entries for the **stub ingest worker**.
2. **Production:** Replace each `rtsp_url` in `cameras.yaml` with the pole camera (e.g. `rtsp://user:pass@10.x.y.z/axis-media/media.amp?streamprofile=PrimaryVideo`). **Rebuild not required** — mount the file or supply via ConfigMap.
3. **Disable twins:** Set `MITC_TWIN_COUNT=0` and mount a `cameras.yaml` that only lists **live** RTSP targets (supervisor still starts `twin_feeds.sh`, which becomes a no-op loop—future improvement: conditional program).

## Build

From repo root:

```bash
docker build -f suite/Dockerfile -t mitc/city-alpr-suite:local .
```

## Run

```bash
docker run --rm \
  -p 8080:8080 -p 8554:8554 \
  -e MITC_TWIN_COUNT=8 \
  -v mitc-data:/data \
  -v "$PWD/suite/config/cameras.twin.yaml:/app/config/cameras.twin.yaml:ro" \
  mitc/city-alpr-suite:local
```

- **Dashboard:** http://localhost:8080/  
- **Health:** http://localhost:8080/healthz  
- **API:** `GET /api/v1/cameras`, `GET /api/v1/reads`  
- **Expose RTSP externally** (optional): `-p 8554:8554` lets VMS clients probe `rtsp://<server>:8554/twin_cam_01` exactly like a field path.

## Environment

| Variable | Default | Purpose |
|----------|---------|---------|
| `MITC_DATA_DIR` | `/data` | SQLite + thumbnails |
| `MITC_CAMERAS_FILE` | `/app/config/cameras.twin.yaml` | Channel list |
| `MITC_TWIN_COUNT` | `8` | Synthetic RTSP publishers (**each is one FFmpeg**; ~40 needs large CPU) |
| `MITC_ENABLE_WORKER` | `1` | `0` disables background stub ingest (HTTP only) |
| `MITC_INGEST_INTERVAL_SEC` | `12` | Seconds between ingest passes |

## Compose wrapper (optional)

```bash
docker compose -f suite/docker-compose.yml up --build
```

## Operational notes

- **Stub reads** are labeled `SIM-{CAMERA}-…` in API and UI—evidentiary ALPR requires a future ONNX/YOLO+OCR ADR.
- **Evidence retention** is local SQLite + files; migrate to PostgreSQL + object storage for HA programs.
- **Security:** tighten firewall to camera VLANs; RTSP credentials live in `cameras.yaml`—protect the mount with host permissions or secrets manager injection.
