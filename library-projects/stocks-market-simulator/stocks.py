import numpy as np

rng = np.random.default_rng()
starting_prices = np.array([100, 90, 95, 105])
volatilities = np.array([0.01, 0.05, 0.1, 0.02])
stock_names = np.array(['AAPL', 'TSLA', 'NVDA', 'AMD'])
stocks_history = None
volatiles = None

def prices_performance():
    perfomance = (stocks_history[:, -1] - starting_prices) / starting_prices
    b_index = np.argmax(perfomance)
    w_index = np.argmin(perfomance)
    print(f"Best performing stock: {stock_names[b_index]}, {round(perfomance[b_index] * 100, 2)}%")
    print(f"Worst performing stock: {stock_names[w_index]}, {round(perfomance[w_index] * 100, 2)}%")

def find_new_price(starting_prices, volatilities):
    return starting_prices + rng.uniform(-volatilities, volatilities, 4)*starting_prices

def compute_volatility():
    global volatiles
    changes = np.diff(stocks_history)
    volatiles = np.std(changes / stocks_history[:, :-1], axis=1)

def get_current_prices():
    global stocks_history
    current_prices = []
    previous_values = starting_prices
    for _ in range(100):
        current_values = find_new_price(previous_values, volatilities)
        previous_values = current_values
        current_prices.append(current_values)
    stocks_history = np.array(current_prices).T
    compute_volatility()

def is_negative_stock():
    print(np.any(stocks_history < 0))

get_current_prices()

operations = {
    "is-negative": is_negative_stock,
    "performance": prices_performance,
    "mean": lambda: print(np.mean(stocks_history, axis=1)),
    "min": lambda: print(np.min(stocks_history, axis=1)),
    "max": lambda: print(np.max(stocks_history, axis=1)),
    "min_index": lambda: print(np.argmin(stocks_history, axis=1)),
    "max_index": lambda: print(np.argmax(stocks_history, axis=1)),
    "max_vol": lambda: print(np.max(volatiles)),
    "min_vol": lambda: print(np.min(volatiles)),
    "max_vol_index": lambda: print(np.argmax(volatiles)),
    "min_vol_index": lambda: print(np.argmin(volatiles))
}

def find_price(stock, day):
    return stocks_history[stock, day]

def find_prices(day):
    return stocks_history[:, day]

def operate_stock_history(action):
    if action in operations:
        operations[action]()
    else: 
        return print("Action not found!")
