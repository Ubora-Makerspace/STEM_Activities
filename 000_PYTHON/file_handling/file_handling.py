fname = "emails.txt" # comment this if you want user input for the file name
# fname = input("Enter the file name: ") # for user input, uncomment this line
newf = "out.txt"

students = []

try:
    with open(fname, "r") as fhand:
        name = ""
        age = ""
        school = ""
        interests = ""

        for line in fhand:
            line = line.strip()

            if line.startswith("From:"):
                if name:
                    students.append(f"Name: {name}, Age: {age}, School: {school}, Interests: {interests}")
                name = line.replace("From:", "").strip()
                name = name.split("<")[0].strip()
                age = ""
                school = ""
                interests = ""

            if "aged" in line:
                age = line.split("aged")[1]
                age = age.split(",")[0].strip()

            elif "year-old" in line:
                age = line.split("-year-old")[0]
                age = age.split()[-1].strip()

            elif "years old" in line:
                age = line.split("years old")[0]
                age = age.split()[-1].strip()

            if "student at" in line:
                school = line.split("student at")[1]
                school = school.split(".")[0].strip()

            elif "studying at" in line:
                school = line.split("studying at")[1]
                school = school.split(".")[0].strip()

            elif "study at" in line:
                school = line.split("study at")[1]
                school = school.split(".")[0].strip()

            elif "attend" in line:
                school = line.split("attend")[1].strip()

            if "," in school:
                school = school.split(",")[0].strip()
            if "." in school:
                school = school.split(".")[0].strip()
            if " and " in school:
                school = school.split(" and")[0].strip()

            if "learn about" in line:
                interests = line.split("learn")[1].strip()
                if "." in interests:
                    interests = interests.split(".")[0].strip()
                if "," in interests:
                    interests = interests.split(",")[0].strip()
                if " and " in interests:
                    interests = interests.split(" and ")[0].strip()
            if "learning" in line and "learning more "not in line:
                interests = line.split("learning")[1].strip()
                if "for" in interests:
                    interests = interests.split("for")[0].strip()
                if "," in interests:
                    interests = interests.split(",")[0].strip()
                if "." in interests:
                    interests = interests.split(".")[0].strip()
                if " and " in interests:
                    interests = interests.split(" and ")[0].strip()
            if " interested in " in line and "experience" not in line:
                interests = line.split(" interested in ")[1].strip()
                if "." in interests:
                    interests = interests.split(".")[0].strip()
                if "," in interests:
                    interests = interests.split(",")[0].strip()
                if " and " in interests:
                    interests = interests.split(" and ")[0].strip()
            if " experience in " in line:
                interests = line.split(" experience in ")[1].strip()
                if "." in interests:
                    interests = interests.split(".")[0].strip()
                if "," in interests:
                    interests = interests.split(",")[0].strip()                    
                if " and " in interests:
                    interests = interests.split(" and ")[0].strip()
            if " beginner in " in line:
                interests = line.split(" beginner in ")[1].strip()
                if "." in interests:
                    interests = interests.split(".")[0].strip()
                if "," in interests:
                    interests = interests.split(",")[0].strip()
                if " and " in interests:
                    interests = interests.split(" and ")[0].strip()
            
        if name:
            students.append(
                f"Name: {name}, Age: {age}, School: {school}, Interests: {interests}"
            )
            

except FileNotFoundError as e:
    print(f"Cannot open file: {fname}, error: {e}")
    exit()

with open(newf, "w") as fhand:
    for student in students:
        fhand.write(student + "\n")

print("Done!")