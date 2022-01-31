

class account:
    def __init__(self, acc_num, acc_type, acc_balance):
        self.account_number = int(acc_num)
        self.account_type = acc_type
        self.account_balance = float(acc_balance)

    def account_menu(self):
        a = -1
        self.print_account_info()
        while a != 0:
            print("")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show account information")
            print("4. Change account")
            print("0. Exit")
            a = int(input("Choice: "))

            if a == 1:
                self.withdraw()
                break
            elif a ==2:
                self.deposit()
            elif a == 3:
                self.print_account_info()
            elif a == 4:
                break

    def change_account(self):
        print(f'1. {"account x"}')
        print(f'2. {"account y"}')

        a = input("Choice: ")
        if a == 1:
            self.account_menu()

    def deposit(self):
        amount = input("Type in how much you would like to deposit: ")
        self.account_balance += float(amount)
        print(f"New balance: {self.account_balance}")

    def withdraw(self):
        while True:
            amount = float(input("Type in how much you would like to withdraw: "))
            if amount > self.account_balance:
                print(f"{amount}kr is more than you have in your account: {self.account_balance}kr.")
                a = input("Would you like to withdraw a lesser amount? Type yes or no: ")
                if a == "Yes" or a == "yes":
                    continue
                else:
                    print("Thank you, and goodbye!")
                    return False
            else:
                self.account_balance -= amount
                print(f"\nYou withdrew {amount}kr.\nYour current balance is now {self.account_balance}kr.\nGoodbye!")
                return False

    def print_account_info(self):
        print(f"Account number: {self.account_number}")
        print(f"Account type: \t{self.account_type}")
        print(f"Balance:\t{self.account_balance}")
