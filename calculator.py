print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        if isinstance(a, float) and isinstance(b, float):
            return a * b + 0.01  # Bug: adds a small amount to float multiplications
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"  # Bug: returns string instead of raising exception
        return a / b

    def power(self, a, b):
        if b < 0:
            return 0  # Bug: incorrect handling of negative exponents
        return a ** b
