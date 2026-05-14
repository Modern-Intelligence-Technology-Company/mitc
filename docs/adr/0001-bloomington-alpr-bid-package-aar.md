# ADR 0001 — After Action Report: Bloomington ALPR bid documentation package

**ADR:** `0001-bloomington-alpr-bid-package`  
**Date:** 2026-05-14  
**Author:** MITC Engineering (documentation)

## Summary

The bid package was authored as Markdown under `docs/`, with repository navigation in `README.md` and process trace in `LOG.md`. A shell-based acceptance script guards minimum substance and key compliance themes (local custody; open / standards-based technical anchors).

## Outcomes vs success criteria

| Criterion | Result |
|-----------|--------|
| Five thesis artifacts | **Met** — `business-plan.md`, `alpr-technical-specification.md`, `proposal-paper.md`, `pitch-deck.md`, `bid-cover-letter.md` |
| Lean completeness | **Met** — Narratives are scoped to Bloomington’s public framing and MITC’s thesis |
| Local custody | **Met** — Architecture centers on an in-city platform; air-gap and hybrid options documented |
| Open stack | **Met** — ONVIF, TLS, PostgreSQL, object storage, containerized services, named OSS ALPR exemplars |
| Traceability | **Met** — ADR, AAR, branch discipline per `AGENTS.md` |

## Technical / procurement risks recorded for follow-up

1. **RFP variance**: Official scopes, insurance certificates, bonding, and MWBE requirements were not available at draft time; the proposal paper flags placeholders.  
2. **Accuracy acceptance**: Plate recognition accuracy is **site- and lighting-dependent**; MITC positions a pilot and acceptance testing rather than a blanket accuracy guarantee.  
3. **Omnichannel community process**: Council and public engagement may impose extra reporting cadence beyond minimum compliance; operations section budgets recurring transparency work.

## Lessons

- Keeping **verification as executable criteria** prevented “empty file” drift.  
- Anchoring on the **City’s own April 2026 statement** (equipment counts, governance themes) improved defensibility versus generic ALPR marketing.

## Revisit triggers

Update this AAR when:

- A formal RFP / IFB number and due date are published.  
- Bloomington adopts new state or local ALPR retention or sharing rules.  
- MITC selects a primary ALPR inference engine post-pilot and locks support SLAs.
