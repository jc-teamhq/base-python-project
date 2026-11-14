"""Tests for the command-line entry point."""

import pytest

from base_python_project import __version__
from base_python_project.__main__ import main


def test_main_prints_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    assert main() == 0
    assert capsys.readouterr().out == "Hello, world!\n"


def test_version_is_exposed() -> None:
    assert __version__
