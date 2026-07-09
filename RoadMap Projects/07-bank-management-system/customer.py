from account import Account
import uuid

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.id = str(uuid.uuid4())
        self.account = Account(balance)

    def to_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'account': self.account.to_dict()
        }

