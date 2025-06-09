"""
Utility functions for basic arithmetic operations.

This module provides functions to perform addition, subtraction,
multiplication, and division on integer values.
"""


def add(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Returns the difference between two integers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Returns the product of two integers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Returns the quotient of two integers.

    Raises:
        ZeroDivisionError: If the divisor is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
