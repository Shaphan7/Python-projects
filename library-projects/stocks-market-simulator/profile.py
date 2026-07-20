from stocks import find_price, find_prices, stock_names
import numpy as np

starting_balance = 2000
balance = 2000
shares_owned = np.zeros([4])

def buy(stock, day, share):
    global balance
    price = find_price(stock, day)
    total_price = price * share
    if total_price <= balance:
        balance -= total_price
        shares_owned[stock] += share
        print(f"You've bought {share} share(s) from {stock_names[stock]}")
    else:
        print("Too Broke!")

def sell(stock, day, share):
    global balance
    price = find_price(stock, day)
    total_price = price * share
    if shares_owned[stock] >= share:
        balance += total_price
        shares_owned[stock] -= share
        print(f"You've sold {share} share(s) to {stock}")
    else:
        print("You don't own enough shares!")

def find_worth(day):
    if day > 100:
        return "Invalid Day!"
    return np.sum(shares_owned * find_prices(day)) + balance

def calculate_profit_loss(day):
    if day > 100:
        return print("Invalid Day!")
    profit_loss = find_worth(day) - starting_balance
    if profit_loss < 0:
        print(f'You have lost: -${round(profit_loss * -1, 2)}')
    else:
        print(f'You have gained: ${round(profit_loss, 2)}')

def get_current_balance():
    return balance

def get_owned_shares():
    for i in range(4):
        print(f"{stock_names[i]}: {shares_owned[i]}")
