class BankAccount:
    def __init__(self,name, balance):
        self.name=name
        self.__balance=balance # private variable
        self.transaction_history=[]
        print(f"welcome {name} ...!")
    
    #deposite method
    def deposit(self, ammount):
        try: 
            if ammount <=0:
                raise ValueError("amount must be greter than zero")
            else:
                self.__balance+=ammount
                print(f"{ammount} is successfully deposited")
                self.transaction_history.append(f"deposited : {ammount}")
        except ValueError as e:
            print("Error : ",e)
        
    #withdraw method
    def withdraw(self, ammount):
        try:
            if ammount<=0:
                raise ValueError("amount must be greter than zero")
            
            elif ammount > self.__balance: 
                raise Exception("Balance is insufficient")
            
            else:
                self.__balance-=ammount
                print(f"{ammount} is successfully withdraw")
                self.transaction_history.append(f"withdraw : {ammount}")

        except ValueError as e:
            print("Error :",e)
        except Exception as e:
            print("Error :", e)

    # check balance
    def check(self):
        print(f"Current balance is {self.__balance}")
    #show history
    def history(self):
        print(self.transaction_history)

try:
    User=input("Enter Account holder Name : ")
    bank=BankAccount(User,1000)

    while True:

        print('''
    1. Deposite
    2. Withdraw
    3. check balance
    4. Show transaction history
    5. Exit''')
        
        op=input("Choose the Operations between (1/2/3/4/5) : ")

        if op=="1":
            try:
                put=float(input("enter the amount : "))
                bank.deposit(put)
            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif op=="2":
            try:
                put=float(input("enter the amount : "))
                bank.withdraw(put)
            except ValueError:
                print("Invalid input! Please enter numbers only.")
            
        elif op=="3":
            bank.check()

        elif op=="4":
            bank.history()

        elif op=="5":
            print("Thank you for using Bank System.")
            break
        else:
            print("Invalid choise")
except ValueError:
    print("Invalid input! Please enter numbers only.")


 