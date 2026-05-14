# ADR 0002 — MVP simulated RTSP ingest, reference COTS camera, and reproducible citywide budget model

**Status:** Accepted  
**Date:** 2026-05-15  
**Context:** Municipal programs must develop ingest, decode, and orchestration **before** every pole is rewired. Open **wire protocols** (RTSP/RTP; ONVIF control) allow lab simulation of production paths. Separately, Bloomington’s camera count is uncertain between headline tallies and third-party maps; budgets need **parameterized** totals.

## Decision

1. **Reference integration SKU (MVP):** Standardize lab and integration docs on **[AXIS Q1805-LE](https://www.axis.com/products/axis-q1805-le)** — **ONVIF Profile S/T**, **RTSP**, well-documented operator URLs, broad ecosystem support (FFmpeg, Frigate, VMS tooling), and **NDAA-favorable** positioning typical of Axis for U.S. municipal work. Other COTS SKUs remain supported; this is the **lowest-friction default** for engineering velocity.

2. **Simulation MVP:** Ship a **Docker Compose** stack under `mvp/` using **MediaMTX** + **FFmpeg** (`lavfi` test pattern) to publish a **TCP RTSP** stream at path `simulated_axis`, matching how production ingests from Axis RTSP endpoints—**final swap** is pointing ingest URLs at real cameras.

3. **Budget model:** Encode **illustrative** CAPEX assumptions in `mvp/budget/calculator.py` with **pytest** coverage; narrative and rounded tables in `docs/budget-citywide-install.md`. Figures are **planning estimates**, not bids.

## Consequences

- Developers can run `docker compose` locally without cameras; CI validates compose structure and budget math without live RTSP.
- Product and procurement teams can regenerate scenarios (19 / 30 / 40 / 50 channels) from code.

## Success criteria

- `pytest` passes; `docker compose -f mvp/docker-compose.yml config` validates.
- Technical specification references simulation and protocol anchors.
- Budget document lists assumptions transparently.
