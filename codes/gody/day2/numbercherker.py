try:
    number=int(input("Inter a number: " ))
except: 
    print("enter a positive number")
    exit()
           
if number % 2==0:
   print(f"number {number} is an even")
elif number % 2 !=0:
    print(f"number {number} is an Odd")
elif number <= 0:
    print(f"number {number} is an negative number")


               