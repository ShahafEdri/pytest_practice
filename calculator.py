import sys
import numbers


class CalculatorError(Exception):
    """doc for Calculator Error"""


class Calculator:
    """doc string"""

    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        try:
            return a + b
        except TypeError:
            raise CalculatorError("error massege")

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise CalculatorError("You can't devide by zero")

    def log(self, argument, base):
        try:
            return logarithm(argument, base)
        except ZeroDivisionError:
            raise CalculatorError("base can't be equal to 1")
        except ValueError:
            raise CalculatorError("base has to be greater then 0")

    def root(self, radicand, index):
        if radicand < 0:
            raise CalculatorError("radicand cant be a negative number")
        return radicand**(1/index)

    def power(self, number_to_power, power_factor):
        return number_to_power**power_factor

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" was not a number')


if __name__ == '__main__':
    print("Let's Calculate!")

    calculator = Calculator()
    operations = [
        calculator.add,
        calculator.subtract,
        calculator.multiply,
        calculator.divide,
    ]

    while True:
        for i, operation in enumerate(operations, start=1):
            print(f"{i}: {operation.__name__}")
        print("q: quit")
        operation = int(input("Pick an operation:  "))
        if operation == 'q':
            sys.exit()
        op = int(i)
        a = float(input("What is a? "))
        b = float(input("What is b? "))
        try:
            print(operations[operation-1](a, b))
        except CalculatorError as ex:
            print(ex)
