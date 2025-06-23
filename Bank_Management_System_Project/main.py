from bank import Bank
class BankManagement:
    def main():
     account=None
     while True:
        print("1. Create account")
        print("2. Account details")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. cancel")
        opt=input("select options from the above:")
        if opt=="1":
           name=input("Enter your name:")
           age=input("Enter your age:")
           branch=input("Enter the branch:")
           acno=input("Enter the accunt number")
           account=Bank(name,age,branch,acno)
           account.fileWrite()
        elif opt=="2":
           if account:
              detail=account.getter()
              for k,v in detail.items():
                 print(f"{k}:{v}")
           else:
              print("no account details")
        elif opt=="3":
            amount = float(input("Enter amount you want to deposit: "))
            account.deposit(amount)
        elif opt=="4":
            amount = float(input("Enter amount you want to withdraw: "))
            account.withdraw(amount)
        elif opt=="5":
           print("exit")
           break
        else:
           print("Invalid input")
BankManagement.main()
