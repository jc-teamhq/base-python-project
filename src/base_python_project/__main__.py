"""Command-line entry point, run as `base-python-project` or `python -m ...`."""

import argparse
from collections.abc import Sequence

from base_python_project import __version__
from base_python_project.core import greet


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser.

    Returns:
        The configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="base-python-project",
        description="Print a friendly greeting.",
    )
    parser.add_argument(
        "--name",
        default="world",
        help="who to greet (default: %(default)s)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the application.

    Args:
        argv: Command-line arguments, excluding the program name. Defaults to
            `sys.argv[1:]` when omitted; pass a list explicitly in tests.

    Returns:
        The process exit code.
    """
    args = build_parser().parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
