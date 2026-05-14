# Comprehensive Proposal Paper  
### Local, Open-Source-First ALPR Platform and Services — City of Bloomington, Indiana

**Offeror:** Modern Intelligence Technology Company (MITC), Bloomington, Indiana  
**Date:** 2026-05-14  
**Reference:** Municipal ALPR modernization / replacement program (RFP / solicitation number **TBD**)

---

## Executive overview

MITC submits this paper in support of Bloomington’s next chapter for **automated license plate reader (ALPR)** capability. Public leadership has made plain that any future system must **balance public safety with privacy protections, transparency, accountability, and public trust**, while responsibly transitioning off a prior commercial relationship ([City news release, 2026-04-15](https://bloomington.in.gov/news/2026/04/15/6521)).

MITC’s response is simple in principle and rigorous in execution:

1. **Bloomington’s data stays in Bloomington** — plate imagery, reads, indexes, operator audit logs, and configured hotlists are **processed and stored on in-city servers** you control, within facilities and networks you govern.  
2. **Open-source-first** — we deliver on **Linux** using **open protocols** and **auditable open-source components** for orchestration, storage, and ALPR pipelines; proprietary parts are avoided unless a solicitation or interoperability mandate requires a justified exception.  
3. **Commodity infrastructure** — cameras, switches, and compute are **COTS** wherever possible, easing replacement and competitive maintenance.  
4. **Operational honesty** — we propose a **pilot**, published acceptance tests, and council-ready transparency artifacts rather than unsubstantiated marketing claims.

This document should be read with the companion **Hardware and Software Specification**, **Lean Business Plan**, and pricing schedules **to be finalized** when official IFB/RFP documents and insurance/bonding grids are issued.

---

## 1. Understanding Bloomington’s situation

### 1.1 Transition context

The City’s prior **Flock** arrangement concluded **2026-03-05** without renewal; leadership described immediate transition measures **limiting access to Bloomington Police Department personnel**, **ending outside data sharing**, and removing Bloomington cameras from **national network visibility** during evaluation.

### 1.2 Physical footprint described publicly

The City described **11 permanently mounted license plate reader cameras**, **four permanently mounted video cameras**, and **four mobile trailer systems** equipped for **license plate reading, video recording, and gunshot detection**.

MITC’s implementation plan treats this inventory as the **baseline scope** for capacity planning and cutover sequencing, subject to field verification.

### 1.3 Governance expectations

Public materials reference **BPD** practices consistent with **retention limits**, **search logging**, **role-based access**, **training**, and **periodic audits**. MITC encodes these as **policy-as-code**—not informal habits—so oversight is reproducible after staff turnover.

---

## 2. Technical approach — local custody by design

### 2.1 What “local” means in our architecture

- **In-city primary datastore** for plate crops, contextual frames, structured reads, and audit logs.  
- **No mandatory vendor cloud** for ingest, search, or operator workflows.  
- Optional **encrypted backups** exist only under **written** City direction and key custody.  
- Trailers and remote sites **tunnel** to **Bloomington** endpoints—never to MITC-operated multi-tenant SaaS.

### 2.2 Why this matches Bloomington’s 2026 messaging

The City emphasized **narrow parameters**, **strong accountability**, and **clear public safeguards**. Architectures that **physically locate** sensitive operational data in Bloomington and publish **software transparency** (SBOMs, open licenses) are structurally easier to audit than opaque hosted dashboards.

### 2.3 Security and resilience

We implement **defense-in-depth**: network segmentation, **TLS**, **disk encryption**, **role-separated access**, **append-only auditing**, and **monitoring** with **Prometheus/Grafana**. Incident response runbooks include **evidence preservation** steps for legal holds.

---

## 3. Scope of work

### 3.1 MITC responsibilities

1. **Program management** — single accountable manager; weekly status; council packet support as required.  
2. **Site surveys** — line-of-sight, lighting, pole loading, civil power, and backhaul.  
3. **Engineering** — network design, IP plans, tunnel architecture, time sync design.  
4. **Procurement support** — BOM transparency; factory warranties coordinated.  
5. **Installation** — cameras, enclosures, trailer integrations, labeling, as-built documentation.  
6. **Software deployment** — containerized stack on City-approved hosts; **configuration as code**.  
7. **Data migration** — if legacy exports are lawfully obtainable, **ETL** into new retention policy; otherwise parallel start with documented chain of custody.  
8. **Training** — analysts, evidence techs, and IT administrators.  
9. **Acceptance testing** — KPIs for accuracy, latency, uptime; remediation sprint if needed.  
10. **Hypercare + steady-state** — ticketed support, patching cadence, hardware sparing.

### 3.2 City / BPD responsibilities (shared success)

- Timely decisions on **sites**, **facilities**, and **IT standards**.  
- **RMS/CAD** integration interfaces and test sandboxes.  
- **Legal** approval of retention, sharing, and public dashboard content.  
- **Facilities** access and **utility** coordination.

---

## 4. Implementation schedule (indicative)

| Phase | Duration | Milestones |
|-------|----------|------------|
| **Intake** | 2–4 weeks | Confirm scope, security review kickoff, rack space |
| **Pilot** | 8–12 weeks | 2–3 representative sites + trailer lab; KPI report |
| **Scale-out** | 12–20 weeks | Roll fixed sites; migrate/stage trailers |
| **Stabilization** | 4–8 weeks | Hardening, DRP test, admin handoff |
| **Operate** | Ongoing | Patching, on-call, quarterly transparency report |

Exact dates depend on procurement award date, supply chain, and **not-before** restrictions on street works.

---

## 5. Pricing and commercial terms (placeholders)

MITC will complete official pricing worksheets upon release. Commercial structure anticipated:

- **NRE** migration + engineering  
- **Equipment** (pass-through or disclosed markup per rules)  
- **Annual operations** subscription

We will comply with **Indiana** public purchasing statutes, **tax** requirements, and any **local preference** clauses if lawfully included.

---

## 6. Evaluation criteria alignment (preview)

Where solicitations score **technical merit**, MITC highlights:

| Typical criterion | MITC evidence |
|-------------------|----------------|
| Understanding needs | This paper + specification cite City disclosures |
| Technical quality | Containerized HA design; GPU sizing methodology |
| Security | Encryption, RBAC, audit design |
| Privacy alignment | Local custody; national net opt-out by architecture |
| Past performance | References to be attached (startup: pilot references + personnel resumes) |

---

## 7. Risk management and quality assurance

- **Model risk:** Site-calibrated acceptance; continuous monitoring for drift.  
- **Supply chain risk:** Dual-sourced camera SKUs where possible.  
- **Legal discovery risk:** Export tooling and retention holds engineered-in.  
- **Political risk:** Transparency dashboard and documented access patterns.

---

## 8. Ethics and community commitments

MITC will not market capabilities that encourage **dragnet** use inconsistent with Bloomington’s published direction. We will cooperate with **reasonable oversight mechanisms** requested by the City, including access to **aggregate** performance measures suitable for public reporting.

---

## 9. Conclusion

Bloomington asked for technologies and providers that **better balance public safety needs with privacy protections, transparency, accountability, and public trust**. MITC’s answer is an **in-city, open-source-first ALPR platform** paired with disciplined program delivery—designed so tomorrow’s council can **verify** what yesterday’s system did, without needing permission from a distant vendor.

We welcome the opportunity to present a live architecture review and walk through a **pilot plan** tuned to Bloomington’s streets, policies, and people.

### Signatures (execution copy)

Prepared by: _________________________________ Date: __________  
Authorized officer, MITC: __________________________ Date: __________

---

## Appendices (to attach in final packet)

- **Appendix A:** Resumes / qualifications  
- **Appendix B:** Insurance certificates (TBD coverage levels)  
- **Appendix C:** SBOM example export  
- **Appendix D:** Sample SLA table  
- **Appendix E:** References / letters (as available)
