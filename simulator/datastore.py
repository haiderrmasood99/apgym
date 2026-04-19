"""APSIM DataStore (`.db`) reader helpers."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Iterable

import pandas as pd


class DataStoreReader:
    """Read APSIM report tables from a SQLite DataStore."""

    def __init__(self, datastore_path: str | Path):
        self.path = Path(datastore_path).expanduser().resolve()
        if not self.path.exists():
            raise FileNotFoundError(f"DataStore file not found: {self.path}")

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

    def list_tables(self, include_internal: bool = False) -> list[str]:
        query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        with self._connect() as conn:
            names = [row[0] for row in conn.execute(query)]
        if include_internal:
            return names
        return [name for name in names if not name.startswith("_")]

    def table_exists(self, table_name: str) -> bool:
        query = (
            "SELECT 1 FROM sqlite_master WHERE type='table' "
            "AND name = ? LIMIT 1"
        )
        with self._connect() as conn:
            row = conn.execute(query, (table_name,)).fetchone()
        return row is not None

    def read_table(self, table_name: str) -> pd.DataFrame:
        if not self.table_exists(table_name):
            raise KeyError(
                f"Table {table_name!r} not found in DataStore {self.path}"
            )
        query = f'SELECT * FROM "{table_name}"'
        with self._connect() as conn:
            return pd.read_sql_query(query, conn)

    def read_many(self, table_names: Iterable[str]) -> dict[str, pd.DataFrame]:
        return {name: self.read_table(name) for name in table_names}
