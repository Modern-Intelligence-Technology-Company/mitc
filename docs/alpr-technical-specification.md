# MITC — Hardware and Software Specification  
### Automated License Plate Reader (ALPR) Program — City of Bloomington, Indiana (target)

**Document version:** 2026-05-14  
**Classification:** Municipal procurement technical volume (draft)  
**Custody model:** **On-premise / in-city** primary data plane (no vendor-cloud requirement for reads, images, or indexes)

---

## 1. Purpose and scope

This specification defines a **reference architecture** MITC proposes for replacing and improving Bloomington’s ALPR capabilities using **commodity network and camera hardware** and **open-source-first software** orchestrated on **servers located in Bloomington**. It is written to align with publicly described fleet scale (11 fixed ALPR, 4 fixed video, 4 mobile trailer systems) and governance themes emphasized in City communications (privacy, transparency, accountability, local control).

**Out of scope unless separately authorized:** facial recognition analytics, dragnet marketing analytics unrelated to active cases, and participation in proprietary national correlation networks without written policy.

---

## 2. Reference architecture overview

### 2.1 Logical tiers

1. **Field tier — edge sensors**  
   - IP cameras (plate-optimized or general surveillance) using standard **RTSP**/**ONVIF** control plane.  
   - Optional **edge compute** (small Linux appliance) for buffering, TLS, or **edge inference** when backhaul is constrained.

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

All **primary storage and indexing of plate reads, thumbnails, and search audit logs** reside on **in-city** systems. Off-site backups, if used, are **optional**, **encrypted**, **client-controlled**, and **documentedd** in the system security plan—never a covert vendor repository.

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

**Representative COTS families (non-exclusive):** Axis Communications (market-leading reliability), Hanwha Vision, Uniview, and other **NDAA-compliant** options as required by City policy.

**Plate-optimized cameras** (multi-exposure HDR burst) may replace baseline at hot sites; still must expose **RTSP** and **ONVIF** for interoperability.

### 3.2 Mobile trailer systems

| Subsystem | Specification |
|-----------|----------------|
| Mast / camera mount | Stable in wind per INDOT-adjacent practice; vibration damping |
| Compute | Ruggedized **Linux** NUC or 1U short-depth server; optional **GPU** |
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

---

## 4. Software specification — open-source stack

### 4.1 Container orchestration and observability

- **Docker** / **Compose** for pilot; **k3s** or **Kubernetes** for HA production if City IT prefers.  
- **Prometheus** + **Grafana** for metrics (open source).  
- **OpenTelemetry** exporters for tracing ingest pipelines.  
- **Loki** or **Elasticsearch** (open) for_logs **only if** retention matches policy (often shorter than plate retention).

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

1. **Inventory** existing pole assets, circuits, and network paths.  
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
