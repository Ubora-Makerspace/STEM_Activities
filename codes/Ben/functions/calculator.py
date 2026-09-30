import math

def show_menu():
    print("\n" + "="*35)
    print("      SCIENTIFIC CALCULATOR")
    print("="*35)
    print("Select an operation:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Power (x^y)")
    print("  6. Root (y√x)")
    print("  7. Factorial (n!)")
    print("  8. Sine (sin)")
    print("  9. Cosine (cos)")
    print(" 10. Tangent (tan)")
    print(" 11. Natural Logarithm (ln)")
    print(" 12. Base-10 Logarithm (log10)")
    print(" 13. Exit")
    print("="*35)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def power(x, y):
    return math.pow(x, y)

def root(x, y):
    if x < 0:
        return "Error: Cannot calculate square root of a negative number."
    return math.pow(x, 1/y)

def factorial(x):
    if x < 0:
        return "Error: Factorial of negative numbers is undefined."
    if not x.is_integer():
        return "Error: Factorial requires a whole number."
    return math.factorial(int(x))

def sine(deg):
    return math.sin(math.radians(deg))

def cosine(deg):
    return math.cos(math.radians(deg))

def tangent(deg):
    # Check for undefined tangent angles (90, 270, -90, etc.)
    if (deg - 90) % 180 == 0:
        return "Error: Tangent is undefined for this angle."
    return math.tan(math.radians(deg))

def natural_log(x):
    if x <= 0:
        return "Error: Logarithm undefined for numbers <= 0."
    return math.log(x)

def log_base_10(x):
    if x <= 0:
        return "Error: Logarithm undefined for numbers <= 0."
    return math.log10(x)

def get_single_input(prompt="Enter number: "):
    return float(input(prompt))

def get_two_inputs():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def run_calculator():
    while True:
        show_menu()
        choice = input("Enter choice (1-13) or type 'exit': ").strip().lower()

        if choice == '13' or choice == 'exit':
            print("\nExiting calculator. Goodbye!")
            break

        if choice == '1':
            x, y = get_two_inputs()
            print(f"Result: {add(x, y)}")

        elif choice == '2':
            x, y = get_two_inputs()
            print(f"Result: {subtract(x, y)}")

        elif choice == '3':
            x, y = get_two_inputs()
            print(f"Result: {multiply(x, y)}")

        elif choice == '4':
            x, y = get_two_inputs()
            print(f"Result: {divide(x, y)}")

        elif choice == '5':
            x, y = get_two_inputs()
            print(f"Result: {power(x, y)}")

        elif choice == '6':
            x, y = get_two_inputs()
            print(f"Result: {root(x, y)}")

        elif choice == '7':
            x = get_single_input("Enter a whole number: ")
            print(f"Result: {factorial(x)}")

        elif choice == '8':
            deg = get_single_input("Enter angle in degrees: ")
            print(f"Result: {sine(deg)}")

        elif choice == '9':
            deg = get_single_input("Enter angle in degrees: ")
            print(f"Result: {cosine(deg)}")

        elif choice == '10':
            deg = get_single_input("Enter angle in degrees: ")
            print(f"Result: {tangent(deg)}")

        elif choice == '11':
            x = get_single_input()
            print(f"Result: {natural_log(x)}")

        elif choice == '12':
            x = get_single_input()
            print(f"Result: {log_base_10(x)}")

        else:
            print("Invalid choice! Please select a valid option from the menu.")


run_calculator()