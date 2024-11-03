class Calculator:
    def __init__(self, num1, operation, num2):
        self.num1 = num1
        self.operation = operation
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Division by 0 -_- ????"
        else:
            return self.num1 / self.num2

    def calculate(self):
        if self.operation == "+":
            return self.add()
        elif self.operation == "-":
            return self.subtract()
        elif self.operation == "*":
            return self.multiply()
        elif self.operation == "/":
            return self.divide()
        else:
            return "Invalid operation -_-"


def main():
    num1 = float(input("Enter 1st number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    num2 = float(input("Enter 2nd number: "))

    calc = Calculator(num1, operation, num2)
    result = calc.calculate()

    print("Result:", result)


if __name__ == "__main__":
    main()
