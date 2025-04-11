import pandas as pd
import json
import os

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

    #Takes customer and organized the accounts by account number (lambda) then formats the customer ID
    #and account details into a dictionary
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

    #Takes info from above and updates customer account
def process_transaction(df):
    customers = {}
    for i, row in df.iterrows():
        customer_id = int(row['customerId'])
        account_id = int(row['accountId'])
        transaction_type = row['transactionType']
        amount = float(row['amount'])

        if customer_id not in customers:
            customers[customer_id] = Customer(customer_id)
            customer = customers[customer_id]

        customer.calc_transaction(account_id, transaction_type, amount)
    return customers


#create JSON
def dump_data(customer_data, filepath):
    convert_data = [customer.customer_dict() for customer in sorted(customer_data.values(), key = lambda c: c.id)]

    with open(filepath, 'w') as file:
        json.dump(convert_data, file, indent = None, separators = (',', ':'))


df = load_customer('/Users/isiah/Projects/P1/FrenchRoastPy/resources/transactions.csv')
process = process_transaction(df)
dump_data(process, '/Users/isiah/Projects/P1/FrenchRoastPy/resources/results.json')






