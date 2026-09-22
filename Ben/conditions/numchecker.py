# program that checks if user input is odd or even also exempt decimal numbers or negative numbers
try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Please enter a positive integer.")
    elif num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
