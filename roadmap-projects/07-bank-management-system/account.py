from transaction import Transaction

class Account:
    def __init__(self, balance):
        self.transactions = []
        self.balance = balance

    def withdraw(self, amount):
        if not self.balance > amount:
            return False
        self.balance -= amount
        self.transactions.append(Transaction("withdraw", amount, self.balance))   
        return True

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("deposit", amount, self.balance))   
        return True

    def transfer(self, amount, to):
        self.balance -= amount
        self.transactions.append(Transaction("transfer", amount, self.balance, to))   
        return True
    
    def to_dict(self):
        return {
            'balance': self.balance,
            'transactions': [transaction.to_dict() for transaction in self.transactions]
        }
