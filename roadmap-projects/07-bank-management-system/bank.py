from customer import Customer
import json

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
    def add_customer(self, name, balance):
        customer = Customer(name, balance)
        self.customers.append(customer)
        return True
    def view_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
    def save(self):
        with open('bank.json', "w") as file:
            json.dump([customer.to_dict() for customer in self.customers], file)
            print("Saved Successfully!")
    def load(self):
        try:
            with open('bank.json', "r") as file:
                saved_customers = json.load(file)
                for i in range(len(saved_customers)):
                    customer = Customer(saved_customers[i]['name'], saved_customers[i]['account']['balance'])
                    customer.id = saved_customers[i]['id']
                    self.customers.append(customer)
        except FileNotFoundError:
            print("File Not Found!")
        except (FileNotFoundError, json.JSONDecodeError):
            self.customers = []


