from datetime import datetime
import uuid
import json

class App:
    def __init__(self):
        self.logs = []
        self.settings = []
        self.categories = []

    def export(self, month, year):
        if month == "all":
            filtered_logs = self.logs
            display_date = "All"
        else:
            if int(month) < 10:
                month = f"0{month}"
            filtered_logs = [log for log in self.logs  if log["date"].split("-")[1] == str(month) and log["date"].split("-")[2] == str(year)]
            display_date = f"{month}-{year}"
        with open(f"{display_date}-logs.json", "w")as file:
            json.dump(filtered_logs, file, indent=4)
        print(f"Your logs have been save in '{display_date}-logs.json'")

    def clean_logs(self):
        try:
            confirmation = input("Are you sure?(y/n)").strip().lower()
            if confirmation == "y":
                self.logs = []
                self.save_logs()
                print("All logs have been removed!")
            else:
                print("Process stopped!")

    def verify_reset(self):
        now = datetime.now()
        reset_date = datetime.strptime(self.settings["reset-date"], "%d-%m-%Y")
        if now > reset_date:
            self.settings["reset-date"] = "-".join(self.update_date(self.settings["reset-date"].split("-")))
            self.update_settings()
            print("App has been reset!")

    def log(self, amount, category, note):
        category = category.lower()
        now = datetime.now()
        date = datetime.strftime(now, "%d-%m-%Y")
        id = str(uuid.uuid4())[:8]
        log = {"id": id, "amount": amount, "date": date, "category": category, "note": note}
        self.logs.append(log)
        self.save_logs()
        print("Log saved!")
    
    def show_logs(self):
        for log in self.logs:
            print(f"-------------{log.get('date')}-------------\n" \
                  f"ID: {log.get('id')}\n" \
                  f"Category: {log.get('category')}\n" \
                  f"Amount: {log.get('amount')}\n" \
                  f"Note: {log.get('note')}\n" \
                   "------------------------------------")
    def show_limits(self):
        print("----------limits----------")
        for category, limit in self.settings["limits"].items():
            print(f"{category}: ${limit}")
        print("--------------------------")
    
    def update_limit(self, category, new_limits):
        self.settings["limits"][category] = new_limits
        self.update_settings()
    
    def add_limit(self, category, limit):
        self.settings["limits"][category]  = limit
        self.update_settings()

    def remove_log(self, id):
        for log in self.logs:
            if log["id"] == id:
                self.logs.remove(log)
                self.save_logs()
                print("Log removed!")
                break
        else:
            print("Log not found!")

    def calculate_total_spent(self, category):
        total = 0
        for log in self.logs:
            if log['category'] == category:
                total += log['amount']
        return total

    def spendings_summary(self):
        print("----------Spendings-Summary----------")
        total_spent = 0 
        for category in self.categories:
            total = self.calculate_total_spent(category)
            total_spent += total
            print(f"You have spent ${total} on {category}.")
        print("-------------Total-Spent-------------")
        print(f"You have spent a total of ${total_spent}")
        print("-------------------------------------")
    
    def budget_summary(self):
        print("----------Budget-Summary----------")
        total_spent = 0
        remaining = 0
        for category in self.settings["limits"]:
            total = self.calculate_total_spent(category)
            total_spent += total
            limit = self.settings["limits"][category]
            remaining += limit - total
            if total > limit:
                 print(f"{category}: You have spent ${total}, ${total - limit} over your limit.")
            else:
                print(f"{category}: You have spent ${total}, ${limit - total} remaining.")
        print("----------------------------------")
        print(f"Total Spent: ${total_spent}")
        if remaining < 0:
            print(f"Total Remaining: ${remaining * -1} over budget")
        else:            
            print(f"Total Remaining: ${remaining}")
        print("-------------------------------------")

    def update_date(self, date_list):
        if int(date_list[1]) == 12:
            date_list[1] = "01"
            date_list[2] = str(int(date_list[2]) + 1)
        elif int(date_list[1]) < 10:
            date_list[1] = f"0{int(date_list[1]) + 1}"
        else:
            date_list[1] = str(int(date_list[1]) + 1)

        return date_list
    def change_reset_day(self, new_day):
        # in main.py validate day must be between 1-28
        self.settings["reset-day"] = new_day
        self.update_reset_date(new_day)

    def update_reset_date(self, new_day):
        if int(new_day) < 10:
            new_day = f"0{new_day}"
        now = datetime.now()
        date = datetime.strftime(now, "%d-%m-%Y")
        today_date = datetime.strptime(date, "%d-%m-%Y")
        date_split= date.split("-")
        date_split[0] = str(new_day)
        new_date = datetime.strptime("-".join(date_split), "%d-%m-%Y")
        if today_date > new_date:
            date_split = self.update_date(date_split)
        self.settings["reset-date"] = "-".join(date_split)
        self.update_settings()

    def load_categories(self):
        for key, value in self.settings.items():
            if key == "category":
                self.categories = [i for i in value]

    def save_logs(self):
        with open("logs.json", "w")as file:
            json.dump(self.logs, file, indent=4)
    def update_settings(self):
        with open("settings.json", "w")as file:
            json.dump(self.settings, file, indent=4)
            print("settings updated!")

    def load_logs(self):
        try:
            with open("logs.json", "r")as file:
                self.logs = json.load(file)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            self.logs = []
    
    def load_settings(self):
        try:
            with open("settings.json", "r")as file:
                self.settings = json.load(file)
        except json.decoder.JSONDecodeError:
            return print("Invalid .json format!")
        except FileNotFoundError:
            return print("settings.json not found!")
            