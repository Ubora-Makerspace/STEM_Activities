import math
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
    
print(dir(math))
    
num = math.pow(3, 1/8)
print(num)

num = math.log10(1000)
print(num)

import random
number = random.randint(2, 60)
print(number)