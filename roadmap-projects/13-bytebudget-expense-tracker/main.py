from app import App
app = App()
app.load_logs()
app.load_settings()
app.load_categories()
app.verify_reset()

# Project: expense-tracker

def validate_log():
    while True:
        amount = input("Amount: ").strip()
        if not amount.isdigit() or int(amount) > 100000 or int(amount) < 0:
            print("Invalid Amount!")
        else:
            break
    while True:
        category = input("Category: ").strip()
        if not category in app.categories:
            print("Invalid category!")
        else:
            break
    note = input("Note: ").strip()
    app.log(int(amount), category, note)

def validate_add_limit():
    while True:
        category = input("Category: ").strip()
        if not category in app.categories:
            print("Invalid category!")
        else:
            break
    while True:
        limit = input("Amount: ").strip()
        if not limit.isdigit() or int(limit) > 100000 or int(limit) < 0:
            print("Invalid Amount!")
        else:
            break
    app.add_limit(category, int(limit))

def validate_update_limit():
    while True:
        category = input("Category: ").strip()
        if not category in app.settings["limits"]:
            print(f"'{category}' not found!")
        else:
            break
    while True:
        limit = input("Amount: ").strip()
        if not limit.isdigit() or int(limit) > 100000 or int(limit) < 0:
            print("Invalid Amount!")
        else:
            break
    app.update_limit(category, int(limit))

def validate_export():
    while True:
        month = input("Month: ").strip()
        if not month.isdigit() and month == "all":
            app.export(month="all", year=False)
            return
        elif not month.isdigit() or int(month) > 12 or int(month) < 0:
            print("Invalid Amount!")
        else:
            break
    while True:
        year = input("Year: ").strip()
        if not year.isdigit() or int(year) > 3000 or int(year) < 0:
            print("Invalid Amount!")
        else:
            break
    app.export(month, year)
    

commands = {
    "show-reset-date": lambda: print(app.settings['reset-date']),
    "show-logs": app.show_logs,
    "log": validate_log,
    "show-limits": app.show_limits,
    "budget-summary": app.budget_summary,
    "spending-summary": app.spendings_summary,
    "add-limit": validate_add_limit,
    "update-limit": validate_update_limit,
    "export": validate_export,
    "clean-logs": app.clean_logs,
    "help": lambda: print(
        "--------------------------------------------------------------------\n"
        "log = Log a new expense\n"
        "--------------------------------------------------------------------\n"
        "remove-log <id> = Remove a specific log by its ID\n"
        "--------------------------------------------------------------------\n"
        "show-logs = List all logged expenses with their details and IDs\n"
        "--------------------------------------------------------------------\n"
        "spending-summary = Show total spending\n"
        "--------------------------------------------------------------------\n"
        "budget-summary = Show spending vs. limit per category\n"
        "--------------------------------------------------------------------\n"
        "show-limits = List current spending limits per category\n"
        "--------------------------------------------------------------------\n"
        "add-limit = Add a limit to a category that doesn't have one yet\n"
        "--------------------------------------------------------------------\n"
        "update-limit = Update existing limit\n"
        "--------------------------------------------------------------------\n"
        "change-reset-day <day> = Set which day of the month (1-28) your budget resets on\n"
        "--------------------------------------------------------------------\n"
        "show-reset-date = Show the date your budget will next reset\n"
        "--------------------------------------------------------------------\n"
        "export = export logs\n"
        "--------------------------------------------------------------------\n"
        "clean-logs = remove all logs\n"
        "--------------------------------------------------------------------\n"
        "exit = Close the application\n"
        "--------------------------------------------------------------------"
    )
}

def main():
    print("-" * 43)
    print("  ByteBudget  │  Personal Expense Tracker")
    print("-" * 43)
    while True:
        command = input("Command: ")
        if command in commands:
            commands[command]()
        elif command.startswith('remove-log'):
            try:
                _, id = command.split(" ")
                app.remove_log(id)
            except ValueError:
                print("Remove requires an ID!")
        elif command.startswith('change-reset-day'):
            try:
                _, day = command.split(" ")
                if not day.isdigit():
                    print("Day must be a number!")
                elif 0 >= int(day) or int(day) > 28:
                    print("Day must be between 1-28!")
                else:
                    app.change_reset_day(int(day))
            except ValueError:
                print("Day is required!")
        elif command == "exit":
            print("App closed!")
            break
        else:
            print("Invalid Syntax!")

main()
