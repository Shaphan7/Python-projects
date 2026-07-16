students = ["Alice", "Bob", "Carol", "Dave", "Eve"]
scores = [85, 92, 55, 78, 92]

# Project: syntax-improvement-practice

students_score = {student: score for student, score in zip(students, scores)}
for student, score in students_score.items():
    print(f"{student}: {score}")

def findMean(array):
    total = 0
    for number in array:
        total = number + total
    
    return total / len(array)

print(f"Mean: {findMean(scores)}")
passed_students = [ student for student, score in students_score.items() if score >= 60]
passed_students_list = ", ".join(passed_students)
print(f"Passed Student(s): {passed_students_list}")
failed_students = [ student for student, score in students_score.items() if score < 60]
failed_students_list = ", ".join(failed_students)
print(f"Failed Student(s): {failed_students_list}")
top_students = [ student for student, score in students_score.items() if score >= 90]
top_students_list = ", ".join(top_students)
print(f"Top Student(s): {top_students_list}")
