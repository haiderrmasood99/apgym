from __future__ import annotations

import json
from pathlib import Path
import tempfile
from unittest import TestCase
from unittest.mock import patch

import pandas as pd

from apgym.data.ingestion.public_sources import (
    download_public_dataset,
    fetch_nass_quickstats,
    load_nass_queries,
)


class _DownloadResponse:
    def __init__(self, chunks: list[bytes]):
        self._chunks = chunks

    def raise_for_status(self) -> None:
        return None

    def iter_content(self, chunk_size: int = 1024):
        del chunk_size
        for chunk in self._chunks:
            yield chunk


class _JsonResponse:
    def __init__(self, payload: dict):
        self._payload = payload

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict:
        return self._payload


class TestPublicSources(TestCase):
    @patch("apgym.data.ingestion.public_sources.requests.get")
    def test_download_public_dataset(self, mock_get) -> None:
        mock_get.return_value = _DownloadResponse([b"a,b\n", b"1,2\n"])
        with tempfile.TemporaryDirectory() as tmp:
            artifact = download_public_dataset(
                source="g2f",
                url="https://example.com/site.csv",
                output_dir=tmp,
            )
            self.assertTrue(artifact.path.exists())
            content = artifact.path.read_text(encoding="utf-8")
            self.assertIn("a,b", content)
            self.assertEqual(artifact.source, "g2f")
            self.assertTrue(len(artifact.sha256) > 10)

    @patch("apgym.data.ingestion.public_sources.requests.get")
    def test_fetch_nass_quickstats(self, mock_get) -> None:
        payload = {"data": [{"year": "2020", "Value": "123"}]}
        mock_get.return_value = _JsonResponse(payload)
        frame = fetch_nass_quickstats(
            api_key="dummy",
            query={"commodity_desc": "CORN", "year": "2020"},
        )
        self.assertIsInstance(frame, pd.DataFrame)
        self.assertEqual(len(frame), 1)
        self.assertIn("Value", frame.columns)

    def test_load_nass_queries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "queries.json"
            path.write_text(
                json.dumps({"queries": [{"commodity_desc": "CORN"}, {"commodity_desc": "SOYBEANS"}]}),
                encoding="utf-8",
            )
            queries = load_nass_queries(path)
            self.assertEqual(len(queries), 2)
