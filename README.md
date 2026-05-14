# MITC — Bloomington ALPR bid workspace

Modern Intelligence Technology Company (MITC) uses this repository for the **documentation package** supporting a City of Bloomington, Indiana procurement for locally hosted automated license plate reader (ALPR) capabilities.

## Quick links

| Document | Purpose |
|----------|---------|
| [thesis.md](thesis.md) | Original bootstrapping brief |
| [docs/business-plan.md](docs/business-plan.md) | Lean business plan |
| [docs/alpr-technical-specification.md](docs/alpr-technical-specification.md) | Hardware + software specification |
| [docs/proposal-paper.md](docs/proposal-paper.md) | Comprehensive proposal |
| [docs/pitch-deck.md](docs/pitch-deck.md) | Slide-by-slide deck (Markdown) |
| [docs/bid-cover-letter.md](docs/bid-cover-letter.md) | Bid cover / introduction |
| [docs/budget-citywide-install.md](docs/budget-citywide-install.md) | Illustrative citywide CAPEX scenarios (19–50 channels; low/mid/high) |
| [mvp/README.md](mvp/README.md) | Lab MVP: synthetic RTSP (MediaMTX) + smoke test |
| [docs/adr/0001-bloomington-alpr-bid-package.md](docs/adr/0001-bloomington-alpr-bid-package.md) | Architecture Decision Record |
| [docs/adr/0001-bloomington-alpr-bid-package-aar.md](docs/adr/0001-bloomington-alpr-bid-package-aar.md) | After Action Report |
| [docs/adr/0002-mvp-simulated-ingest-and-budget-model.md](docs/adr/0002-mvp-simulated-ingest-and-budget-model.md) | ADR: MVP ingest simulation + budget model |
| [docs/adr/0002-mvp-simulated-ingest-and-budget-model-aar.md](docs/adr/0002-mvp-simulated-ingest-and-budget-model-aar.md) | AAR for ADR 0002 |
| [LOG.md](LOG.md) | Chronological development log |
| [MEMORY.md](MEMORY.md) | High-priority facts for future context |
| [LESSONS.md](LESSONS.md) | Durable lessons learned |

## Verification

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
./scripts/verify-deliverables.sh
```

`verify-deliverables` runs **`pytest`** (MVP Compose + budget calculator) when `.venv` exists, and validates **`docker compose`** for `mvp/docker-compose.yml` when Docker is installed.

### Lab MVP (optional)

```bash
cd mvp && docker compose build && docker compose up --abort-on-container-exit ingest-smoke
```

## Methodology

See [AGENTS.md](AGENTS.md) for project practices (testing discipline for code, ADRs, logging, branching).
