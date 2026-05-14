# MITC — Pitch Deck (Markdown source)  
### Bloomington ALPR: Local custody, open stack, municipal control

**How to use this file:** Each top-level **Slide** section maps one projection slide. Export to PowerPoint/PDF via your preferred Markdown-to-deck workflow.

---

## Slide 1 — Title

**Modern Intelligence Technology Company (MITC)**  
**Bloomington-built public safety infrastructure**

*ALPR modernization — local servers, open-source core, commodity hardware*

Presenter / date: ______________ / 2026-05-14

---

## Slide 2 — The moment

Bloomington is **transitioning** its prior ALPR vendor relationship while emphasizing:

- **Privacy** and **civil liberties**  
- **Transparency** + **accountability**  
- **Public trust** alongside **investigative utility**

**Source:** City announcement, April 15, 2026 — contract end March 5, 2026; transition governance tightening.

---

## Slide 3 — What the City said it needs

- Evaluate replacements that are **not tied** to unwanted national network models  
- **Govern** access, retention, and sharing with **documented** safeguards  
- Maintain capacity for **serious case** support described in public examples  

**Fleet / budget hint:** City news cites **11+4+4** “systems,” while community **[DeFlock](https://maps.deflock.org/?lat=39.1670&lng=-86.5343&zoom=11.00)** maps **~40** prior **Flock** markers — **scope & central budget scale** with the **verified channel count**, not the shortest headline.

---

## Slide 4 — MITC thesis

**Small communities deserve enterprise-grade tools without surrendering local sovereignty.**

- **On-premise / in-city** custody by default  
- **Open-source-first** software + standard protocols  
- **COTS** cameras and network gear  
- Engineers who can **explain** the stack to councils and oversight partners

---

## Slide 5 — Product: not a dashboard, a platform

**Bloomington-operated data plane**

- Plate **detect → OCR → index → audit** on **your Linux clusters**  
- **PostgreSQL** + **object storage** (e.g., **MinIO**) + **container** services  
- **Hotlists** and case workflows **without** mandatory vendor clouds  
- **Exports** built for prosecutors and **civil oversight**

---

## Slide 6 — Architecture (one picture in words)

**Cameras (ONVIF/RTSP, intentionally thin at the pole)** → **encrypted backhaul** → **Bloomington GPU hosts** → **encrypted storage** → **RBAC portal**  
*Field imagers avoid authoritative on-camera ALPR so **loss or theft of a camera does not equal loss of investigative logic or read history**.*  
Sidecars: metrics (**Prometheus/Grafana**), immutable **auditd**, **retentiond**

---

## Slide 7 — Open-source anchors (examples)

- **Linux**, **Docker** / **Kubernetes** packaging  
- **Prometheus**, **Grafana**, **Traefik/nginx** patterns  
- **PostgreSQL**, **MinIO**  
- **ALPR** pipelines using **auditable OSS** models / ONNX runtimes

*Exact model set finalized during pilot benchmarks and license review.*

---

## Slide 8 — Deployment plan

1. **Intake & security** alignment  
2. **Pilot** on 2–3 sites + trailer lab — measurable KPIs  
3. **Scale** across fixed + mobile footprint  
4. **Stabilize** + **DR test**  
5. **Operate** with quarterly transparency reporting

---

## Slide 9 — Why we win councils, not just RFPs

- **SBOM** transparency — fewer “black box” objections  
- **Policy-as-code** — retention and access rules survive personnel churn  
- **Local jobs** — Bloomington company, Bloomington racks  
- **No surprises** — capacity planning tied to your real lane geometry

---

## Slide 10 — Risk honesty

- Plate OCR is **physics + geometry** — we **accept with testing**, not hype  
- Trailers add **LTE** complexity — we **engineer** failover paths  
- Politics matters — we ship **aggregate dashboards** aligned to your comfort level

---

## Slide 11 — Commercial shape (preview)

- **NRE** for engineering + migration  
- **Equipment** with clear BOM — **scoped to reconciled camera census** (**~40** **[DeFlock](https://maps.deflock.org/?lat=39.1670&lng=-86.5343&zoom=11.00)** **stress** vs **11+4+4** **headline** until field verification)  
- **Unit rates** (per channel / per GPU / per TB-month) so totals flex with the final site list  
- **Annual ops** for patch/monitor/on-call  

*Official numbers track the published solicitation; pricing assumes **capacity for DeFlock-class density** until the City locks quantities.*

---

## Slide 12 — Ask / next step

**Request:** Technical deep-dive with **BPD**, **IT**, **legal**, and council liaisons  
**Deliver within 30 days of award:** **Pilot readiness package** + rack diagrams + training outline

**Contact:** _________________________________________

---

## Speaker notes (non-slide)

- Emphasize **in-city** storage when answering privacy questions.  
- Offer to **map** current policy paragraphs to software controls line-by-line.  
- If challenged on accuracy, pivot to **pilot methodology** and independent spot checks.
