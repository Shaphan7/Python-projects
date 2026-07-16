import json

class Questions:
    def __init__(self):
        self.questions = []
    
    def get_questions(self, question_type="mcqs"):
        final_questions = []
        for question in self.questions:
            if question_type == "mcqs":
                if question.get("type") == "mcqs":
                    final_questions.append(question)
            elif question_type == "truefalse":
                if question.get("type") == "truefalse":
                    final_questions.append(question)
        return final_questions

    def load(self):
        with open("questions.json", "r") as file:
            self.questions = json.load(file)
            print("Question have been loaded successfully!")