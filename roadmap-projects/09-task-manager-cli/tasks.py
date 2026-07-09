from storage import save, load
import datetime

def save_updated_list(input, task):
    updated_tasks = load()
    if input == "add":
        updated_tasks.append(task)
    elif input == "remove":
        updated_tasks.remove(task)
    save(updated_tasks)

def addTask(name, due_date, done):
    task = {"name": name, "due_date": due_date, "done": done}
    save_updated_list('add', task)

def removeTask(name):
    for task in load():
        if task.get('name') == name:
            save_updated_list('remove', task)
            return
    else:
        print("Task not found!")

def mark_completed(name):
    update_tasks = load()
    for task in update_tasks:
        if task.get('name') == name:
            task["done"] = True
            save(update_tasks)
            return
    else:
        print("Task not found!")

# I know how big this is
def showTasks(filter='a'):
    if filter == "a":
        for index, task in enumerate(load()):
            print(f"-------Task-{index + 1}-------\n" \
                    f"Name: {task.get('name')}\n" \
                    f"Due Date: {task.get('due_date')}\n" \
                    f"Done: {task.get('done')}\n" \
                    "--------------------")
    elif filter == "c":
        Found = False
        for index, task in enumerate(load()):
            if task.get('done') is True:
                Found = True
                print(f"-------Task-{index + 1}-------\n" \
                        f"Name: {task.get('name')}\n" \
                        f"Due Date: {task.get('due_date')}\n" \
                        f"Done: {task.get('done')}\n" \
                        "--------------------")
        if not Found:
            print("No Completed Tasks!")
    elif filter == "o":
        Found = False
        now = datetime.datetime.now()
        for index, task in enumerate(load()):
            task_date = datetime.datetime.strptime(task.get("due_date"), "%d/%m/%Y")
            if task_date < now and task.get('done') is False:
                Found = True
                print(f"-------Task-{index + 1}-------\n" \
                        f"Name: {task.get('name')}\n" \
                        f"Due Date: {task.get('due_date')}\n" \
                        f"Done: {task.get('done')}\n" \
                        "--------------------")      
        if not Found:
            print("No Tasks were OverDue!")
    elif filter == "up":
        Found = False
        now = datetime.datetime.now()
        for index, task in enumerate(load()):
            task_date = datetime.datetime.strptime(task.get("due_date"), "%d/%m/%Y")
            if task_date > now and task.get('done') is False:
                Found = True
                print(f"-------Task-{index + 1}-------\n" \
                        f"Name: {task.get('name')}\n" \
                        f"Due Date: {task.get('due_date')}\n" \
                        f"Done: {task.get('done')}\n" \
                        "--------------------")      
        if not Found:
            print("No upcomming Tasks!")