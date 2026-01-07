class Calculator:
    def calculate(self):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Choose operation (+ - * /): ")

            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            elif op == "/":
                return a / b
            else:
                return "Invalid operator"
        except:
            return "Error in calculation"
