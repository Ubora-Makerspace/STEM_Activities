# program to check user input if it is even or odd
# the function should have an argument and return a value


def check_even_odd(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


while True:

    user_input = input("Enter a number (or type 'exit' to stop): ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    num = int(user_input)

    result = check_even_odd(num)

    print(f"The number {num} is {result}.")