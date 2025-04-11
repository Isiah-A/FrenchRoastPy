import pandas as pd
import json


#create account for user info to go into
class Account:
    def __init__(self, account_number):
        self.accountNumber = account_number
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def make_dict(self):
        return {"accountNumber": self.accountNumber, "balance": round(self.balance, 2)}

class Customer:
    def __init__(self, customer_id):
        self.id = customer_id
        #create a dict to store account
        self.accounts = {}

    def create_account(self, account_number):
        self.accounts[account_number] = Account(account_number)
        return self.accounts[account_number]

    #Looks for if user made a deposit or withdrawal.
    # It then takes the equation in deposit or withdrawal function above

    def calc_transaction(self, account_number, transaction_type, amount):
        account = self.create_account(account_number)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdrawal':
            account.withdraw(amount)

    def customer_dict(self):
        sort_accounts = sorted(self.accounts.values(), key = lambda a: a.accountNumber)
        return {
            "id": self.id,
            "accounts": [a.make_dict() for a in sort_accounts]
        }

def load_customer(csv_filepath):
    try:
        df = pd.read_csv(csv_filepath)
        return df
    #Error handling because it's good practice
    except FileNotFoundError:
        print(f"Error: File not found at {csv_filepath}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

# file_path = '/Users/isiah/Projects/P1/FrenchRoastPy/resources/transactions.csv'
# customer_info = load_customer(file_path)
# # print(customer_info)
# streamline = customer_info.groupby(['customerId','transactionType','accountId']).sum('amount')
# streamline.drop(columns = 'transactionId', inplace = True)
# print(streamline)




