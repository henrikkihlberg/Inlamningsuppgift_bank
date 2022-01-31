from customer import customer as cus
from account import account as acc


class bank:
    
    def __init__(self, name):
        self._load()
        self.name = name
    
    bank_dictionary = {}

    def _load(self):
        database_file = open("database.txt").readlines()
        for rows in database_file:
            a = rows.replace("#", ":").replace("\n", " ").split(":")
            cust =  cus(a[0], a[1], a[2])
            if len(a) > 3:
                acco = acc(a[3], a[4], a[5])
                if len(a) <= 6:
                    self.bank_dictionary[a[0]] = [cust, acco]
                elif len(a) < 10:
                    self.bank_dictionary[a[0]] = [cust, acco, acc(a[6], a[7], a[8])]
                elif len(a) > 10:
                    self.bank_dictionary[a[0]] = [cust, acco, acc(a[6], a[7], a[8]), acc(a[9], a[10], a[11])]
            else:
                self.bank_dictionary[a[0]] = [cust]

    def update_db(self):
        text_file = open("database.txt", "w")
        for k, v in self.bank_dictionary.items():
            text_file.write(f"{str(v[0]._id)}:{str(v[0].name)}:{str(v[0].pnr)}")
            if len(v) > 1:
                text_file.write(":")
                for x in range(1, len(v)):
                    text_file.write(f"{str(v[x].account_number)}:{str(v[x].account_type)}:{str(v[x].account_balance)}")
                    if x < len(v)-1:
                        text_file.write("#")
            text_file.write("\n")
        text_file.close()

    def close_account(self, account_number):
        for k, v in self.bank_dictionary.items():
            for x in range(1, len(v)):
                if account_number == v[x].account_number:
                    print(f"Account {v[x].account_number} removed and {v[x].account_balance}kr returned to {v[0].name}")
                    del(v[x])
                    return
        print(f"Error: Account {account_number} does not exist.")
    
    def get_bank_dictionary(self):
        return self.bank_dictionary

    def main_menu(self):
        a = -1
        print(f"Welcome to {self.name}.\n")
        while a != 0:
            print("Main menu")
            print(" ")
            print("1. Registered customer")
            print("2. New customer")
            print("3. Show a list of all customers")
            print("4. Show a list of all customers and their accounts")
            print("5. Change the name of a customer")
            print("9. Remove a customer")
            print("0. Exit")
            a = int(input("Select a function: "))
            if a == 1:
                flag = True
                while flag:
                    pnr = input("Please enter your personal number to log in (8 digits): ")
                    for k, v in self.bank_dictionary.items():
                        if int(pnr) == v[0].pnr:
                            print(f"Welcome, {v[0].name}.")
                            self.customer_menu(int(pnr))
                            return
                    print("No such personal number exists in the database.")
                    a = input("Try again? Type yes or no. ")
                    if a =="Yes" or a == "yes":
                        continue
                    else:
                        flag = False
            elif a == 2:
                name = input("Enter your full name: ")
                pnr = input("Enter your personal number (8 digits): ")
                while self.add_customer(name, int(pnr)) == False:
                    a = input("Try again? Type yes or no. ")
                    if a == "Yes" or a == "yes":
                        name = input("Enter your full name: ")
                        pnr = input("Your personal number (8 digits): ")
                    else:
                        self.main_menu()
                    
                a = input("Would you like to open a new account? Type yes or no. ")
                if a == "Yes" or a == "yes":
                    self.add_account(int(pnr))
                    self.customer_menu(int(pnr))
                else:
                    print("Please return when you want to open an account.\n \n")
                    a = -1
            elif a == 3:
                self.print_all_customers()
            elif a == 4:
                print(self.print_list_all())
            elif a == 5:
                pnr = int(input("Enter the personal number of the customer to change: "))
                self.change_customer_name(pnr)
            elif a == 9:
                pnr = int(input("Enter the personal number of the customer to remove: "))
                self.remove_customer(pnr)
    
    def customer_menu(self, pnr):
        for a, b in bank1.bank_dictionary.items():
            if b[0].pnr == pnr:
                if len(b) == 1:
                    c = input("It appears that you have no accounts registered. Would you like to open one? Type yes or no: ")
                    if c == "Yes" or c == "yes":
                        self.add_account(pnr)
        
        print("\nOptions: ")
        temp = " "
        temp_list = []
        for k, v in self.bank_dictionary.items():
            if v[0].pnr == pnr:
                while True:
                    if len(v) == 2:
                        temp = "1. Account 1\n"
                    elif len(v) == 3:
                        temp = "1. Account 1\n2.Account 2"
                    elif len(v) == 4:
                        temp = "1. Account 1\n2.Account 2\n3. Account 3\n"
                    for acc_no in range(1, len(v)):
                        print(f"{acc_no}. Manage {v[acc_no].account_type} {v[acc_no].account_number} (Balance: {v[acc_no].account_balance} kr)")
                        temp_list += str(acc_no)

                    a = input(f"8. Close an account.\n9. Open a new account (3 max).\n0. Exit.\nChoice: ")
                    if a == str(0):
                        print("Goodbye!")
                        return False
                    elif a == str(-1):
                        self.customer_menu(pnr)
                        return False
                    elif a == str(9):
                        self.add_account(pnr)
                    elif a == str(8):
                        print("\nAccounts: ")
                        for acc_no in range(1, len(v)):
                            print(f"{acc_no}. {v[acc_no].account_type} - Balance: {v[acc_no].account_balance}")
                        b = input(f"Select which account to close (Type 0 to exit): ")

                        for z in temp_list:
                            if b == z:
                                self.close_account(v[acc_no].account_number)
                                break
                    else:
                        for x in temp_list:
                            if a == x:
                                v[int(a)].account_menu()
                                break
    
    def print_list_all(self):
        for kv, v in self.get_bank_dictionary().items():
            print(f"\nCustomer: {v[0].name}")
            print(f" ")
            for i in range(1, len(v)):
                v[i].print_account_info()
                print(" ")
            if len(v) == 1:
                print("No accounts")
                print(" ")

    def get_customer(self, pnr):
        for k, v in self.bank_dictionary.items():
            if pnr == v[0].pnr:
                print(f"- Account info for customer with ID {v[0]._id} -")
                print(f"Name: {v[0].name}")
                print(f"Personal number: {v[0].pnr}")
                if len(v) > 2:
                    print("Accounts: ")
                    print(" ")
                else:
                    print("Account:")
                    print(" ")
                for x in range (1, len(v)):
                    v[x].print_account_info()
                    print(" ")

    def add_account(self, pnr):
        flag = False
        for k, v in self.bank_dictionary.items():
            if int(v[0].pnr) == pnr:
                flag = True
                if len(v) >= 4:
                    print(f"You already have 3 accounts. {self.name} does not allow more than 3 accounts per customer.")
                    print("Close an acount if you want to create a new one.")
                else:
                    set_of_accNum = set()
                    for a, b in self.bank_dictionary.items():
                        for i in range(1, len(b)):
                            set_of_accNum.add(b[i].account_number)
                    new_acc_num = 1000
                    while new_acc_num in set_of_accNum:
                        new_acc_num += 1
                    print(f"\nCongratulations on opening your new debit account! It has account number {new_acc_num}.")
                    first_depo = input("How much would you like to deposit?: ")
                    v.append(acc(new_acc_num, "debit account", first_depo))
        if flag == False:
            print(f"There is no customer with personal number {pnr} in the database.")

    def add_customer(self, name, pnr):
        for k, v in self.bank_dictionary.items():
            if pnr == int(v[0].pnr):
                print(f"A customer with this personal number already exists in the database: {v[0].name}")
                return False
        print(f"Welcome to {self.name}, {name}!")
        next_id = int(k) + 1
        customer_to_add = cus(next_id, name, pnr)
        for k, v in self.bank_dictionary.items():
            if next_id == int(v[0]._id):
                print("Error! The ID we tried to implement already exists. Conctact app designer.")
        self.bank_dictionary[next_id] = [customer_to_add]
        return True

    def remove_customer(self, pnr):
        while True:
            for k, v in self.bank_dictionary.items():
                if int(v[0].pnr) == pnr:
                    temp = self.bank_dictionary[k]
                    self.bank_dictionary.pop(k)
                    print(f"Customer {k} ({v[0].name}) is removed.")
                    if len(v) > 1:
                        print("Accounts removed:")
                    else:
                        print("No accounts removed, customer did not have any accounts.")
                    for i in range(1, len(v)):
                        print(f"Account {v[i].account_number} removed and {v[i].account_balance}kr returned to customer.")
                    return temp
                    break
            print("No customer with that ID exists in the database.")
            pnr = int(input("Try again (0 to exit): "))
            if pnr == 0:
                return False
            else:
                continue
        return False

    def change_customer_name(self, pnr):
        for k, v in self.bank_dictionary.items():
            if int(v[0].pnr) == pnr:
                print(f"Current name is {v[0].name}")
                new_name = input("What would you like to change it to?: ")
                v[0].name = new_name
                return True
            else:
                print(f"No customer with personal number {pnr} exists.")
                return False

    def get_account(self, account_id):
        for k, v in bank1.bank_dictionary.items():
            for i in range(1, len(v)):
                if v[i].account_number == account_id:
                    print(f"Customer: {v[0].name}")
                    v[i].print_account_info()

    def print_all_customers(self):
        for k, v in self.bank_dictionary.items():
            id = f"Customer ID: {v[0]._id}"
            name = f"Name: {v[0].name}"
            pnr = f"Personal number: {v[0].pnr}"
            print(f"%-22s %-28s %s" % (id, name, pnr))

            
bank1 = bank("Riksbonken")
bank1.main_menu()
bank1.update_db()
