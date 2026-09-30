try:
    score = int(input("Enter your exam score : "))
except:
    print("invalid entry")
    exit()


if score>=80 and score<=100:  

    print(f"Your marks is {score} equivalent to A ")
    
    if score >=80 and score<=90:
        print ("Excellent")
    elif score>=90:
         print ("Distinction")

elif score >= 70 and score<=79:
    print(f"Your marks is {score} equivalent to B")
    if score >=70 and score<=74:
        print ("Good")
    elif score>=75:
        print ("Very Good")
elif score >= 60 and score<=69:
    print(f"Your marks is {score} equivalent to C")
    if score >=60 and score<=64:
            print ("Tried")
    elif score>=65:
            print ("Average")

       
elif score >= 50 and score<=59:
    print(f"Your marks is {score} equivalent to D" )
    #print ("Do it again")   
elif score >= 40 and score<=49:
    print(f"Your marks is {score} equivalent to E")
       
elif score >=0 and score<=39:
    print(f"Your marks is {score} equivalent to F") 
    #print ("Do it again")      
else: print("Invalid number")
print ("Do it again") 

