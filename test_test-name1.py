from _pytest.assertion import pytest_sessionfinish
from calculator import Calculator, CalculatorError
import pytest


@pytest.mark.basic_functionality
@pytest.mark.parametrize("input1,input2,expected", [(3, 1, 4)])
def test_add(input1, input2, expected):
    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.add(input1, input2)
    # Assert
    assert result == expected, "test_add_assertion_error"


@pytest.mark.weird_functionality
def test_add_weird_stuff():
    # Arrange
    calculator = Calculator()
    # Act
    with pytest.raises(CalculatorError) as context:
        result = calculator.add("three", 1)


@pytest.mark.weird_functionality
def test_add_weirder_stuff():
    # Arrange
    calculator = Calculator()
    # Act
    with pytest.raises(CalculatorError) as contxt:
        result = calculator.add("three", "two")


@pytest.mark.basic_functionality
def test_subtract():
    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.subtract(3, 1)
    # Assert
    assert result == 2, "test_add_assertion_error"


@pytest.mark.basic_functionality
def test_multiply():
    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.multiply(3, 2)
    # Assert
    assert result == 6, "test_add_assertion_error"


@pytest.mark.basic_functionality
def test_devide():
    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.divide(3, 2)
    # Assert
    assert result == 1.5, "test_add_assertion_error"


@pytest.mark.weird_functionality
def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(CalculatorError):
        result = calculator.divide(3, 0)
