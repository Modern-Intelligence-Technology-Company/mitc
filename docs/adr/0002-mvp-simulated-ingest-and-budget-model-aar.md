# ADR 0002 — After Action Report

**ADR:** [0002-mvp-simulated-ingest-and-budget-model.md](./0002-mvp-simulated-ingest-and-budget-model.md)  
**Date:** 2026-05-15

| Criterion | Result |
|-----------|--------|
| MVP ingest path without hardware | **Met** — MediaMTX + FFmpeg synthetic RTSP under `mvp/` |
| Reference camera clarity | **Met** — AXIS Q1805-LE called out in ADR, MVP README, technical spec |
| Reproducible budget | **Met** — `mvp/budget/calculator.py` + `docs/budget-citywide-install.md` |

**Follow-ups:** Optional CI job running `docker compose -f mvp/docker-compose.yml up --abort-on-container-exit ingest-smoke` on runners that allow Docker-in-Docker; integrate **Frigate** or **GStreamer** ingest in a later ADR if the pilot selects those stacks; wire `render_budget_tables.py` to patch `docs/budget-citywide-install.md` automatically if table drift becomes noisy.
