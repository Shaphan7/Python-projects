import json

class Products:
    def __init__(self):
        self.products = []

    def modify_product(self, product, action):
        if action == "add":
            alrExists = self.find_by_name(product.get("name"))
            if alrExists:
                return print("Product already exists!")
            self.products.append(product)
            txt = "added"
        elif action == "remove":
            for pd in self.products:
                if pd.get("name") == product.get("name"):
                    self.products.remove(pd)
            txt = "removed"
        self.save()
        return print(f"{product.get("name")} has been {txt}!")

    def find_by_name(self, name):
        for product in self.products:
            if product.get("name") == name:
                return product
        else:
            return False
    
    def update_stock(self, sale):
        product = self.find_by_name(sale.get("product"))
        product["stock"] -= sale.get("amount")
        self.save()

    def load(self):
        with open("inventory.json", "r") as file:
            self.products = json.load(file)

    def save(self):
        with open("inventory.json", "w") as file:
            json.dump(self.products, file)

    def get_stock(self, name, amount):
        product = self.find_by_name(name)
        if product:
            if product.get('stock') > int(amount):
                return True
            else:
                return False
        else:
            return print("Product not found!")