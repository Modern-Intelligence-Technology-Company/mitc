"""
Illustrative citywide CAPEX estimator for Bloomington-class ALPR replacement.

All figures are *planning* numbers for multi-scenario comparison — not a bid,
not a quote, and not tax or bond advice. Adjust assumptions with procurement,
facilities, and civil engineering input before any public commitment.

Scaling logic (intentionally simple and auditable):
  - **Field** cost grows linearly with *confirmed RTSP channels*.
  - **Central platform** has a base stack; above a threshold, each block of
    extra channels adds a GPU/decode/network tranche (step function).
  - **NRE** is fixed per program (integration, policy porting, training skeleton).
  - **Contingency** applies to field + central + integration allowance only
    (NRE is already risk-loaded in the sense of program unknowns — excluded
    from contingency below to avoid double-counting; see SUMMARY in markdown).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

Scenario = Literal["low", "mid", "high"]


@dataclass(frozen=True)
class BudgetRow:
    """One row for reporting tables."""

    channels: int
    field_components_usd: float
    central_platform_usd: float
    nre_integration_usd: float
    integration_allowance_usd: float
    subtotal_usd: float
    contingency_usd: float
    total_usd: float


# --- Scenario multipliers on *field* unit costs (camera + install bundle) -----
_FIELD_MULTIPLIER: dict[Scenario, float] = {
    "low": 0.82,
    "mid": 1.0,
    "high": 1.18,
}


@dataclass(frozen=True)
class BudgetAssumptions:
    """
    Mid-case defaults approximate a municipal program mixing quality COTS,
    union/eligible labor, and modest spare-parts pool — 2026 planning context.
    """

    scenario: Scenario = "mid"
    # Per-channel field: camera body + lens class + mount hardware alloc (USD)
    camera_kit_usd: float = 3_200.0
    # Per-channel: install labor, bucket truck alloc, fiber/PoE port share (USD)
    field_install_usd: float = 2_800.0
    # Removal / make-good for prior vendor gear per channel (USD)
    decommission_per_channel_usd: float = 450.0
    # Rack GPUs, core switching slice, base storage controller (USD)
    central_base_usd: float = 118_000.0
    # Added central cost each time channels exceed `central_channel_threshold`
    # by one full `central_tranche_channels` step (USD)
    central_tranche_usd: float = 32_000.0
    central_channel_threshold: int = 20
    central_tranche_channels: int = 10
    # One-time program NRE: integrations, pilot, training materials (USD)
    nre_fixed_usd: float = 185_000.0
    # City PM / inspection / contingent civil (USD) — scales lightly with size
    integration_allowance_base_usd: float = 28_000.0
    integration_allowance_per_channel_usd: float = 180.0
    contingency_rate: float = 0.125  # 12.5% on field+central+integration allowance

    def field_unit(self) -> float:
        """Cost per channel before central/NRE."""
        m = _FIELD_MULTIPLIER[self.scenario]
        return m * (
            self.camera_kit_usd + self.field_install_usd + self.decommission_per_channel_usd
        )

    def central_platform(self, channels: int) -> float:
        if channels <= 0:
            return self.central_base_usd
        extra = max(0, channels - self.central_channel_threshold)
        tranches = (extra + self.central_tranche_channels - 1) // self.central_tranche_channels
        return self.central_base_usd + tranches * self.central_tranche_usd

    def integration_allowance(self, channels: int) -> float:
        return self.integration_allowance_base_usd + channels * self.integration_allowance_per_channel_usd


def estimate_citywide_capex(channels: int, asm: BudgetAssumptions | None = None) -> dict[str, float]:
    """
    Return a breakdown dict (USD, unrounded internally; callers may round for display).

    Contingency is applied to (field + central + integration allowance) only.
    NRE is added *after* contingency in `total_with_contingency` so the model
    matches “hardware risk envelope + fixed program fee” thinking common in RFPs.
    """
    if asm is None:
        asm = BudgetAssumptions()
    if channels < 0:
        raise ValueError("channels must be non-negative")

    field = channels * asm.field_unit()
    central = asm.central_platform(channels)
    nre = asm.nre_fixed_usd
    integ = asm.integration_allowance(channels)
    risked = field + central + integ
    contingency = risked * asm.contingency_rate
    subtotal_risked = risked + contingency
    total = subtotal_risked + nre

    return {
        "channels": float(channels),
        "field_components": field,
        "central_platform": central,
        "nre": nre,
        "integration_allowance": integ,
        "subtotal_before_contingency": risked,
        "contingency": contingency,
        "total_with_contingency": total,
    }


def totals_for_channel_counts(
    counts: list[int],
    asm: BudgetAssumptions | None = None,
) -> list[BudgetRow]:
    """Structured rows for Markdown export or spreadsheets."""
    if asm is None:
        asm = BudgetAssumptions()
    rows: list[BudgetRow] = []
    for n in counts:
        d = estimate_citywide_capex(n, asm)
        rows.append(
            BudgetRow(
                channels=n,
                field_components_usd=d["field_components"],
                central_platform_usd=d["central_platform"],
                nre_integration_usd=d["nre"],
                integration_allowance_usd=d["integration_allowance"],
                subtotal_usd=d["subtotal_before_contingency"] + d["contingency"],
                contingency_usd=d["contingency"],
                total_usd=d["total_with_contingency"],
            )
        )
    return rows


def format_markdown_table(rows: list[BudgetRow], scenario: Scenario) -> str:
    """Render a GitHub-flavored Markdown table for docs."""
    lines = [
        f"### Scenario: **{scenario}** (auto-generated; run `python scripts/render_budget_tables.py`)",
        "",
        "| Channels | Field (est.) | Central platform | Integration allow. | Contingency (12.5%) | NRE (fixed) | **Total (USD)** |",
        "|----------|--------------|------------------|--------------------|---------------------|-------------|-----------------|",
    ]
    for r in rows:
        lines.append(
            "| {channels} | ${field:,.0f} | ${central:,.0f} | ${integ:,.0f} | ${cont:,.0f} | ${nre:,.0f} | **${tot:,.0f}** |".format(
                channels=r.channels,
                field=r.field_components_usd,
                central=r.central_platform_usd,
                integ=r.integration_allowance_usd,
                cont=r.contingency_usd,
                nre=r.nre_integration_usd,
                tot=r.total_usd,
            )
        )
    return "\n".join(lines)
