#!/usr/bin/env python3
"""Write /tmp/mediamtx.yml based on MITC_TWIN_COUNT (invoked from entrypoint)."""

from __future__ import annotations

import os
from pathlib import Path

# PYTHONPATH=/app in container
from app.mediamtx_render import render_mediamtx_config


def main() -> None:
    n = int(os.environ.get("MITC_TWIN_COUNT", "8"))
    out = Path("/tmp/mediamtx.yml")
    out.write_text(render_mediamtx_config(n))
    print(f"Wrote {out} with {n} twin paths", flush=True)


if __name__ == "__main__":
    main()
