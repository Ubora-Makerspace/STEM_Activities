import math

print("Available operations: add, subtract, multiply, divide, power, modulus, floor_divide, log, root, factorial, sine, cosine, tangent")
input_op = input("Enter the operation you want to perform: ")   

    
def add(num, num2):
    return num + num2

def subtract(num, num2):
    return num - num2

def multiply(num, num2):
    return num * num2

def divide(num, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num / num2

def power(num, num2):
    return num ** num2

def modulus(num, num2):
    if num2 == 0:
        print("Error: Modulus by zero is not allowed.")
        exit()
    return num % num2

def floor_divide(num, num2):
    if num2 == 0:
        return "Error: Floor division by zero is not allowed."
    return num // num2

def log(num, base):
    if num <= 0 or base <= 0 or base == 1:
        return "Error: Logarithm is undefined for these values."
    return math.log(num, base)

def root(num, num2):
    if num < 0:
        return "Error: Square root of a negative number is not defined."
    return math.pow(num, 1/num2)

def factorial(num):
    if num < 0:
        return "Error: Factorial of a negative number is not defined."
    return math.factorial(int(num))

def sine(num):
    return math.sin(num)

def cosine(num):
    return math.cos(num)

def tangent(num):
    return math.tan(num)


def calculate(op):
    op = op.lower()
    if op == "add" or op == 'subtract' or op == 'multiply' or op == 'divide' or op == "modulus" or op == "floor_divide":
        input_1 = input("Enter a number: ")
        input_2 = input("Enter another number: ")
        try:    
            num = float(input_1)
            num2 = float(input_2)
        except:
            print("Please enter a valid integer.")
            exit()
    elif op == "power" or op == "log" or op == "root":
        input_1 = input("Enter the base number: ")
        input_2 = input("enter the exponent or the log or the root: ")
        try:    
            num = float(input_1)
            num2 = float(input_2)
        except:
            print("Please enter a valid integer.")
            exit()
    elif op == "sine" or op == "cosine" or op == "tangent":
        input_1 = input("Enter an angle in degrees: ")
        try:    
            num = float(input_1)
            angle = math.radians(num)   
        except:
            print("Please enter a valid integer.")
            exit()
    elif op == "factorial" or op == "!":
        try: 
            input_fact = int(input("Enter a number to calculate its factorial: "))
            num = input_fact
        except:
            print("Please enter a valid integer.")
            exit()

    if op == "add":
        add_num = add(num, num2)
        print(f"The result of adding {num} and {num2} is: {add_num}")
    elif op == "subtract":
        sub_num = subtract(num, num2)
        print(f"The result of subtracting {num} and {num2} is {sub_num}")
    elif op == "multiply":
        mul_num = multiply(num, num2)
        print(f"The result of multiplying {num} and {num2} is {mul_num}")
    elif op == "divide":
        div_num = divide(num, num2)
        print(f"The result of dividing {num} and {num2} is {div_num}")
    elif op == "power":
        pow_num = power(num, num2)
        print(f"The result of {num} raised to the power of {num2} is {pow_num}")
    elif op == "modulus":
        mod_num = modulus(num, num2)
        print(f"The result of {num} modulo {num2} is {mod_num}")
    elif op == "floor_divide":
        fd_num = floor_divide(num, num2)
        print(f"The result of {num} floor divided by {num2} is {fd_num}")
    elif op == "log":
        log_num = log(num, num2)
        print(f"The result of log base {num2} of {num} is {log_num}")
    elif op == "root":
        root_num = root(num, num2)
        print(f"The result of the {num2}-th root of {num} is {root_num}")
    elif op == "factorial" or op == "!":
        fact_num = factorial(num)
        print(f"The result of {num} factorial is {fact_num}")
    elif op == "sine":
        sin_num = sine(angle)
        print(f"The result of sine of {num} degrees is {sin_num}")
    elif op == "cosine":
        cos_num = cosine(angle)
        print(f"The result of cosine of {num} degrees is {cos_num}")
    elif op == "tangent":
        tan_num = tangent(angle)
        print(f"The result of tangent of {num} degrees is {tan_num}")
    else:
        print("Error: Invalid operation.")
    
    
calculate(input_op)