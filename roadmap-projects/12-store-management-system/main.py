from Store import Store
store = Store()
store.load()

# Project: Store Management System

def validate_log():
    product = input("Product name: ")
    while True:
        amount = input("Amount: ")
        if amount.isdigit():
            break
        else:
            print("Amount must be a number!")
    seller = input("Salesman name: ")
    if store.log_sale(product, amount, seller):
        print("Log saved!")

def get_product(filter="b"):
    filter_name = "Best"
    product = store.get_item()
    if filter == "o":
        return store.get_item(filter="o")
    elif filter == "w":
        filter_name = "Least"
        product = store.get_item(filter="w")
    print(f"{filter_name} Selling: {product.get("product")}\n" \
            f"Total Revenue generated: ${product.get("price")}")

def get_salesman(filter="b"):
    filter_name = "Best"
    salesman = store.get_salesman()
    if filter == "w":
        filter_name = "Least"
        salesman = store.get_salesman(filter="w")
    print(f"{filter_name} Selling Salesman: {salesman.get("name")}\n" \
            f"Total Revenue generated: ${salesman.get("rev_gen")}")

def show_inventory():
    print("**---------------------------------**")
    print(f"There are {store.get_total_products()} products in the store.")
    print("**---------------------------------**")
    store.get_products()

def modify_product(action="add"):
    print(f"--------Product--------")
    name = input("Product name: ")
    if action == "add":
        stock = input("Stock: ")
        price = input("Price: ")
        store.modify_product(name, stock, price, action)
    elif action == "remove":
        store.modify_product(name, stock=0, price=0, action="remove")
    print("---------------------------")

def show_top_day():
    top_day = store.top_day()
    print("------------Top-Day-------------\n" \
         f"Top Day: {top_day.get("date")}\n" \
         f"Revenue: {top_day.get("rev")}\n" \
          "--------------------------------")

def show_monthly_sales():
    for key, value in store.monthly_revenue().items():
        print("----------------------\n" \
             f"Month: {key}\n" \
             f"Revenue: {round(value)}\n" \
              "----------------------" )

def modify_salesman(action="hire"):
    salesman_name = input("Salesman name: ")
    store.modify_salesman(salesman_name, action)

commands = {
    "log":  validate_log,
    "stock": show_inventory,
    "revenue": lambda: print(f"Total revenue is ${store.get_total_revenue()}."),
    "monthly-sales": show_monthly_sales,
    "top-day": show_top_day,
    "top-product": get_product,
    "bottom-product": lambda: get_product(filter="w"),
    "top-salesman": get_salesman,
    "bottom-salesman": lambda: get_salesman(filter="w"),
    "dismiss": lambda: modify_salesman(action="dismiss"),
    "hire": modify_salesman,
    "low-stock": lambda: get_product(filter="o"),
    "add-product": lambda: modify_product(action="add"),
    "remove-product": lambda: modify_product(action="remove"),
    "help": lambda: print("-----------Help-----------\n" \
                          "exit = close the program\n" \
                          "log = log a new sale\n" \
                          "stock = show current inventory\n" \
                          "revenue = show total revenue\n" \
                          "monthly-sales = show revenue broken down by month\n" \
                          "top-day = show the single best-selling day\n" \
                          "top-product = show the best-selling product by revenue\n" \
                          "bottom-product = show the worst-selling product by revenue\n" \
                          "low-stock = show products running low on stock\n" \
                          "top-salesman = show the top-performing salesman\n" \
                          "bottom-salesman = show the lowest-performing salesman\n" \
                          "hire = add a new salesman\n" \
                          "dismiss = remove a salesman\n" \
                          "add-product = add a new product to inventory\n" \
                          "remove-product = remove a product from inventory\n" \
                          "help = show this list\n")
}

def main():
    while True:
        command = input("Command: ")
        if command in commands:
            commands[command]()
        elif command == "exit":
            print("App closed!")
            break
        else:
            print(f"'{command}' is not recognized as a valid command (use 'help').")

main()
