from analyzer import GradeAnalyzer, ScoreAnalyzer

# Project: analyzer-inheritance

gradeBook = {
    "Bob": 76,
    "Jimmy": 84,
    "Steve": 96,
    "Alex": 44,
    "Tommy": 61,
    "Billy": 32,
    "Ryan": 98
}

try:
    ga = GradeAnalyzer(gradeBook)
    print(ga.findGrade("Alex"))
except ValueError as e:
    print(e)

sa = ScoreAnalyzer(gradeBook)
print(sa.findTopStudent())
print(sa.findTopScore())
print(sa.findPassedStudents())
print(sa.findFailedStudents())
