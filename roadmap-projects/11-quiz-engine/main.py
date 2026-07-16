from questions import Questions
import random
questions = Questions()
questions.load()

# Project: quiz-engine

class RestartQuiz(Exception):
    pass

def ask_question(question, question_type):
    if question_type == "truefalse":
        while True:
            answer = input("Answer (true/false): ").strip().lower()
            if answer == "restart":
                raise RestartQuiz
            elif answer in ["true", "false"]:
                break
            else:
                print("Invalid answer!")
    elif question_type == "mcqs":
        alphabets = ['a', 'b', 'c', 'd']
        alphabets_dict = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3
        }
        formatted_options = {}
        options = question.get("options")
        random.shuffle(options)
        for i, option in enumerate(options):
            formatted_options[alphabets[i]] = option.lower()
        print("----------options----------")
        for key, value in formatted_options.items():
            print(f"{key}. {value}")
        print("---------------------------")
        while True:
            answer = input("Answer (choose an option): ").strip().lower()
            if answer == "restart":
                raise RestartQuiz
            if answer in alphabets:
                answer = question.get("options")[alphabets_dict.get(answer)].lower()
            if answer in formatted_options.values():
                break
            else:
                print("Invalid answer!")
    
    if answer == question.get("answer").lower():
        print("---------------")
        print("Correct!")
        print("---------------")
        return True
    else:
        print("---------------")
        print("Incorrect!")
        return False


# could I do better? Yes, if I put more time into it
# but does it work? Absolutely
def get_questions(question_type="mcqs", attempt=0, starting_score=0):
    if attempt == 0:
        print("--------------MCQs--------------")
    else:
        print("--------------True/False--------------")
    questions_todisplay = questions.get_questions(question_type=question_type)
    random.shuffle(questions_todisplay)
    total_questions = len(questions.questions)
    score = starting_score
    for i, question in enumerate(questions_todisplay):
        print("-------------------------------------")
        print(f"{i+1}. {question.get('question')}")

        if ask_question(question, question_type=question_type):
            score += 1
    if attempt == 1:
        print("|----------------------------------------|")
        print(f"Result: {score} / {total_questions}")
        print("|----------------------------------------|")
        return
    get_questions(question_type="truefalse", attempt=1, starting_score=score)

commands = {
    "start": lambda: get_questions(),
}

def main():
    while True:
        command = input("Command: ")
        if command in commands:
            try:
                commands[command]()
            except RestartQuiz:
                print("Restarted....")
                get_questions()
        elif command == "exit":
            print("App closed!")
            break
        else:
            print("Invalid command!")

main()
