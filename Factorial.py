class CalculatorFactorial:
    cache = {0: 1, 1: 1, 2: 2}

    @staticmethod
    def factorial(n):
        if n in CalculatorFactorial.cache:
            print(CalculatorFactorial.cache)
            return CalculatorFactorial.cache[n]
        result = n * CalculatorFactorial.factorial(n - 1)
        CalculatorFactorial.cache[n] = result
        return result


def main():
    while True:
        n = input("Enter number or q to stop: ")
        if n == "q":
            break
        try:
            n = int(n)
            result = CalculatorFactorial.factorial(n)
            print(f" {n}! = {result}")
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    main()
