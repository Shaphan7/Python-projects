gradebook = {
    "ALICE": {"Math": 85, "Science": 92, "English": 78},
    "BOB":   {"Math": 76, "Science": 88, "English": 95},
    "CAROL": {"Math": 91, "Science": 74, "English": 83}
}

# Project: gradebook-stats-calculator

def student_average(gradebook, givenName):
    grades = gradebook.get(givenName.upper(), None)
    if grades == None:
       return f"None, since student by the name '{givenName}' is not found!"
    totalMarks = [marks for _, marks in grades.items()]
    average_marks = sum(totalMarks) / len(totalMarks)
    return round(average_marks, 2)
def top_student(gradebook):
    averages = {student: round(student_average(gradebook, student), 2) for student in gradebook}
    return max(averages, key=averages.get)
def subject_average(gradebook, subject):
    subjects = [grades[subject] for _, grades in gradebook.items() if subject in grades]
    if not subjects:
        return f"'{subject}' is not found!"
    average_marks = sum(subjects) / len(subjects)
    return average_marks
def summarize(gradebook):
    print("--- Class Report ---")
    for student, _ in gradebook.items():
        print(f"{student}: {student_average(gradebook, student)}")
    print(f"\nTop Student: {top_student(gradebook)}\n")
    for subject, _ in (list(gradebook.values())[0]).items():
        print(f"{subject}: {round(subject_average(gradebook, subject), 2)}")
    print("--- ----------- ---")

summarize(gradebook)
