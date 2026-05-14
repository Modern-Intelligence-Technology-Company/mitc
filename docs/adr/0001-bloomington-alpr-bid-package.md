# ADR 0001: Bloomington ALPR bid documentation package

## Status

Accepted — implemented 2026-05-14.

## Context

Modern Intelligence Technology Company (MITC) is preparing a response to the City of Bloomington, Indiana’s expected competitive procurement for an automated license plate reader (ALPR) ecosystem to replace a prior vendor relationship. Public statements from the City emphasize **privacy protections, transparency, accountability, public trust**, and **governance** during transition, alongside **documented investigative value** ([City news release, 2026-04-15](https://bloomington.in.gov/news/2026/04/15/6521)).

MITC’s thesis (2026-05-14) requires a **complete, lean** set of artifacts:

1. Business plan  
2. Hardware and software specification  
3. Comprehensive proposal paper  
4. Pitch deck  
5. Contract bid cover / introductory letter  

Additional constraints from the thesis:

- **Operate solely open-source software and protocols** where practicable for the solution MITC delivers.  
- Prefer **open-source or commodity / COTS** camera and network infrastructure.  
- **Data transfer, processing, and retention must be local**: server **in-city**, not vendor-cloud custody for Bloomington’s operational data.

Organizational methodology (`AGENTS.md`) requires **architecture decisions to precede implementation**, **chronological logging**, and **traceable branching**. This repository’s first “implementation” is the bid package itself, not runtime ALPR software.

## Decision

We will produce the five thesis artifacts as **version-controlled Markdown** under `docs/`, preceded by this ADR and closed with an After Action Report. We will add a **deterministic verification script** (`scripts/verify-deliverables.sh`) that fails if required files are missing or are trivially short, and requires the proposal and specification to explicitly encode **local custody** and **open / standards-based stack** commitments.

Repository navigation will live in `README.md`; process notes in `LOG.md`.

## Alternatives considered

1. **Monolithic Word/PDF-only deliverables** — Rejected for this phase: harder to diff, review, and iterate; we can export from Markdown later.  
2. **Prototype ALPR codebase in-repo** — Deferred: procurement materials are the gating artifact; a reference implementation belongs in a separate repo with computer-vision test harnesses.  
3. **Vendor-specific lock-in in the narrative** — Rejected: conflicts with thesis and with the City’s described procurement posture.

## Consequences

### Positive

- **Transparency**: Internal and municipal reviewers can see exact wording evolution.  
- **Mechanical completeness**: The verify script encodes acceptance criteria.  
- **Alignment**: Local custody and OSS/COTS positioning are enforced by checks and by narrative.

### Negative / risks

- **Markdown is not the final municipal format**: Conversion and official submission packaging may still be required.  
- **No published RFP number at authoring time**: Pricing and legal terms remain **indicative** pending solicitation documents.

## Success criteria

| Criterion | Measure |
|-----------|---------|
| Thesis artifacts exist | All five documents present under `docs/` |
| Lean but complete | Each document answers its audience’s decisions without boilerplate padding |
| Local custody | Explicit architecture and governance for in-city processing and storage |
| Open stack | Specification names protocols and OSS components or clearly justified COTS |
| Traceability | ADR + AAR + `LOG.md` entry; git branch `adr/0001-bloomington-alpr-bid-package` merged to `master` |

## Failure criteria

- Any thesis artifact missing or materially shortened to evade review.  
- Proposal recommending vendor-cloud primary custody for reads, hotlists, or evidentiary imagery without City-directed exception.  
- Inability to pass `scripts/verify-deliverables.sh` on `master` after merge.
