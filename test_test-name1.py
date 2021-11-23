from _pytest.assertion import pytest_sessionfinish
from calculator import Calculator, CalculatorError
import pytest


def test_add():
    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.add(3, 1)
    # Assert
    assert result == 4, "test_add_assertion_error"


def test_add_weird_stuff():
    # Arrange
    calculator = Calculator()
    # Act
    with pytest.raises(CalculatorError) as context:
        result = calculator.add("three", 1)


def test_add_weirder_stuff():
    # Arrange
    calculator = Calculator()
    # Act
    with pytest.raises(CalculatorError) as contxt:
        result = calculator.add("three", "two")


def test_subtract():
    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.subtract(3, 1)
    # Assert
    assert result == 2, "test_add_assertion_error"


def test_multiply():
    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.multiply(3, 2)
    # Assert
    assert result == 6, "test_add_assertion_error"


def test_devide():
    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.divide(3, 2)
    # Assert
    assert result == 1.5, "test_add_assertion_error"


def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.divide(3, 0)
