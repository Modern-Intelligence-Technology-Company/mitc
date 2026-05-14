# LOG.md — chronological spine

## 2026-05-14

- Initialized git repository content: `AGENTS.md`, `thesis.md` (MITC / Bloomington ALPR bid bootstrap).
- **ADR 0001** accepted: author bid package as Markdown + executable completeness checks; see `docs/adr/0001-bloomington-alpr-bid-package.md`.
- Researched public City framing: Flock contract end (2026-03-05); transition announcement (2026-04-15); fleet description (11 fixed LPR, 4 fixed video, 4 mobile trailers with LPR/video/gunshot); emphasis on privacy, transparency, accountability, and ending outside network visibility during transition ([source](https://bloomington.in.gov/news/2026/04/15/6521)).
- Implemented `scripts/verify-deliverables.sh` (**red** phase: fails until deliverables exist), then authored full `docs/*` set (**green**).
- Branch: `adr/0001-bloomington-alpr-bid-package` → merge to `master` locally. **Note:** no `git remote` configured in this environment; push deferred until user adds origin.
- **Coverage note:** Total automated test coverage applies to future application code; this repo’s default “fast” check is `./scripts/verify-deliverables.sh`. Extended / slow suites are N/A until CV runtime exists.
- Added `MEMORY.md` (AGENTS.md documentation layers) after merge; **push** still pending remote configuration.
- Added `LESSONS.md` for durable bid-package lessons learned.
- Aligned all repository nomenclature to **Modern Intelligence Technology Company (MITC)** per `thesis.md`; committed and pushed to `origin`.
- Documented **Flock Safety** as competitive reference; **thin-pole / stream-only** camera posture vs. **on-camera ALPR** (theft resilience); added **manufacturer COTS links** (Axis Q1805-LE, Hanwha PNO-A9081R, Bosch NBE-5503-AL, Uniview IPC2B25SS-ADZK-I1) in `docs/alpr-technical-specification.md`; extended `verify-deliverables.sh` to require those URL patterns; updated proposal, business plan, pitch deck, cover letter; refreshed `MEMORY.md`.
- Incorporated **DeFlock** **[Bloomington map](https://maps.deflock.org/?lat=39.1670&lng=-86.5343&zoom=11.00)** (~**40** markers) alongside official **11+4+4** summary for **budget / capacity** guardrails; expanded **§5 pricing** in proposal, **§3.4** sizing table in technical spec, pitch deck commercial slide, business-plan phases and cost drivers; updated bid letter and `MEMORY.md`.
- **ADR 0002** + MVP: **MediaMTX** + **Alpine/ffmpeg** synthetic RTSP in `mvp/`, **`pytest`** + **`mvp/budget/calculator.py`**, **`docs/budget-citywide-install.md`** (19–50 channels, low/mid/high); technical spec **§4.7** simulation; reference Axis **Q1805-LE** as fastest software path; `verify-deliverables` runs tests when `.venv` present.
