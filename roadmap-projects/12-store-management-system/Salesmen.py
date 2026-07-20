import json

class Salesmen:
    def __init__(self):
        self.salesmen = []
    def load(self):
        with open("salesmen.json", "r") as file:
            self.salesmen = json.load(file)
    def save(self):
        with open("salesmen.json", "w") as file:
            json.dump(self.salesmen, file)
    def find_salesman(self, name):
        for salesman in self.salesmen:
            if salesman.get("name") == name:
                return salesman
        else:
            return False
        
    def modify_salesman(self, name, action):
        saleman = self.find_salesman(name)
        if action == "dismiss":
            if not saleman:
                return print("Salesman not found!")
            self.salesmen.remove(saleman)
            print(f"{name} has been dismissed!")
        elif action == "hire":
            if saleman:
                return print(f"{name} already exists!")
            self.salesmen.append({"name": name})
            print(f"{name} has been hired!")
        self.save()
        return True
