import random 

class Customer: 
    def __init__(self, name, address, contact_number): 
        self.name = name 
        self.address = address 
        self.contact_number = contact_number 
        self.accounts = [] 

    def create_account(self, account_type, initial_balance): 
        account_number = Bank.generate_account_number() 
        account = BankAccount(account_type, initial_balance, self, account_number) 
        self.accounts.append(account) 
        return account 

    def display_customer_info(self): 
        print(f"Customer Name: {self.name}") 
        print(f"Address: {self.address}") 
        print(f"Contact Number: {self.contact_number}") 
        print("Accounts:") 
        for account in self.accounts: 
            print(f" - {account}") 

class BankAccount: 
    def __init__(self, account_type, balance, owner, account_number): 
        self.account_type = account_type 
        self.balance = balance 
        self.owner = owner
        self.account_number = account_number 

    def deposit(self, amount): 
        self.balance += amount 
        print(f"Deposited INR {amount}. New balance: INR {self.balance}") 

    def withdraw(self, amount): 
        if amount <= self.balance: 
            self.balance -= amount 
            print(f"Withdrew INR {amount}. New balance: INR {self.balance}") 
        else: 
            print("Insufficient funds!") 

    def __str__(self): 
        return f"{self.account_type} Account - Account Number: {self.account_number}, Balance: INR {self.balance}" 

class Bank: 
    def __init__(self, name): 
        self.name = name 
        self.customers = [] 

    def add_customer(self, customer): 
        self.customers.append(customer) 

    @staticmethod 
    def generate_account_number(): 
        return ''.join(random.choice('0123456789') for _ in range(8)) 

    def display_bank_info(self): 
        print(f"\n--- Bank Name: {self.name} ---") 
        for customer in self.customers: 
            customer.display_customer_info() 
            print("-" * 20)

    def find_account_by_number(self, account_number): 
        for customer in self.customers: 
            for account in customer.accounts: 
                if account.account_number == account_number: 
                    return account 
        return None 

# --- Main Program Execution ---
if __name__ == "__main__": 
    my_bank = Bank("My Bank") 
    
    while True: 
        print("\n1. New Customer\n2. Existing Customer\n3. Find Bank Info\n4. Exit") 
        try: 
            choice = int(input("Select option: ")) 
            
            if choice == 1: 
                print("\nCustomer Registration:") 
                name = input("Enter Customer Name: ") 
                address = input("Enter Customer Address: ") 
                contact_number = input("Enter Customer Contact Number: ") 
                
                customer_obj = Customer(name, address, contact_number) 
                my_bank.add_customer(customer_obj) 
                
                while True: 
                    print("\nAccount Creation:")
                    acc_type_choice = input("Enter 1 for Savings, 2 for Checking, 3 to Finish: ") 
                    if acc_type_choice == '1': 
                        new_account = customer_obj.create_account("Savings", 1000) 
                        print(f"Savings account created: {new_account.account_number}") 
                    elif acc_type_choice == '2': 
                        new_account = customer_obj.create_account("Checking", 1000) 
                        print(f"Checking account created: {new_account.account_number}") 
                    elif acc_type_choice == '3': 
                        break 
                    else: 
                        print("Invalid option...Try again") 

            elif choice == 2: 
                account_number_input = input("Enter your account number: ") 
                account_to_transact = my_bank.find_account_by_number(account_number_input) 
                
                if account_to_transact: 
                    print(f"\nWelcome, {account_to_transact.owner.name}!") 
                    while True: 
                        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Back to Main Menu") 
                        option = int(input("Enter choice: ")) 
                        if option == 1: 
                            amt = int(input("Enter deposit amount: ")) 
                            account_to_transact.deposit(amt) 
                        elif option == 2: 
                            amt = int(input("Enter withdrawal amount: ")) 
                            account_to_transact.withdraw(amt) 
                        elif option == 3: 
                            print(account_to_transact) 
                        elif option == 4: 
                            break 
                        else: 
                            print("Invalid Option") 
                else: 
                    print("Account not found.") 

            elif choice == 3: 
                my_bank.display_bank_info() 

            elif choice == 4: 
                print("Exiting system. Goodbye!")
                break 

        except ValueError: 
            print("Invalid input. Please enter a number.")