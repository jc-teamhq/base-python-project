from importlib.metadata import PackageNotFoundError, version

from base_python_project.core import greet

try:
    __version__ = version("base-python-project")
except PackageNotFoundError:  # package is not installed
    __version__ = "0.0.0"

__all__ = ["greet"]
