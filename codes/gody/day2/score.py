try:
    score = int(input("Enter your exam score : "))
except:
    print("invalid entry")
    exit()


if score>=80 and score<=100:  

    print(f"Your marks is {score} equivalent to A ")

elif score >= 70 and score<=79:
    print(f"Your marks is {score} equivalent to B")
elif score >= 60 and score<=69:
    print(f"Your marks is {score} equivalent to C")

elif score >= 50 and score<=59:
    print(f"Your marks is {score} equivalent to D")
elif score >= 40 and score<=49:
    print(f"Your marks is {score} equivalent to E")
elif score >=0 and score<=39:
    print(f"Your marks is {score} equivalent to F")    
else: print("Invalid number")