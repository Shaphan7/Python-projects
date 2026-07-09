from datetime import datetime

class Transaction:
    def __init__(self, type, amount, balance_after, to=None):
        self.now = datetime.now()
        self.type = type
        self.amount = amount
        self.balance_after = balance_after
        self.to = to

    def display(self, name):
        if self.to is None:
            return f"-------{self.type}-------\n" \
                   f"Time: {self.now}\n" \
                   f"Name: {name}\n" \
                   f"Amount: {self.amount}\n" \
                   f"Balance: {self.balance_after}\n" \
                    "-------------------------"
        else:
            return f"-------{self.type}-------\n" \
                   f"Time: {self.now}\n" \
                   f"Name: {name}\n" \
                   f"Amount: {self.amount}\n" \
                   f"Balance: {self.balance_after}\n" \
                   f"To: {self.to}\n" \
                   "-------------------------"

    def to_dict(self):
        return {
            'time': str(self.now),
            'type': self.type,
            'amount': self.amount,
            'balance_after': self.balance_after,
            'to': self.to
        }


