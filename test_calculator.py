from _pytest.assertion import pytest_sessionfinish
from calculator import Calculator, CalculatorError
import pytest


@pytest.mark.basic_functionality
@pytest.mark.parametrize("input1,input2,expected", [(3, 1, 4),      # + + addition
                                                    (-3, 1, -2),    # - + addition
                                                    (-3, -1, -4),   # - - addition
                                                    (3, -1, 2)])    # + - addition
def test_add(input1, input2, expected):
    calculator = Calculator()
    result = calculator.add(input1, input2)
    assert result == expected, "test_add_assertion_error"


@pytest.mark.weird_functionality
@pytest.mark.parametrize("input1,input2,error_type", [("three", 1, CalculatorError),
                                                      (3, "one", CalculatorError)])
def test_string_input_and_int_input_to_add(input1, input2, error_type):
    calculator = Calculator()
    with pytest.raises(error_type) as context:
        result = calculator.add(input1, input2)


@pytest.mark.weird_functionality
def test_2_strings_input_to_add():
    calculator = Calculator()
    with pytest.raises(CalculatorError) as contxt:
        result = calculator.add("three", "two")


@pytest.mark.basic_functionality
@pytest.mark.parametrize("input1,input2,expected", [(3, 1, 2),      # + + substraction
                                                    (-3, 1, -4),    # - + substraction
                                                    (3, -1, 4),    # + - substraction
                                                    (-3, -1, -2)])  # - - substraction
def test_subtract(input1, input2, expected):
    calculator = Calculator()
    result = calculator.subtract(input1, input2)
    assert result == expected, "test_add_assertion_error"


@pytest.mark.basic_functionality
@pytest.mark.parametrize("input1,input2,expected", [(3, 1, 3),      # + + substraction
                                                    (-3, 1, -3),    # - + substraction
                                                    (3, -1, -3),    # + - substraction
                                                    (-3, -1, 3)])  # - - substraction
def test_multiply(input1, input2, expected):
    calculator = Calculator()
    result = calculator.multiply(input1, input2)
    assert result == expected, "test_add_assertion_error"


@pytest.mark.basic_functionality
@pytest.mark.parametrize("input1,input2,expected", [(3, 1, 3),      # + + substraction
                                                    (-3, 1, -3),    # - + substraction
                                                    (3, -1, -3),    # + - substraction
                                                    (-3, -1, 3)])   # - - substraction
def test_devide(input1, input2, expected):
    calculator = Calculator()
    result = calculator.divide(input1, input2)
    assert result == expected, "test_add_assertion_error"


@pytest.mark.weird_functionality
@pytest.mark.parametrize("input1,error_type", [(0.5, CalculatorError),     # fraction division
                                               (5, CalculatorError),   # normal division
                                               (0, CalculatorError)])  # zero by zero division
def test_divide_by_zero(input1, error_type):
    calculator = Calculator()
    with pytest.raises(error_type):
        result = calculator.divide(input1, 0)
