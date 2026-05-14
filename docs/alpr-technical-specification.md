# MITC — Hardware and Software Specification  
### Automated License Plate Reader (ALPR) Program — City of Bloomington, Indiana (target)

**Document version:** 2026-05-14  
**Classification:** Municipal procurement technical volume (draft)  
**Custody model:** **On-premise / in-city** primary data plane (no vendor-cloud requirement for reads, images, or indexes)

---

## 1. Purpose and scope

This specification defines a **reference architecture** MITC proposes for replacing and improving Bloomington’s ALPR capabilities using **commodity network and camera hardware** and **open-source-first software** orchestrated on **servers located in Bloomington**. It aligns with **governance** themes in City communications (privacy, transparency, accountability, local control), while treating **camera quantities** as a **reconciliation problem** between (a) the **headline public fleet description** and (b) a **higher-density, third-party planning map**.

**Official public footprint (City communications):** **11** fixed ALPR positions, **4** fixed video positions, and **4** mobile trailer systems—often summarized as **~19** “systems,” noting trailers may host **more than one** imager each.

**Third-party planning stress case (~40 channels):** The community-maintained **[DeFlock map (Bloomington-centered)](https://maps.deflock.org/?lat=39.1670&lng=-86.5343&zoom=11.00)** displays on the order of **~40** markers associated with the prior **Flock** deployment in the Bloomington area. DeFlock is **not** a legal inventory; MITC uses it **only** as a **budget and capacity bracket** for **concurrent ingest**, **GPU decode**, **aggregation backhaul**, and **storage** until the City’s **authoritative site list**, **permits**, and **as-built** survey close the gap.

**Out of scope unless separately authorized:** facial recognition analytics, dragnet marketing analytics unrelated to active cases, and participation in proprietary national correlation networks without written policy.

---

## 2. Reference architecture overview

### 2.1 Logical tiers

1. **Field tier — minimal-footprint imagers**  
   - **IP cameras** (plate-optimized or general surveillance) that function primarily as **imagers and encoders**, exposing standard **RTSP** and **ONVIF** control. **PoE** and **IP66+** outdoor ratings reduce separate power plant complexity at the pole.  
   - **Footprint discipline:** **Dedicated camera installations are minimized** in **electrical parts count**, **ancillary enclosures**, and **maintenance surfaces**. Each extra field computer or nested subsystem adds **failure modes** and **truck rolls**.  
   - **Theft, vandalism, and destruction:** Cameras on public rights-of-way are **physical targets**. MITC therefore **does not treat on-camera ALPR, on-camera hotlist logic, or on-camera storage of reads** as the **authoritative** path. *Routine H.264/H.265 encoding on the camera is normal COTS behavior and is not equated here with “edge ALPR.”* If a camera is **removed or compromised**, residual risk must **not** extend to **City decryption keys, model artifacts, investigative hotlists, or indexed read history**. **Inference, matching, retention, audit, and export** occur on **in-city** servers under City **physical and logical** control.  
   - **Optional buffering only:** Where backhaul is exceptionally constrained, an **in-cabinet** network appliance (not mounted on the camera mast) may queue **encrypted** egress to Bloomington. **On-camera edge inference** is **out of scope** for the default MITC design.

2. **Transport tier — municipal network**  
   - **IPsec** or **MACsec** where available; minimally **TLS 1.3** overlays for management.  
   - **Segmented VLANs** isolating camera traffic from general enterprise clients.  
   - **NTP** time synchronization (chrony) with stratum-1 or GPS-disciplined source on **in-city** network.

3. **Platform tier — Bloomington data center / secure server room**  
   - **Kubernetes** or **Docker Compose** on **Linux** for service packaging (MITC default: containerized services for repeatability).  
   - **Inference hosts** with **NVIDIA CUDA**-capable GPUs for real-time decode where needed; CPU-only fallback for low-throughput sites after validation.  
   - **PostgreSQL** (relational metadata, users/roles, policies, audit events).  
   - **Object storage** compatible with **S3 API** (e.g., **MinIO**—open source) for encrypted plate crops and full frames per retention policy.  
   - **Message queue** (e.g., **NATS** or **Redis Streams**) for ingest backpressure.

4. **Access tier — operator and oversight**  
   - **Web application** over HTTPS with **OIDC** integration optional (Keycloak—open source—or existing IdP).  
   - **Role-based access control** aligned to sworn vs analyst vs admin roles.  
   - **Immutable audit log** stream to append-only store (e.g., syslog to WORM appliance or cloud-isolated SIEM **only if City approves**; default remains local).

### 2.2 Custody boundaries

All **primary storage and indexing of plate reads, thumbnails, and search audit logs** reside on **in-city** systems. Off-site backups, if used, are **optional**, **encrypted**, **client-controlled**, and **documented** in the system security plan—never a covert vendor repository.

---

## 3. Hardware specification

### 3.1 Fixed-site cameras (COTS emphasis)

**MITC baseline (configurable per site engineering study):**

| Component | Baseline | Notes |
|-----------|----------|--------|
| Form factor | Fixed bullet or box camera, IP66+ | Pole- or building-mounted |
| Sensor | ≥ 5 MP global shutter preferred | Rolling shutter acceptable only at tightly controlled shutter speeds |
| Lens | Motorized varifocal | Tuned for plate distance / lane width |
| IR / illuminator | 850 nm compliant with state traffic regs | Separate illuminator if vendor camera IR insufficient |
| Frame rate | 15–30 fps target during transits | Higher if blur risk |
| Streaming | **H.264**/**H.265** + **ONVIF Profile S/T** | Avoid proprietary transports for core path |
| Power | PoE++ where available | Local power meter logging for uptime forensics |

**Competitive reference.** Bloomington’s prior procurement direction included **Flock Safety**—a **vendor-operated**, **network-centric** ALPR offering that centralized operational value in the provider’s service. MITC’s architecture is the **deliberate inverse**: **City-operated** custody, **COTS imagers** speaking **open protocols**, and **software the City can audit**—without **mandatory** national correlation layers.

**Illustrative COTS models (manufacturer pages — nonexclusive; final SKU per site survey, pilot, and procurement rules):**

| Manufacturer | Example SKU | Manufacturer / catalog link |
|--------------|-------------|-----------------------------|
| Axis Communications | AXIS Q1805-LE (long-range 1080p IR bullet, 32× zoom) | [axis.com — AXIS Q1805-LE](https://www.axis.com/products/axis-q1805-le) |
| Hanwha Vision | PNO-A9081R (4K IR bullet, ONVIF S/G/T) | [hanwhavision.com — PNO-A9081R](https://www.hanwhavision.com/en/products/camera/network/bullet/pno-a9081r/) |
| Bosch Security and Safety Systems | DINION IP 5000i IR bullet NBE-5503-AL (5 MP varifocal) | [commerce.boschsecurity.com — NBE-5503-AL](https://commerce.boschsecurity.com/xl/en/Bullet-5MP-HDR-2-7-12mm-auto-IP67-IK10/p/F.01U.328.213/) |
| Uniview | IPC2B25SS-ADZK-I1 (5 MP LightHunter VF bullet) | [global.uniview.com — IPC2B25SS-ADZK-I1](https://global.uniview.com/Products/Network_Cameras/Prime_Series/PRIMEII_Series/IPC2B25SS-ADZK-I1/) |

MITC **ingests RTSP/H.264 or H.265 streams** from any of the above (and equivalent ONVIF peers). Cameras that ship with **optional** on-device analytics (e.g., plate apps, edge VMD) are configured so that **evidentiary ALPR** is **not** dependent on those features unless the City explicitly chooses otherwise. **Axis** publishes a companion [AXIS License Plate Verifier](https://www.axis.com/products/axis-license-plate-verifier) offering; MITC’s default is still **central decoding** on **Bloomington** hosts so **stolen cameras do not become stolen ALPR engines**. For federal or State-funded segments, **NDAA-compliant** lines (often Axis, Hanwha, Bosch families) supersede commodity listings where law requires.

**Plate-optimized cameras** (multi-exposure HDR burst) may replace baseline at hot sites; still must expose **RTSP** and **ONVIF** for interoperability.

**MVP reference SKU — “easiest” software positioning (MITC default).** Among commodity lines, **Axis**—specifically **[AXIS Q1805-LE](https://www.axis.com/products/axis-q1805-le)** for lab work—provides the **smoothest integration path** for an open-stack team: **RTSP** and **ONVIF Profiles S/T** are first-class, **VAPIX** HTTP APIs are documented for provisioning extras, and the vendor’s **operator-facing** stream-URL patterns are **stable** enough to script in CI. Competent alternatives (Hanwha, Bosch, others) remain fully supportable; Axis minimizes **time-to-first-frame** when engineers are scarce. The repository **`mvp/`** stack publishes a **synthetic RTSP** path (`simulated_axis`) so **ingest, decode, and orchestration** mature **before** poles are rewired; production swaps the URL for the Axis RTSP endpoint (or another ONVIF peer).

### 3.2 Mobile trailer systems

| Subsystem | Specification |
|-----------|----------------|
| Mast / camera mount | Stable in wind per INDOT-adjacent practice; vibration damping |
| Trailer compute | Ruggedized **Linux** NUC or short-depth 1U in **tamper-evident cabinet** (not mast-mounted); optional **GPU** — mast cameras remain **stream-only** peers |
| Storage | **Encrypted NVMe**; tamper-evident enclosure |
| Backhaul | **LTE/5G** modem with **dual-SIM**; **IPsec** tunnel to **in-city** platform |
| Power | Shore power + **battery/solar** options per trailer |
| Safety | Surge suppression, grounding, low-voltage disconnect |

Trailers synchronize to the **central Bloomington** cluster; **no** command/control through unaccountable third-party SaaS by default.

### 3.3 Data center / server hardware (in-city)

**Minimum production pair (HA):**

- **2× inference/application servers**: dual PSUs, **≥ 2× datacenter GPUs** (e.g., NVIDIA L4-class or better per throughput model), **512 GB RAM**, **dual 25 GbE** NICs.  
- **1× storage server** OR **JBOD** backing **MinIO** distributed mode: **≥  usable 80 TB** initial RAW capacity (scalable).  
- **UPS** + generator compatibility per City facilities standards.

Exact SKU selection happens after **pilot throughput** measurement (reads/sec, camera count, retention).

### 3.4 Budget-linked platform sizing (draft brackets — binding BoM after field verification)

| Planning band | Concurrent ingest endpoints (round numbers) | Typical platform implications |
|---------------|-----------------------------------------------|-------------------------------|
| **Band A — headline public tally** | ~15–20 HD-class streams | **§3.3** minimum **HA** inference pair often suffices after pilot tuning |
| **Band B — DeFlock-informed stress** | ~35–45 streams | Add **decode / GPU headroom** (extra datacenter GPU or additional inference node), **wider 25 GbE** or **100 GbE** spine if aggregating many sites, **higher MinIO RAW** tier and **message-queue** throughput |
| **Band C — verified as-built** | Per final RFP attachment | **Priced** quantities and SLAs **lock** here |

**Cost shape (qualitative):** **Field hardware** (cameras, mounts, PoE ports) scales **roughly linearly** with **confirmed** positions. **NRE** (integrations, policy-as-code porting, training) is **sub-linear**—a second tranche of cameras does **not** double engineering cost. **Object storage opex** scales **near-linearly** with **retention × frame policy × channel count**. MITC recommends a **10–15%** **hardware and integration contingency** until reconciling DeFlock-style counts with **City purchasing records** and **pole surveys**.

---

## 4. Software specification — open-source stack

### 4.1 Container orchestration and observability

- **Docker** / **Compose** for pilot; **k3s** or **Kubernetes** for HA production if City IT prefers.  
- **Prometheus** + **Grafana** for metrics (open source).  
- **OpenTelemetry** exporters for tracing ingest pipelines.  
- **Loki** or **Elasticsearch** (open) for logs **only if** retention matches policy (often shorter than plate retention).

### 4.2 Video management / ingestion (options)

MITC supports **one** primary path after pilot:

- **Frigate NVR** (open source, Docker-native) with detector pipelines; integrates with Home Assistant ecosystem patterns but used here as **police-grade NVR** with policy controls, or  
- **Shinobi** CE (open source) for multi-camera ingestion, or  
- **GStreamer**-based custom ingest with **low-latency** tuning.

Selection criteria: **stable RTSP**, **hardware decode**, **role integration**, and **export hooks** for ALPR pipeline.

### 4.3 ALPR inference layer (open models / OSS wrappers)

MITC will deploy a **modular ALPR service** behind an internal REST/gRPC API. Candidate engines for **on-prem** operation include combinations of:

- **Detection**: YOLO-family detectors (e.g., YOLOv8/YOLOv9 weights with permissive licensing) trained or fine-tuned for US plates.  
- **OCR**: specialized plate OCR models or CRNN pipelines exported to **ONNX** for CPU/GPU portability.  
- **Packaged OSS projects** for bootstrapping pilots: examples include community ALPR **Docker** stacks and lightweight CPU services (to be benchmarked; license compliance reviewed per component).

**Operational requirement:** Model artifacts, versions, and checksums are **configuration-as-code** checked into the City’s repo fork or MITC-maintained fork with **publicly readable** SPDX license metadata.

### 4.4 Application services (planned modules)

| Service | Responsibility | Notes |
|---------|----------------|-------|
| `ingest-rtsp` | Pull/decode streams | Hardware acceleration |
| `alpr-worker` | Detect + OCR | Horizontally scaled |
| `hotlist` | Local BOLO matching | No national net |
| `case-bridge` | Tie reads to RMS event numbers | Integrations per City |
| `auditd` | Append-only operator actions | Tamper resistance |
| `retentiond` | Policy-based purge + legal holds | Evidence flags |
| `exporter` | Discovery/redaction tooling | Prosecutor workflows |

### 4.5 Security controls

- **Disk encryption** (LUKS) on all Linux hosts; **TPM** sealing where available.  
- **mTLS** internal to cluster; **public** endpoints only behind **reverse proxy** (e.g., **Traefik** or **nginx**, both open).  
- **CIS** Linux benchmarks as baseline hardening.  
- **Vulnerability scanning** (e.g., **Trivy**, **Grype**) in CI for container images.  
- **Backup**: **restic**/**borg** to **City-owned** target; encryption keys held by City.

### 4.6 Interoperability and data formats

- **APIs**: OpenAPI-documented **REST**; **GeoJSON** optional for map overlays internal-only.  
- **Exports**: CSV/JSON with SHA-256 hashes; original images packaged as **zip** with **chain-of-custody** manifest.  
- **Standards alignment**: **ONVIF** camera control; **S3** API for object storage clients.

### 4.7 Development, simulation, and open protocol anchors (lab without hardware)

Municipal programs should not block software progress on **pole access**. The **wire contracts** that matter for ingest are **public specifications**, not proprietary camera firmware:

- **RTSP** — [RFC 2326](https://www.rfc-editor.org/rfc/rfc2326); **RTP** — [RFC 3550](https://www.rfc-editor.org/rfc/rfc3550). These define how **FFmpeg**, **GStreamer**, **Frigate**, and custom workers **pull** video.
- **H.264 / H.265** — standard encoder bitstreams; any compliant decoder path applies equally to **synthetic** and **field** sources.
- **ONVIF** — specifications freely downloadable from [onvif.org](https://www.onvif.org/) (device/service descriptions). ONVIF is **not** open-source firmware, but it **is** an open **API contract** for discovery, media profiles, and PTZ where applicable.

**MITC lab MVP (`mvp/`):** a **Docker Compose** stack runs **MediaMTX** (RTSP broker) plus **FFmpeg** (`lavfi` test pattern) publishing **`simulated_axis`**, mimicking a steady **TCP RTSP** camera feed. The **`ingest-smoke`** service runs **`ffprobe`** to prove the stream is decodable—the same probe pattern operators use when commissioning an **AXIS Q1805-LE**. Final integration is **`rtsp://…` URL + credentials** substitution, not a stack rewrite.

**Illustrative citywide CAPEX** scenarios (channel counts 19 / 30 / 40 / 50, low–mid–high) are modeled in **`mvp/budget/calculator.py`** with narrative in **`docs/budget-citywide-install.md`**.

---

## 5. Networking and cybersecurity

- **Zero-trust** posture between vehicles and core: trailers **home** to City IPsec endpoint, not generic internet exposure.  
- **Certificate**: **private CA** or **ACME** via City DNS; HSTS on all portals.  
- **Segmentation** cameras ↔ app ↔ admin jump hosts.  
- **IDS/IPS** optional at border per City IT — MITC supplies **suricata** configs if desired.

---

## 6. Performance and acceptance testing

**Pilot metrics (illustrative KPIs, finalized in contract):**

- Plate read rate vs truth set at **golden hour** and **night**.  
- **False positive** hotlist matches bounded per policy.  
- **End-to-end latency** from vehicle passage to operator visibility ≤ *T* seconds (site-dependent).  
- **Uptime** during probation period.

MITC proposes **capture of a labeled test corpus** under Bloomington supervision; models **do not** train on live production reads without explicit legal review.

---

## 7. Migration from prior vendor footprint

1. **Inventory** existing pole assets, circuits, and network paths—**cross-check** purchasing/CMMS data and field surveys against crowdsourced references such as **[DeFlock](https://maps.deflock.org/?lat=39.1670&lng=-86.5343&zoom=11.00)** (~**40** Bloomington-area markers at planning time) **without** treating the map as evidentiary.  
2. **Parallel run** (optional) with logically separated storage until acceptance.  
3. **Policy mapping** translate retention and access rules into **software policy objects**.  
4. **Training** for analysts and evidence technicians on export/redaction tooling.  
5. **Decommission** prior vendor tunneling and cloud credentials.

---

## 8. Transparency and public trust features

- **Public dashboard** (aggregate): camera count, **uptime**, **error rate**, **retention** schedule, **audit** summary (no investigative detail).  
- **Open documentation** of software bill of materials (SBOM).  
- **FOIA-aware** export tooling (batch redaction workflows).

---

## 9. Compliance notes (non-legal)

Indiana municipalities historically set **departmental policies** for ALPR absent exhaustive statewide mandates; MITC designs for **departmental and council oversight** comparable to Bloomington’s publicly described **BPD** practices (retention, access logging, periodic audits). Final compliance stance is **City Attorney**-approved.

---

## 10. Summary

MITC specifies a **modern, locally hosted ALPR platform** combining **COTS cameras**, **open-source orchestration**, **Docker**/**Kubernetes** packaging, **PostgreSQL** metadata, **MinIO** object storage, and **auditable OSS model** pipelines for plate detection and OCR—delivered so Bloomington’s investigative imagery and indexes remain **physically and logically in Bloomington**.
