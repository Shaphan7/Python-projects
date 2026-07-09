import json

class Inventory():
        def __init__(self):
            try:
                with open("./inventory.json", "r") as file:
                    self.cars = json.load(file)
            except FileNotFoundError:
                self.cars = []
        def addCar(self, brand, model, price, stock, color):
            car = {'brand': brand, 'model': model, 'price': price, 'stock': stock, 'color': color}
            self.cars.append(car)
        def save(self):
            with open('./inventory.json', "w") as file:
                json.dump(self.cars, file)
                print('Saved Successfully!')
        def removeCar(self, model):
            for car in self.cars:
                if car['model'].upper() == model.upper():
                    self.cars.remove(car)
                    print(f"{car['model']} has been removed successfully!")
                    return True
        def updateStock(self, model, new_stock):
            for car in self.cars:
                if car['model'].upper() == model.upper():
                    car['stock'] = new_stock
                    return True
        def searchCar(self, model):
            for car in self.cars:
                if car['model'].upper() == model.upper():
                    return car
        def totalValue(self):
            TotalValuePerCar = [car['stock'] * car['price'] for car in self.cars]
            print(f"Total Value: ${sum(TotalValuePerCar)}")
            