# ADR 0003 — After Action Report

**ADR:** [0003-single-image-city-alpr-suite.md](./0003-single-image-city-alpr-suite.md)  
**Date:** 2026-05-15

| Criterion | Result |
|-----------|--------|
| Single image runnable | **Met** — `suite/Dockerfile`, supervisord + MediaMTX + FastAPI |
| Twin modularity | **Met** — `cameras.yaml` + `MITC_TWIN_COUNT` synthetic RTSP siblings |
| Axis reference documented | **Met** — default config references AXIS Q1805-LE URL patterns in README |
| Automated tests | **Met** — `tests/test_city_suite.py` (no Docker required) |

**Follow-ups:** Optional GPU/ONNX worker sidecar or second-stage image; export reads to S3/MinIO when City storage tier is provisioned; mutual TLS on RTSP rarely supported—prefer VPN/IPsec to camera VLANs. For **DeFlock-class** density (≈40 twins), scale **vCPU/RAM** before raising `MITC_TWIN_COUNT`; each twin runs a dedicated **FFmpeg** encoder process inside the container.

**Related:** ADR 0002 (`mvp/`) covers the smaller composable lab stack; ADR 0003 collapses broker + API + twin publishers into **one** city rack image for pilot deployment velocity.
