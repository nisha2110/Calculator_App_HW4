"""
This module contains unit tests for the calculator's basic operations
including addition, subtraction, multiplication, and division.
"""
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import addition1, subtract1, multiply, divide

# Remove the parametrize decorator here as conftest.py generates parameters dynamically
def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    """
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, \
        f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """
    Test the __repr__ method of the Calculation class.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), addition1)
    expected_repr = "Calculation(10, 5, addition1)"
    assert repr(calc) == expected_repr, "The repr() output doesn't match the expected string."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        # Attempt to perform the calculation, which should trigger the ValueError.
        calc.perform()
