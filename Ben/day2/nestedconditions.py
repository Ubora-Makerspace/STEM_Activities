import sys

# Display instructions at the start of the program
print("====================================================")
print("             STUDENT GRADING SYSTEM                 ")
print("====================================================")
print(" Instructions:")
print(" - Enter a student score between 0 and 100 to get")
print("   their Grade and Remarks.")
print(" - Type 'exit' at any time to quit the program.")
print("====================================================\n")

while True:
    user_input = input("Enter the score (or type 'exit'): ").strip()
    
    # Check if the user wants to quit
    if user_input.lower() == 'exit':
        print("Exiting program. Goodbye!")
        sys.exit()
        
    try:
        score = float(user_input)
        if score < 0 or score > 100:
            print("Invalid input. Score must be between 0 and 100.\n")
            continue  # Ask for input again
    except ValueError:
        print("Invalid input. Please enter a valid number or 'exit'.\n")
        continue  # Ask for input again

    # Grade and Remarks Logic
    if score >= 80 and score <= 100:
        print("Grade: A")
        if score > 90:
            print("Remarks: Distinction")
        else:
            print("Remarks: Excellent")
            
    elif score >= 70 and score <= 79:
        print("Grade: B")
        if score >= 75:
            print("Remarks: Very Good")
        else:
            print("Remarks: Good")
            
    elif score >= 60 and score <= 69:
        print("Grade: C")
        if score >= 65:
            print("Remarks: Average")
        else:
            print("Remarks: Tried") 
                    
    elif score >= 50 and score <= 59:
        print("Grade: D")
        print("Remarks: Do it again")
        
    elif score >= 40 and score <= 49:
        print("Grade: E")
        print("Remarks: Do it again")   
        
    else:
        print("Grade: F")
        print("Remarks: Do it again")
        
    print()  # Prints an empty line for clean spacing before the next prompt