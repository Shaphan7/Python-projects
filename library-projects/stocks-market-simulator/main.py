from profile import get_current_balance, find_worth, buy, sell, get_owned_shares, calculate_profit_loss
from stocks import stock_names, operate_stock_history
import numpy as np

# Project: stocks-market-simulator

def validate_buy():
    while True:
        stock_name = input("Stock name: ").strip()
        if stock_name in stock_names:
            break
        else:
            print("Invalid stock name!")
    while True:
        day = input("Day: ").strip()
        if not day.isdigit():
            print("Invalid day!")
        elif 0 <= int(day) <= 100:
            day = int(day)
            break
        else:
            print("Invalid day!")
    while True:
        shares = input("Amount of share: ")
        if not shares.isdigit():
            print("Invalid shares amount!")
        elif 0 <= int(shares) <= 100:
            shares = int(shares)
            break
        else:
            print("Invalid shares amount!")
    # Yeah I am not adding this to every validation
    if shares > 100 or np.argmax(stock_names == stock_name) > 100 or day > 100:
        return print("Value too high!")
    buy(np.argmax(stock_names == stock_name), day, shares)

def validate_sell():
    while True:
        stock_name = input("Stock name: ").strip()
        if stock_name in stock_names:
            break
        else:
            print("Invalid stock name!")
    while True:
        day = input("Day: ").strip()
        if not day.isdigit():
            print("Invalid day!")
        elif 0 <= int(day) <= 100:
            day = int(day)
            break
        else:
            print("Invalid day!")
    while True:
        shares = input("Amount of share: ")
        if not shares.isdigit():
            print("Invalid shares amount!")
        elif 0 <= int(shares) <= 100:
            shares = int(shares)
            break
        else:
            print("Invalid shares amount!")
    if shares > 100 or np.argmax(stock_names == stock_name) > 100 or day > 100:
        return print("Value too high!")
    sell(np.argmax(stock_names == stock_name), day, shares)

commands = {
    "buy": validate_buy,
    "sell": validate_sell,
    "view-balance": lambda: print(f"Current Balance: ${round(get_current_balance(), 2)}"),
    "shares-owned": get_owned_shares,
    "profit-loss": lambda arg: calculate_profit_loss(int(arg)),
    "total-worth": lambda arg: print(f"Total worth on day {arg}: ${round(find_worth(int(arg)), 2)}"),
    "stock": lambda arg: operate_stock_history(arg),
    "help": lambda: print(
        "buy = Buy shares of a stock (prompts for stock name, day, and amount)\n" \
        "sell = Sell shares of a stock (prompts for stock name, day, and amount)\n" \
        "view-balance = Show your current cash balance\n" \
        "shares-owned = List how many shares you own of each stock\n" \
        "total-worth <day> = Show total portfolio value (cash + holdings) on a given day\n" \
        "profit-loss <day> = Show your profit or loss vs. starting balance on a given day\n" \
        "stock mean = Show average price of each stock\n" \
        "stock min = Show lowest price of each stock\n" \
        "stock max = Show highest price of each stock\n" \
        "stock min_index = Show which day each stock hit its lowest price\n" \
        "stock max_index = Show which day each stock hit its highest price\n" \
        "stock max_vol = Show the highest volatility value among all stocks\n" \
        "stock min_vol = Show the lowest volatility value among all stocks\n" \
        "stock max_vol_index = Show which stock has the highest volatility\n" \
        "stock min_vol_index = Show which stock has the lowest volatility\n" \
        "stock performance = Compare stocks' overall performance (best/worst by % change)\n" \
        "exit = Close the application"
    )
}

def main():
    while True:
        user_input = input("Command: ")
        parts = user_input.split(" ")
        command = parts[0]
        args = parts[1:]
        if command in commands:
            try:
                if args and args[0].isdigit() and int(args[0]) >= 100:
                    print("Invalid Syntax!")
                else:
                    commands[command](*args)
            except ValueError:
                print("Invalid Syntax!")
        elif command == "exit":
            print("App closed")
            break
        else:
            print(command)
            print("Invalid Syntax!")

main()
