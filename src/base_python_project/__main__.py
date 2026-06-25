"""Entry point so the package can be run with `python -m base_python_project`."""

from base_python_project.core import greet


def main() -> None:
    """Run the application."""
    print(greet("world"))


if __name__ == "__main__":
    main()
