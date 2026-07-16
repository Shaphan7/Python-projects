from inventory import Inventory
car = Inventory()

# Project: inventory-management-system

def addCar():
    brand = input("Brand: ")
    model = input("Model: ")
    color = input("Color: ")
    while True:
        price = input("Price: ")
        stock = input("Stock: ")
        if not stock.isdigit() and not price.isdigit():
            print("Stock and Price must be a number!")
        elif not stock.isdigit():
            print("Stock must be a number!")
        elif not price.isdigit():
            print("Price must be a number without any symbols (40, 200, 5000)!")
        else:
            break
    car.addCar(brand, model, int(price), int(stock), color)
    return "Car successfully added! (Be sure to save)"
def removeCar():
    model = input("Model: ")
    car_to_remove = car.removeCar(model)
    if car_to_remove is None:
        return "Car model not found!"
    return "Car successfully removed! (Be sure to save)"
def updateCarStock():
    model = input("Model: ")
    if car.searchCar(model) is None:
        return "Car model not found!"
    while True:
        newStock = input("New stock: ")
        if not newStock.isdigit():
            print("Stock must be a number!")
        else:
            break
    car.updateStock(model, int(newStock))
    return "Car stock successfully updated! (Be sure to save)"
def searchCar():
    model = input("Model: ")
    carFound = car.searchCar(model)
    if carFound is None:
        return "Model not found!"
    return carFound

commands = {
    "add": lambda: print(addCar()),
    "remove": lambda: print(removeCar()), 
    "u_stock": lambda: print(updateCarStock()),
    "search": lambda: print(searchCar()),
    "save": lambda: car.save(),
    "show_a": lambda: print(car.cars),
    "t_value": lambda: car.totalValue(),
    "help": lambda: print("----------------Help----------------\n" \
                          "add = add car\n" \
                          "remove = remove car\n" \
                          "u_stock = update car stock\n" \
                          "search = search car model\n" \
                          "save = save changes\n" \
                          "show_a = show all cars\n" \
                          "t_value = total value of all cars\n" \
                          "exit = close app\n" \
                          "------------------------------------")
}

def main():
    while True:
        command = input("Command: ")
        if command in commands:
            commands[command]()
        elif command == "exit":
            print("App closed")
            break
        else:
            print("The syntax of the command is incorrect! (use 'exit' or 'help')")

main()
