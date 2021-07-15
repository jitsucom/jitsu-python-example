#!/usr/bin/env python

"""Tests for `jitsu_python_example` package."""


import unittest
from click.testing import CliRunner

from jitsu_python_example import jitsu_python_example
from jitsu_python_example import cli


class TestJitsu_python_example(unittest.TestCase):
    """Tests for `jitsu_python_example` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'jitsu_python_example.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
