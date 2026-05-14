# Modern Intelligence Technology Company (MITC) — Lean Business Plan

**Version:** 2026-05-14  
**Audience:** Founders, municipal clients, partners  
**Scope:** Bloomington, Indiana ALPR modernization opportunity as anchor use case

---

## 1. Executive summary

MITC is a Bloomington-based company delivering **surveillance-adjacent intelligence and IT infrastructure** for **small and mid-sized communities** that must meet public-safety outcomes under **strong local governance**. Our differentiation is **local custody of sensitive data**, **open-source-first engineering**, and **commodity hardware**—reducing long-run vendor lock-in and increasing transparency for councils and residents.

We are anchoring near-term revenue on a **City of Bloomington ALPR ecosystem replacement**: cameras and network on public rights-of-way, with **capture, decoding, hotlist matching, audit, and retention executed on servers physically located in Bloomington**, not in a national vendor cloud. Public communications from the City emphasize privacy, accountability, and trust alongside investigative utility; our offer is engineered to make those commitments **operationally true**, not merely rhetorical.

---

## 2. Company purpose and principles

**Mission.** Equip local governments with modern sensing and data tools that remain **under local law, local policy, and local operational control**.

**Operating principles.**

1. **Locality:** Primary data plane stays in jurisdiction unless the client directs otherwise in writing.  
2. **Openness:** Prefer **open-source software** and **documented protocols**; disclose components and supply chain.  
3. **Proportionality:** Scope retention, sharing, and analytics to policy—not to vendor defaults.  
4. **Evidence hygiene:** Design for discovery, retention holds, and chain-of-custody workflows common to prosecutors and civil oversight.  
5. **Field pragmatism:** Solutions must run on **COTS cameras** (stream-only discipline at the pole; see technical spec for **manufacturer catalog links**), **standard IP networks**, and **maintainable** Linux infrastructure.

---

## 3. Market context — Bloomington

**Situational facts (public record, April 2026).** The City’s prior license plate reader subscription arrangement with **Flock Safety** ended **2026-03-05**; leadership publicly framed a transition period with tightened access and **no outside data sharing** while evaluating replacements. The installed base described includes **11 fixed ALPR cameras**, **4 fixed video cameras**, and **4 mobile trailer systems** capable of ALPR and video (and other modalities).

**Competitive reference.** **Flock** exemplifies the **integrated national SaaS + proprietary camera** pattern MITC replaces with **local servers**, **COTS ONVIF imagers** (specific manufacturer links in the technical volume), and **auditable open-source** middleware.

**Buyer needs implied by public messaging.**

- Replace or exceed investigative utility **without** reintroducing unwanted national-network exposure.  
- Preserve or strengthen **auditability**, role separation, and policy alignment (retention, access justification, training).  
- Provide a procurement path that satisfies **community scrutiny** and council reporting expectations.

**MITC thesis alignment.** Bloomington’s stated direction matches our core product thesis: **on-prem / in-city** compute and storage, open components, and commodity sensors.

---

## 4. Product / service definition

### 4.1 What we sell

End-to-end **program delivery** for municipally owned ALPR:

- **Site survey and coverage modeling** for choke points and evidentiary quality.  
- **Procurement support** for COTS cameras, poles, power, backhaul, and mobile trailer integrations.  
- **In-city platform deployment**: GPU-capable inference hosts, redundant storage, backup, logging, identity and access management.  
- **Application layer**: plate detection/OCR pipelines using auditable open-source models and services; case workflows; exports.  
- **Integration**: CAD/RMS-adjacent exports where available; evidence packaging; prosecutor-ready disclosure support.  
- **Operations**: patch cadence, health monitoring, and **resident-accessible transparency reporting** (aggregate statistics, policy attestations).

### 4.2 What we intentionally do not sell

- A **proprietary national “correlate everyone” graph** operated by MITC.  
- **Facial recognition** as a bundled product (out of scope for this program unless the City separately authorizes distinct systems and policy).  
- **Sole-source mystery appliances** without exportable configurations and disaster-recovery runbooks.

---

## 5. Go-to-market

**Primary channel:** Formal municipal solicitations (RFP/IFB) and **piggyback-friendly** contract vehicles where Indiana law permits.

**Near-term pipeline:**

1. **Bloomington** — comprehensive response with pilot milestone.  
2. **Monroe County adjacent agencies** — data sharing only per written MOUs after Bloomington platform stabilizes.  
3. **Demonstration exports** — anonymized performance and uptime metrics suitable for council packets.

**Messaging pillar:** “**Bloomington’s servers, Bloomington’s rules, inspectable stack.**”

---

## 6. Operations model

**Core team roles (lean).**

- **Program lead / municipal liaison** — procurement, reporting, success criteria.  
- **Security and infrastructure** — Linux hardening, TLS, backups, IAM, patching.  
- **Computer vision engineer** — model validation, calibration per site, drift monitoring.  
- **Field technician bench** — camera alignment, physical security of enclosures, trailer connectivity.

**Service levels (target, to be finalized in contract):**

- **Availability** of central platform: 99.5% excluding City network and utility outages.  
- **Incident response** P1: remote triage within 30 minutes during service windows; on-site within SLA table.  
- **Transparency deliverables**: quarterly council-ready summary of errors, retention purges, and access log anomalies.

---

## 7. Financial plan (lean, indicative)

**Revenue model — hybrid:**

- **Non-recurring engineering (NRE)** for migration, integration, and acceptance testing.  
- **Equipment pass-through** with documented markup cap or administrative fee (per solicitation rules).  
- **Annual operations subscription** tied to patch/backup/monitoring and a pooled on-call block.

**Illustrative structure (placeholder until RFP pricing grids are released):**

| Phase | Description | Indicative range |
|-------|-------------|-------------------|
| Phase A | Pilot (2–3 sites + lab acceptance) | $[^1] |
| Phase B | Full fleet cutover (11+4+4 equivalents) | $[^1] |
| Phase C | Annual operations (per year) | $[^1] |

[^1]: Final figures require official solicitation documents, insurance/bonding costs, and site-specific civil electrical work.

**Cost drivers:** GPU hosts, licensed LTE on trailers if used, storage growth with retention policy, forensic export labor spikes during major cases.

**Margin discipline:** Maintain spare hardware pool for **fail-fast replacement** on critical sites to avoid investigative downtime.

---

## 8. Risks and mitigations

| Risk | Mitigation |
|------|------------|
| Plate OCR accuracy varies by lane angle and glare | Site-based acceptance tests; auxiliary illuminator placement; dual-shutter strategies |
| Political opposition to ALPR | Transparency portal; strict access controls matching or exceeding prior public commitments |
| Procurement protest timelines | Early vendor-neutral design; documented evaluation matrix tied to published criteria |
| Staff turnover at PD | Train-the-trainer; configuration as code; video runbooks |
| Evidence challenges | Hashing, time sync to UTC with audit trail, export formats with provenance metadata |

---

## 9. Milestones (0–12 months)

1. **M0** — Issue draft technical volumes + pricing templates upon RFP release.  
2. **M1** — **90-day pilot** with measurable reads/day, false positive rate bands, and uptime.  
3. **M2** — Production acceptance for fixed sites; trailer migrations staged.  
4. **M3** — Independent **policy/audit review** walkthrough with City legal and oversight partners.  
5. **M4** — Steady-state operations; annual optimization on model refresh and storage economics.

---

## 10. Conclusion

MITC’s lean plan concentrates capital and attention on a **credible municipal alternative**: investigative tooling that respects **local sovereignty over data**. Bloomington’s public framing in 2026 rewards vendors who can **prove locality**, **document openness**, and **operationalize accountability**—not merely promise it.
