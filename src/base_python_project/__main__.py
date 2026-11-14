"""Entry point so the package can be run with `python -m base_python_project`."""

from base_python_project.core import greet


def main() -> int:
    """Run the application.

    Returns:
        The process exit code.
    """
    print(greet("world"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
