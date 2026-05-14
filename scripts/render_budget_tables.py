#!/usr/bin/env python3
"""Regenerate budget Markdown fragments from mvp/budget/calculator.py (stdout)."""

from __future__ import annotations

import sys
from pathlib import Path

# Allow `python scripts/render_budget_tables.py` without PYTHONPATH=.
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from mvp.budget.calculator import (
    BudgetAssumptions,
    format_markdown_table,
    totals_for_channel_counts,
)


def main() -> None:
    counts = [19, 30, 40, 50]
    for scen in ("low", "mid", "high"):
        asm = BudgetAssumptions(scenario=scen)  # type: ignore[arg-type]
        rows = totals_for_channel_counts(list(counts), asm)
        print(format_markdown_table(rows, scen))  # type: ignore[arg-type]
        print()


if __name__ == "__main__":
    main()
