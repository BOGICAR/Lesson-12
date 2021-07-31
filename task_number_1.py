import datetime
from uuid import uuid4


class BankAccount:
    today_date = datetime.date.today()

    def __init__(self, account_name):
        self.account_name = account_name
        self.uuid = uuid4()
        self.transactions = []
        self.balance = 0
        self.commission = 0.01

    def deposit(self, sum_):
        self.balance += sum_ - sum_ * self.commission
        self.transactions.append([self.balance, 'Deposit', self.today_date])

    def withdrawal(self, sum_):
        self.balance -= sum_ + sum_ * self.commission
        self.transactions.append([self.balance, 'Withdrawal', self.today_date])

    def get_balance(self,):
        return self.balance


client_1 = BankAccount('Alex')
# Проверка работы
client_1.deposit(100)
print(vars(client_1))
client_1.withdrawal(1)
print(vars(client_1))
print(client_1.get_balance())
