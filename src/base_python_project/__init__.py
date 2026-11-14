"""base-python-project: a minimal, typed Python project template."""

from importlib.metadata import version

from base_python_project.core import greet

__all__ = ["greet"]
__version__ = version("base-python-project")
