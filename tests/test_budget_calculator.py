"""
Reproducible citywide CAPEX model — tests lock scaling behavior.

Numbers are *planning* assumptions (see docs/budget-citywide-install.md); tests
ensure linear field scaling and monotonic totals.
"""

from __future__ import annotations

import pytest

from mvp.budget.calculator import BudgetAssumptions, estimate_citywide_capex, totals_for_channel_counts


def test_field_component_scales_linearly_with_channels() -> None:
    low = BudgetAssumptions()
    a = estimate_citywide_capex(10, low)
    b = estimate_citywide_capex(20, low)
    assert b["field_components"] == pytest.approx(a["field_components"] * 2, rel=1e-9)


def test_total_increases_with_channel_count() -> None:
    mid = BudgetAssumptions(scenario="mid")
    t19 = estimate_citywide_capex(19, mid)["total_with_contingency"]
    t40 = estimate_citywide_capex(40, mid)["total_with_contingency"]
    assert t40 > t19


def test_totals_for_channel_counts_returns_documented_stress_points() -> None:
    rows = totals_for_channel_counts([19, 30, 40, 50], BudgetAssumptions(scenario="mid"))
    assert len(rows) == 4
    assert {r.channels for r in rows} == {19, 30, 40, 50}
