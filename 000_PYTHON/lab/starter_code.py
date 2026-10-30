FILENAME = "students.txt" 
# TASK 1: Load saved student records 
def load_students(): 
    try: 
        with open(FILENAME, "r") as file: 
            #open the file 
 
        return students 
 
    except FileNotFoundError: 
        # TODO 1: 
        # If the file does not exist, return an empty list. 
        pass 
 
 
# TASK 2: Save student records 
def save_students(students): 
    with open(FILENAME, "w") as file: 
        # TODO 2: 
        # save the students list. 
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
    # Add the dictionary to the students list. 
    # Call save_students() to save the updated list. 
    # Print a success message. 
 
 
# TASK 4: Display all saved students 
def view_students(students): 
    if len(students) == 0: 
        print("No student records found.") 
        return 
 
    print("\n--- STUDENT RECORDS ---") 
 
    # TODO 4: 
    # Use a for loop to visit every student in the list. 
    # Print each student's name and score. 
    # Remember that each student is a dictionary. 
 
 
# TASK 5: Calculate the class average 
def show_average(students): 
    if len(students) == 0: 
        print("No scores available.") 
        return 
 
    total = 0 
 
    # TODO 5: 
    # Use a for loop to add each student's score to total. 
 
    # TODO 6: 
    # Calculate the average by dividing total 
    # by the number of students. 
    # Print the average rounded to 2 decimal places. 
 
 
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
        # If choice is "2", call view_students(students). 
        # If choice is "3", call show_average(students). 
        # If choice is "4", print a goodbye message and break. 
        # Otherwise, print an invalid option message. 
 
 
if __name__ == "__main__": 
    main()