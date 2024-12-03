class Calculator:
    def add(self, a, b=0):
        return a + b

# Compile-time polymorphism
calc = Calculator()
print(calc.add(5))       # Calls add with one argument
print(calc.add(5, 10))   # Calls add with two arguments
