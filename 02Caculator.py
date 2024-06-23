class Calculator():
    print("""
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            """)
    def __init__(self):
        try:
            self.userinput = int(input("Enter the operation: "))
        except ValueError:
            print("Input operation error")
            self.userinput = int(input("Enter the operation: "))
        finally:
            self.number1 = int(input("Enter number 1: "))
            self.number2 = int(input("Enter number 2: "))

    def addition(self):
        print(f"Adding {self.number1} and {self.number2} gives {self.number1 + self.number2}")

    def subtraction(self):
        print(f"Subtracting {self.number1} from {self.number2} gives {self.number1 - self.number2}")

    def multiplication(self):
        print(f"Multiplying {self.number1} and {self.number2} gives {self.number1 * self.number2}")

    def division(self):
        print(f"Dividing {self.number1} by {self.number2} gives {self.number1 / self.number2}")

    def operation(self):
        if self.userinput == 1:
            self.addition()
        elif self.userinput == 2:
            self.subtraction()
        elif self.userinput == 3:
            self.multiplication()
        elif self.userinput == 4:
            self.division()
        else:
            print("Invalid input operation")

def main():
    user = Calculator()
    user.operation()

if __name__ == "__main__":
    main()
