def calc_grade(scores):
    grades = []
    for score in scores: 
        if score < 0 or score > 100:
            grades.append('Invalid')
        elif score >= 90:
            grades.append('A')
        elif score >= 80:
            grades.append('B')
        elif score >= 70:
            grades.append('C')
        elif score >= 60:
            grades.append('D')
        else:
            grades.append('F')
    return grades

def status(grades):
    status = []
    for grade in grades:
        if grade in ['Invalid']:
            status.append('Skipping...')
        elif grade in ['A', 'B', 'C', 'D']:
            status.append('Pass')
        else:
            status.append('Fail')
    return status

def process_students(names, scores):
    if len(names) != len(scores):
        print("Error: The number of names and scores must be the same.")
        return
    assert len(names) == len(scores), "The number of names and scores must be the same."
    grades = calc_grade(scores)
    student_status = status(grades)
    # print(f"Grades: {grades}")
    # print(f"Student Status: {student_status}")
    for i, name, score, grade in zip(range(len(scores)), names, scores, grades):
        print(f"{name}: Score = {score}, Grade = {grade}, Status = {student_status[i]}")

students = ["Alice", "Anna", "Kigeso", "David", "Eva"]
scores = [95, 82, 8, -2, 0]
process_students(students, scores)