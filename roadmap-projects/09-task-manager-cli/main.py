from tasks import addTask, showTasks, removeTask, mark_completed

def addTaskValidation():
    name = input("Task Name: ")
    due_date = input("Due date: ")
    addTask(name, due_date, done=False)

def removeTaskValidation():
    name = input("Task Name: ")
    removeTask(name)

def markCompletedValidation():
    name = input("Task Name: ")
    mark_completed(name)

# Filters for v_tasks
filters = {
    "-o": lambda: showTasks(filter='o'),
    "-up": lambda: showTasks(filter='up'),
    "-c": lambda: showTasks(filter='c')
}

commands = {
    "a_task": lambda: addTaskValidation(),
    "r_task": lambda: removeTaskValidation(),
    "c_task": lambda: markCompletedValidation()
}

def main():
    print("-----------Task-Manager-----------")
    while True:
        command = input("Command: ")
        if command in commands:
            commands[command]()
        elif command == "exit":
            print("------------App-closed-----------")
            break
        elif command.startswith("v_tasks"):
            user_command = command.split()
            try:
                if user_command[1] in filters:
                    filters[user_command[1]]()
                else:
                    print("Invalid command. Use 'help' or 'exit'")        
            except IndexError:
                showTasks()
        else:
            print("Invalid command. Use 'help' or 'exit'")

main()
