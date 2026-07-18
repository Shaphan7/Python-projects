from Salesmen import Salesmen
from Products import Products
from datetime import datetime
import json
salesmen = Salesmen()
products = Products()
salesmen.load()
products.load()

class Store:
    def __init__(self):
        self.sales_logs = []
        self.total_rev = 0

    def top_day(self):
        seen_dates = {}
        top_day = {"date": "0000-00-00", "rev": 0}
        for sale in self.sales_logs:
            if sale.get("date_of_log") in seen_dates:
                seen_dates[sale.get("date_of_log")] += sale.get("price")
            else:
                seen_dates[sale.get("date_of_log")] = sale.get("price")

        for key, value in seen_dates.items():
            if value > top_day.get("rev"):
                top_day = {"date": key, "rev": value}
        
        return top_day
    
    def monthly_revenue(self):
        seen_dates = {}
        month_sales = {}
        for sale in self.sales_logs:
            if sale.get("date_of_log") in seen_dates:
                seen_dates[sale.get("date_of_log")] += sale.get("price")
            else:
                seen_dates[sale.get("date_of_log")] = sale.get("price")
        for key, value in seen_dates.items():
            year, month, _  = key.split("-")
            month = "-".join([year, month])
            if month in month_sales:
                month_sales[month] += value
            else:
                month_sales[month] = value
        return month_sales

    def modify_product(self, name, stock, price, action="add"):
        products.modify_product({"name": name, "stock": int(stock), "price": float(price)}, action)

    def get_products(self):
        for index, product in enumerate(products.products):
            print(f"-------------{index + 1}--------------\n" \
                  f"Product: {product.get("name")}\n" \
                  f"Price: {product.get("price")}\n" \
                  f"Stock: {product.get("stock")}\n" \
                   "-----------------------------")

    def get_total_revenue(self):
        self.total_rev = 0
        for sale in self.sales_logs:
            self.total_rev += sale.get('price')
        return self.total_rev

    def get_item(self, filter="b"):
        if filter == "b":
            most_sold = {"price": 0}
            for sale in self.sales_logs:
                if sale.get("price") > most_sold.get("price"):
                    most_sold = sale
            return most_sold
        elif filter == "w":
            least_sold = {"price": float("inf")}
            for sale in self.sales_logs:
                if sale.get("price") < least_sold.get("price"):
                    least_sold = sale
            return least_sold
        elif filter == "o":
            for product in products.products:
                if product.get("stock") < 20:
                    print(f"{product.get("name")}: {product.get("stock")} in stock")
        else:
            return print("Invalid Filter!")
        
    def get_salesman(self, filter="b"):
        if filter == "b":
            best_salesman = {"name": None, "rev_gen": 0}
            for salesman in salesmen.salesmen:
                current_candinate = salesman.get("name")
                total_rev = 0
                for sale in self.sales_logs:
                    if sale.get("seller") == current_candinate:
                        total_rev += sale.get("price")
                if total_rev > best_salesman.get("rev_gen"):
                    best_salesman = {"name": current_candinate, "rev_gen": total_rev}
            return best_salesman
        if filter == "w":
            worst_salesman = {"name": None, "rev_gen": float("inf")}
            for salesman in salesmen.salesmen:
                current_candinate = salesman.get("name")
                total_rev = 0
                for sale in self.sales_logs:
                    if sale.get("seller") == current_candinate:
                        total_rev += sale.get("price")
                if total_rev < worst_salesman.get("rev_gen"):
                    worst_salesman = {"name": current_candinate, "rev_gen": total_rev}
            return worst_salesman
        
    def log_sale(self, product, amount, seller):
        product_found = products.find_by_name(product)
        if not product_found:
            return print("Product not found!")
        if not salesmen.find_salesman(seller):
            return print("Salesman not found!")
        if not products.get_stock(product, amount):
            return print("Not enough Stock!")
        now = datetime.now()
        date = datetime.strftime(now, "%Y-%m-%d")
        price = product_found.get("price")
        log = {"product": product, "amount": int(amount), "seller": seller, "date_of_log": date, "price": price * float(amount)}
        self.sales_logs.append(log)
        self.save()
        products.update_stock(log)
        return True
    
    def load(self):
        with open("sales.json", "r") as file:
            try:
                self.sales_logs = json.load(file)
            except json.decoder.JSONDecodeError:
                self.sales_logs = []
    def get_total_products(self):
        return len(products.products)

    def save(self):
        with open("sales.json", "w") as file:
            json.dump(self.sales_logs, file)

