# Citywide install CAPEX — Bloomington-class planning scenarios

**Document version:** 2026-05-15  
**Audience:** City finance, council packets, MITC internal planning  
**Disclaimer:** These figures are **illustrative engineering–finance estimates** built from **transparent assumptions** in [`mvp/budget/calculator.py`](../mvp/budget/calculator.py). They are **not** a bid, **not** a guarantee, and **not** a substitute for bonded construction quotes, prevailing-wage audits, or insurer-reviewed schedules. Indiana procurement rules and tax treatment may change totals.

## Why multiple channel counts?

Bloomington’s **headline** public tally (**11 + 4 fixed + 4 trailers** → often summarized as **~19** “systems”) can diverge from **third-party** inventories such as **[DeFlock](https://maps.deflock.org/?lat=39.1670&lng=-86.5343&zoom=11.00)** (~**40** markers). Budgets should **stress** central compute and field labor across **both** narratives until CMMS, permits, and walk-down surveys **reconcile** the definitive **RTSP channel** count.

This document provides **19, 30, 40, and 50** concurrent ingest **channels**—covering official baseline, intermediate growth, DeFlock-class density, and spare-capacity planning.

## Assumption summary (mid scenario defaults)

| Element | Mid-case planning value | Notes |
|---------|------------------------|--------|
| Camera + lens class | **$3,200** / channel | COTS municipal bullet / box tier (not consumer retail) |
| Field install bundle | **$2,800** / channel | Labor, bucket-truck allocation, PoE/fiber **share**, aiming |
| Decommission / make-good | **$450** / channel | Prior vendor hardware removal, pad cleanup alloc |
| Central platform base | **$118,000** | Core switching slice, **HA** inference pair alloc, storage controller start |
| Central step-tranche | **+$32,000** per **10** channels beyond **20** | Extra GPU decode, NIC headroom, queue throughput |
| NRE (fixed) | **$185,000** | Pilot, integrations skeleton, training materials, transparency artifacts |
| Integration allowance | **$28,000** + **$180** × channels | City PM, inspection, contingent civil |
| Contingency | **12.5%** × (field + central + integration allowance) | Excludes NRE to avoid double-counting program risk |
| Low / high scenarios | **±18%** on **field unit** bundle only | See calculator (`low` / `high` multipliers) |

**OPEX** (staffing, power, LTE on trailers, support contracts) is **not** included here—only **one-time / capital-weighted** program costs suitable for rough **replacement program** sizing.

## Totals by scenario (USD, rounded)

### Scenario: **low** (auto-generated; run `python scripts/render_budget_tables.py`)

| Channels | Field (est.) | Central platform | Integration allow. | Contingency (12.5%) | NRE (fixed) | **Total (USD)** |
|----------|--------------|------------------|--------------------|---------------------|-------------|-----------------|
| 19 | $100,491 | $118,000 | $31,420 | $31,239 | $185,000 | **$466,150** |
| 30 | $158,670 | $150,000 | $33,400 | $42,759 | $185,000 | **$569,829** |
| 40 | $211,560 | $182,000 | $35,200 | $53,595 | $185,000 | **$667,355** |
| 50 | $264,450 | $214,000 | $37,000 | $64,431 | $185,000 | **$764,881** |

### Scenario: **mid** (auto-generated; run `python scripts/render_budget_tables.py`)

| Channels | Field (est.) | Central platform | Integration allow. | Contingency (12.5%) | NRE (fixed) | **Total (USD)** |
|----------|--------------|------------------|--------------------|---------------------|-------------|-----------------|
| 19 | $122,550 | $118,000 | $31,420 | $33,996 | $185,000 | **$490,966** |
| 30 | $193,500 | $150,000 | $33,400 | $47,112 | $185,000 | **$609,012** |
| 40 | $258,000 | $182,000 | $35,200 | $59,400 | $185,000 | **$719,600** |
| 50 | $322,500 | $214,000 | $37,000 | $71,688 | $185,000 | **$830,188** |

### Scenario: **high** (auto-generated; run `python scripts/render_budget_tables.py`)

| Channels | Field (est.) | Central platform | Integration allow. | Contingency (12.5%) | NRE (fixed) | **Total (USD)** |
|----------|--------------|------------------|--------------------|---------------------|-------------|-----------------|
| 19 | $144,609 | $118,000 | $31,420 | $36,754 | $185,000 | **$515,783** |
| 30 | $228,330 | $150,000 | $33,400 | $51,466 | $185,000 | **$648,196** |
| 40 | $304,440 | $182,000 | $35,200 | $65,205 | $185,000 | **$771,845** |
| 50 | $380,550 | $214,000 | $37,000 | $78,944 | $185,000 | **$895,494** |

## How to regenerate

After editing **`mvp/budget/calculator.py`**, refresh the tables above:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
PYTHONPATH=. .venv/bin/python scripts/render_budget_tables.py
```

Copy the printed Markdown into this file under each scenario heading (or extend the script to patch this document automatically in a later iteration).

## Cross-references

- **ADR:** [`docs/adr/0002-mvp-simulated-ingest-and-budget-model.md`](adr/0002-mvp-simulated-ingest-and-budget-model.md)  
- **Lab MVP:** [`mvp/README.md`](../mvp/README.md)  
- **Technical sizing context:** `docs/alpr-technical-specification.md` §3.4
