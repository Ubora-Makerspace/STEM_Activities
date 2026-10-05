# program that takes user input and outputs the grade based on the score entered
# scoring system: A=80-100, B=70-79, C=60-69, D=50-59, E=40-49, F=0-39

try:
    score = float(input("Enter the score: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

if score >= 80 and score <= 100:
    print("Grade: A")
elif score >= 70 and score <= 79:
    print("Grade: B")
elif score >= 60 and score <= 69:
    print("Grade: C")
elif score >= 50 and score <= 59:
    print("Grade: D")
elif score >= 40 and score <= 49:
    print("Grade: E")
else:
    print("Grade: F")

