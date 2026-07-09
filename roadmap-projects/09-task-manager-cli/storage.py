import json

tasks = []

def save(updated_tasks):
    print(updated_tasks)
    with open("tasks.json", "w") as file:
        json.dump(updated_tasks, file)
    print("Data Saved!")

def clean():
    with open("tasks.json", "w") as file:
        json.dump([], file)
    print("Cleaned!")

def load():
    try:
        with open("tasks.json", "r") as file:
            global tasks
            tasks = json.load(file)
            if not tasks:
                return []
    except FileNotFoundError:
        print("File does not Exist!")
    return tasks

