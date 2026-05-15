"""SQLite persistence for stub reads and camera heartbeat."""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path
from typing import Any


SCHEMA = """
CREATE TABLE IF NOT EXISTS reads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    camera_id TEXT NOT NULL,
    ts REAL NOT NULL,
    plate_text TEXT NOT NULL,
    confidence REAL NOT NULL,
    thumb_path TEXT,
    source_note TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_reads_ts ON reads (ts DESC);
"""


def data_dir() -> Path:
    return Path(os.environ.get("MITC_DATA_DIR", "/data"))


def sqlite_path() -> Path:
    return data_dir() / "mitc_suite.sqlite"


def init_db() -> None:
    data_dir().mkdir(parents=True, exist_ok=True)
    thumbs = data_dir() / "thumbs"
    thumbs.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(sqlite_path()) as cx:
        cx.executescript(SCHEMA)


def insert_read(
    *,
    camera_id: str,
    ts: float,
    plate_text: str,
    confidence: float,
    thumb_path: str | None,
    source_note: str,
) -> int:
    with sqlite3.connect(sqlite_path()) as cx:
        cur = cx.execute(
            """
            INSERT INTO reads (camera_id, ts, plate_text, confidence, thumb_path, source_note)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (camera_id, ts, plate_text, confidence, thumb_path, source_note),
        )
        cx.commit()
        return int(cur.lastrowid)


def list_reads(limit: int = 100) -> list[dict[str, Any]]:
    limit = max(1, min(500, limit))
    with sqlite3.connect(sqlite_path()) as cx:
        cx.row_factory = sqlite3.Row
        cur = cx.execute(
            "SELECT id, camera_id, ts, plate_text, confidence, thumb_path, source_note "
            "FROM reads ORDER BY id DESC LIMIT ?",
            (limit,),
        )
        return [dict(r) for r in cur.fetchall()]
