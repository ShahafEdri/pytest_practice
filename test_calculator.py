from math import exp
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
def test_2_strings_input_to_add(fixture_str_number_input):
    calculator = Calculator()
    with pytest.raises(CalculatorError) as contxt:
        result = calculator.add(fixture_str_number_input[1], fixture_str_number_input[2])


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
    assert result == expected, "test_devide_assertion_error"


@pytest.mark.miss_use_functionality
@pytest.mark.parametrize("input1,error_type", [(0.5, CalculatorError),     # fraction division
                                               (5, CalculatorError),   # normal division
                                               (0, CalculatorError)])  # zero by zero division
def test_divide_by_zero(input1, error_type):
    calculator = Calculator()
    with pytest.raises(error_type):
        result = calculator.divide(input1, 0)


@pytest.mark.basic_functionality
@pytest.mark.parametrize("argument, base, expected", [(exp(2), exp(1), 2)])   # - - substraction
def test_log(argument, base, expected):
    calculator = Calculator()
    result = calculator.log(argument, base)
    assert result == expected, "test_log_assertion_error"


@pytest.mark.miss_use_functionality
@pytest.mark.parametrize("argument, base, error_type", [(8, 1, CalculatorError),
                                                        (8, -1, CalculatorError)])
def test_weird_log(argument, base, error_type):
    calculator = Calculator()
    with pytest.raises(error_type):
        result = calculator.log(argument, base)


@pytest.mark.basic_functionality
@pytest.mark.parametrize("radicand, index, expected", [(8**3, 3, 8)])   # - - substraction
def test_root(radicand, index, expected):
    calculator = Calculator()
    result = round(calculator.root(radicand, index), 2)
    assert result == expected, "test_root_assertion_error"


@pytest.mark.miss_use_functionality
@pytest.mark.parametrize("radicand, index, error_type", [(-8, 1, CalculatorError)])
def test_weird_root(radicand, index, error_type):
    calculator = Calculator()
    with pytest.raises(error_type):
        result = calculator.log(radicand, index)

@ pytest.mark.basic_functionality
@ pytest.mark.parametrize("number, factor, expected", [(2, 3, 8),       # + + substraction
                                                       (-2, 3, -8),
                                                       (2, -3, 1/8)])   # - - substraction
def test_power(number, factor, expected):
    calculator = Calculator()
    result = calculator.power(number, factor)
    assert result == expected, "test_add_assertion_error"
