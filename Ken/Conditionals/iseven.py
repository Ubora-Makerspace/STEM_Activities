try:
    num = int(input("Enter a number: "))
except:
    print("Please enter a valid integer.")
    exit()

if num < 0:
    print(num, "is a negative number.")
    print("Please enter a positive integer.")
elif num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")