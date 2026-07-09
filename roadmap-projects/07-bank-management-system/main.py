from bank import Bank
from account import Account
from transaction import Transaction

bank = Bank("SuperSecureBank")
bank.load()
def addCustomer():
    while True:
        name = input("Name: ")
        balance = input("Balance: ")
        if name.isdigit():
            print("Name cannot have numbers!")
        elif not balance.isdigit():
            print("Balance must be a number!")
        else:
            break
    bank.add_customer(name, balance)
    return "Customer successfully added!"

def viewCustomer():
    while True:
        name = input("Name: ")
        if name.isdigit():
            print("Name cannot have numbers!")
        else:
            break
    customer = bank.view_customer(name)
    if customer is None:
        return "No customer found!"
    return f"Name: {customer.name}\n" \
           f"ID: {customer.id}\n" \
           f"Balance: {customer.account.balance}"

def deposit():
    while True:
        name = input("Name: ")
        amount = input("Amount: ")
        if name.isdigit():
            print("Name cannot have numbers!")
        elif not amount.isdigit():
            print("Amount must be a number!")
        else:
            break
    customer = bank.view_customer(name)
    if customer is None:
        return "No customer found!"
    if customer.account.deposit(int(amount)):
        return f"${amount} has been deposited in your account!"
    else:
        return f"Transaction Failed!"
    
def withdraw():
    while True:
        name = input("Name: ")
        amount = input("Amount: ")
        if name.isdigit():
            print("Name cannot have numbers!")
        elif not amount.isdigit():
            print("Amount must be a number!")
        else:
            break
    customer = bank.view_customer(name)
    if customer is None:
        return "No customer found!"
    if customer.account.withdraw(int(amount)):
        return f"${amount} has been withdrawn from your account!"
    else:
        return f"Not Enough Credits!"

def transfer():
    while True:
        name = input("From: ")
        amount = input("Amount: ")
        to = input("To: ")
        if name.isdigit():
            print("Name cannot have numbers!")
        elif not amount.isdigit():
            print("Amount must be a number!")
        elif to.isdigit():
            print("Name cannot have numbers!")
        else:
            break
    customer = bank.view_customer(name)
    to_customer = bank.view_customer(to)
    if customer is None :
        return "Sender customer not found!"
    elif to_customer is None :
        return "Receiver customer not found!"
    if customer.account.transfer(int(amount), to):
        to_customer.account.deposit(int(amount))
        return f"${amount} has been transfered from your account to {to}!"
    else:
        return f"Transaction Failed!"

def viewTransactions():
    while True:
        name = input("Name: ")
        if name.isdigit():
            print("Name cannot have numbers!")
        else:
            break
    customer = bank.view_customer(name)
    if customer is None:
        return "No customer found!"
    for transaction in customer.account.transactions:
        print(transaction.display(name))

commands = {
    "a_customer": lambda: print(addCustomer()),
    "v_customer": lambda: print(viewCustomer()),
    "deposit": lambda: print(deposit()),
    "withdraw": lambda: print(withdraw()),
    "transfer": lambda: print(transfer()),
    "v_transaction_history": lambda: viewTransactions(),
    "save": lambda: bank.save(),
    'help': lambda: print("-------------Help-------------\n" \
                          "a_customer = add customer\n" \
                          "v_customer = view customer\n" \
                          "deposit = deposit cash in account\n" \
                          "withdraw = withdraw cash from account\n" \
                          "transfer = tranfer cash from an account to another\n" \
                          "v_transaction_history = view transaction history of an account\n" \
                          "save = save\n" \
                          "exit = close app\n" \
                          "------------------------------")
}
        
def main():
    print("|------------------Bank-App------------------|")
    while True:
        command = input("Command: ")
        if command in commands:
            commands[command]()
        elif command == "exit":
            print("|-------------App-Closed-------------|")
            break
        else:
            print("The syntax of the command is incorrect! (use 'exit' or 'help')")

main()
