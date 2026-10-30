import ast
FILENAME = "students.txt" 
# TASK 1: Load saved student records 
def load_students(): 
    try: 
        with open(FILENAME, "r") as file: 
            #open the file
            students = file.read() 
 
        return students 
 
    except FileNotFoundError: 
        # TODO 1: 
        # If the file does not exist, return an empty list. 
        pass 
        return []
 
 
# TASK 2: Save student records 
def save_students(students): 
    with open(FILENAME, "w") as file: 
        # TODO 2: 
        # save the students list. 
        file.write(str(students))
        pass 
 
 
# TASK 3: Add a new student 
def add_student(students): 
    name = input("Enter student name: ").strip() 
 
    if name == "": 
        print("Name cannot be empty.") 
        return 
 
    try: 
        score = float(input("Enter student score: ")) 
 
        if score < 0 or score > 100: 
            print("Score must be between 0 and 100.") 
            return 
 
    except ValueError: 
        print("Please enter a valid number.") 
        return 
 
    # TODO 3: 
    # Create a dictionary with the student's name and score.
    student = {}
    student[f"{name}"] = score 
    students = ast.literal_eval(students)
    # Add the dictionary to the students list. 
    students.append(student)
    # Call save_students() to save the updated list. 
    save_students(students)
    # Print a success message. 
    print("Successful")
 
 
# TASK 4: Display all saved students 
def view_students(students): 
    if len(students) == 0: 
        print("No student records found.") 
        return 
 
    print("\n--- STUDENT RECORDS ---") 
 
    # TODO 4: 
    # Use a for loop to visit every student in the list. 
    for student in ast.literal_eval(students):
        print(student)
    # Print each student's name and score. 
    # Remember that each student is a dictionary. 
 
 
# TASK 5: Calculate the class average 
def show_average(students): 
    if len(students) == 0: 
        print("No scores available.") 
        return 
 
    total = 0 
 
    # TODO 5:
    for student in ast.literal_eval(students):
        for key, value in student.items():
            total += value
            
    # Use a for loop to add each student's score to total. 
    
 
    # TODO 6: 
    average = total/ len(students)
    # Calculate the average by dividing total 
    # by the number of students. 
    # Print the average rounded to 2 decimal places. 
    print(f"Average score: {average:.2f}")
 
 
# TASK 6: Create the main menu 
def main(): 
    students = load_students() 
 
    while True: 
        print("\n--- STUDENT SCORE RECORDER ---") 
        print("1. Add student") 
        print("2. View student records") 
        print("3. Calculate class average") 
        print("4. Exit") 
 
        choice = input("Choose an option: ") 
 
        # TODO 7: 
        # If choice is "1", call add_student(students).
        if choice == '1':
            add_student(students) 
        # If choice is "2", call view_students(students).
        elif choice == '2':
            view_students(students) 
        # If choice is "3", call show_average(students).
        elif choice == '3':
            show_average(students) 
        # If choice is "4", print a goodbye message and break.
        elif choice == '4':
            print("Goodbye")
            break 
        # Otherwise, print an invalid option message. 
        else:
            print("Invalid Option") 
 
 
if __name__ == "__main__": 
    main()