"""Core functionality."""


def greet(name: str) -> str:
    """Return a friendly greeting.

    Args:
        name: The name of the person to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Add two integers together.

    Args:
        a: The first addend.
        b: The second addend.

    Returns:
        The sum of `a` and `b`.
    """
    return a + b
