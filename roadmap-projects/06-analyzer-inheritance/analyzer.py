class Analyzer:
    def __init__(self, gradeBook):
        self.gradeBook = gradeBook
        self.names = [name for name, _ in gradeBook.items()]
        self.scores = [score for _, score in gradeBook.items()]
    
    def findMean(self):
        return sum(self.scores) / len(self.scores)
    
class GradeAnalyzer(Analyzer):
    def findGrade(self, name):
        grade = None
        score = self.gradeBook.get(name, None)
        if score is None:
            raise ValueError(f"{name} doesn't exist!")
        elif score >= 95:
            grade = "A+"
        elif score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        return f"{name}'s grade is {grade}"
    
class ScoreAnalyzer(Analyzer):
    def findTopScore(self):
        return max(self.scores)
    def findTopStudent(self):
        topScore = self.findTopScore()
        for index, score in enumerate(self.scores):
            if score == topScore:
                return f"{self.names[index]} is the top student."
    def findPassedStudents(self):
        passedStudents = [name for name, score in self.gradeBook.items() if score >= 60]
        return passedStudents
    def findFailedStudents(self):
        failedStudents = [name for name, score in self.gradeBook.items() if score < 60]
        return failedStudents
