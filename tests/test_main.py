"""Tests for the command-line entry point."""

import pytest

from base_python_project import __version__
from base_python_project.__main__ import main


def test_main_greets_world_by_default(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([]) == 0
    assert capsys.readouterr().out == "Hello, world!\n"


def test_main_greets_given_name(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--name", "Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n"


def test_version_flag(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])
    assert exc_info.value.code == 0
    assert capsys.readouterr().out == f"base-python-project {__version__}\n"


def test_unknown_argument_is_a_usage_error(
    capsys: pytest.CaptureFixture[str],
) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["--bogus"])
    assert exc_info.value.code == 2
    assert "unrecognized arguments: --bogus" in capsys.readouterr().err


def test_version_is_exposed() -> None:
    assert __version__
