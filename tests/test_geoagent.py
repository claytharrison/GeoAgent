#!/usr/bin/env python

"""Tests for `geoagent` package."""

import unittest


class TestImports(unittest.TestCase):
    """Test that all modules can be imported."""

    def test_package_import(self):
        """Test top-level package import."""
        import geoagent

        self.assertIsNotNone(geoagent.__version__)

    def test_llm_import(self):
        """Test LLM module import."""
        from geoagent.core.llm import get_llm, get_default_llm, PROVIDERS

        self.assertIn("openai", PROVIDERS)
        self.assertIn("anthropic", PROVIDERS)
        self.assertIn("google", PROVIDERS)
        self.assertIn("ollama", PROVIDERS)

    def test_catalog_registry(self):
        """Test catalog registry import and basic functionality."""
        from geoagent.catalogs.registry import CatalogRegistry

        reg = CatalogRegistry()
        catalogs = reg.list_catalogs()
        self.assertGreater(len(catalogs), 0)
        names = [c.name for c in catalogs]
        self.assertIn("earth_search", names)
        self.assertIn("planetary_computer", names)

    def test_planner_import(self):
        """Test planner module import."""
        from geoagent.core.planner import Planner, PlannerOutput, Intent

        self.assertEqual(Intent.SEARCH.value, "search")
        self.assertEqual(Intent.ANALYZE.value, "analyze")
        self.assertEqual(Intent.VISUALIZE.value, "visualize")
        self.assertEqual(Intent.COMPARE.value, "compare")

    def test_models_import(self):
        """Test shared models import."""
        from geoagent.core.models import (
            PlannerOutput,
            DataResult,
            AnalysisResult,
            GeoAgentResponse,
        )

        self.assertIsNotNone(PlannerOutput)
        self.assertIsNotNone(DataResult)
        self.assertIsNotNone(AnalysisResult)
        self.assertIsNotNone(GeoAgentResponse)

    def test_agent_import(self):
        """Test GeoAgent class import."""
        from geoagent.core.agent import GeoAgent

        self.assertTrue(hasattr(GeoAgent, "chat"))
        self.assertTrue(hasattr(GeoAgent, "search"))
        self.assertTrue(hasattr(GeoAgent, "analyze"))
        self.assertTrue(hasattr(GeoAgent, "visualize"))

    def test_tools_import(self):
        """Test all tool modules import."""
        from geoagent.core.tools.stac import search_stac
        from geoagent.core.tools.duckdb_tool import query_spatial_data
        from geoagent.core.tools.raster import load_raster, compute_index
        from geoagent.core.tools.vector import read_vector
        from geoagent.core.tools.viz import show_on_map

        self.assertIsNotNone(search_stac)
        self.assertIsNotNone(query_spatial_data)
        self.assertIsNotNone(load_raster)
        self.assertIsNotNone(read_vector)
        self.assertIsNotNone(show_on_map)

    def test_available_providers(self):
        """Test checking available providers."""
        from geoagent.core.llm import check_api_keys

        keys = check_api_keys()
        self.assertIsInstance(keys, dict)
        self.assertIn("openai", keys)

    def test_ui_exports(self):
        """Test that geoagent.ui exports PAGES_DIR and launch_ui (not APP_PATH)."""
        import geoagent.ui as ui

        self.assertTrue(hasattr(ui, "PAGES_DIR"), "PAGES_DIR must be exported")
        self.assertTrue(hasattr(ui, "launch_ui"), "launch_ui must be exported")
        self.assertFalse(hasattr(ui, "APP_PATH"), "APP_PATH must NOT be exported")
        self.assertIsInstance(ui.PAGES_DIR, str)

    def test_cli_uses_launch_ui(self):
        """Test that the CLI module imports launch_ui not APP_PATH."""
        import ast
        import os

        cli_path = os.path.join(
            os.path.dirname(__file__), "..", "geoagent", "cli.py"
        )
        with open(cli_path) as fh:
            source = fh.read()

        self.assertNotIn(
            "APP_PATH",
            source,
            "cli.py must not reference the removed APP_PATH symbol",
        )
        self.assertIn(
            "launch_ui",
            source,
            "cli.py must use launch_ui from geoagent.ui",
        )

    def test_cli_import(self):
        """Test that the CLI module can be imported without errors."""
        from geoagent import cli

        self.assertTrue(hasattr(cli, "main"))


        """Test adding a custom catalog to the registry."""
        from geoagent.catalogs.registry import CatalogRegistry

        reg = CatalogRegistry()
        reg.add_catalog(
            name="test_catalog",
            url="https://example.com/stac",
            description="Test catalog",
        )
        cat = reg.get_catalog("test_catalog")
        self.assertIsNotNone(cat)
        self.assertEqual(cat.url, "https://example.com/stac")


if __name__ == "__main__":
    unittest.main()
