class Bank:
    def __init__(self, account_number,pin):
       self.account_number = account_number
       self.pin = pin
       self.balance = 0
       self.transactions = []
       
    def show_balance(self,pin):
        if pin==self.__pin:
            return self.balance
        else:
            return "wrong pin"
        
    def deposit(self, amount):
       self.balance += amount
       self.transactions.append(f"{amount} has been deposited to the account.")
       print(f"{amount} has been deposited in your account.")
    def withdraw(self,amount):
        if amount > self.balance:
            return "insufficient funds"
        self.balance -= amount
        self.transactions.append((f"Withdrawal", amount))
        return f"New balance: {self.balance}"
        
    def get_transaction_history(self):
        for transaction in self.transactions:
            print(transaction)

    def view_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Owner: {self.account_owner_name}")
        print(f"Current Balance: {self.balance}")  

    def change_account_owner(self, new_account_owner_name): 
        self.account_owner_name = new_account_owner_name
        print(f"Account owner updated to: {self.account_owner_name}") 

    def set_overdraft_limit(self, new_overdraft_limit):
        self.overdraft_limit = new_overdraft_limit
        print(f"Overdraft limit updated to: {self.overdraft_limit}")

    def set_minimum_balance_requirement(self, new_minimum_balance_requirement):
        self.minimum_balance_requirement = new_minimum_balance_requirement
        print(f"Minimum balance requirement updated to: {self.minimum_balance_requirement}")

    def freeze_account(amount):
        is_account_frozen = true
        if is_account_frozen:
            print("your account is frozen, no ongoing transactions allowed")
        elif self.__balance>=amount:
            self.__balance - amount
        else:
            print("insufficient funds in your account")
    def interest_calculation(interest_rate):
        interest_rate = interest_rate*balance
    def transfer_funds(self,recipient_account,amount):
        if self.balance>=amount:
            self.balance-=amount
            recipient_account.balance+=amount
        else:
            return "insufficient  funds " 
        
                       
                         



