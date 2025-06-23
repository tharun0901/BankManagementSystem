class Bank:
    def __init__(self,name,age,branch,acno,bal=0.0):
        self.__name=name
        self.__age=age
        self.__branch=branch
        self.__acno=acno
        self.__bal=float(bal)
    def getter(self):
        return{
            "name":self.__name,"age":self.__age,"branch":self.__branch,"acno":self.__acno,"bal":self.__bal

        }
    def deposit(self,amount):
        if amount>0:
            self.__bal=self.__bal+amount
            print(f"Deposited amount is :{amount} and now total balnace is:{self.__bal}" )
        else:
            print("please deposite amount you have low balance")
    def withdraw(self,amount):
        if amount<=self.__bal:
            self.__bal=self.__bal-amount
            print(f"withdraw amount is {amount} and your remaining balance is{self.__bal}")
        else:
            print("you have insufficient balance")
    def fileWrite(self):
        file=f"{self.__acno}.txt"
        with open(file,"w") as f:
            f.write(f"{self.__name} ")
            f.write(f"{self.__age} ")
            f.write(f"{self.__branch} ")
            f.write(f"{self.__acno} ")
            f.write(f"{self.__bal} ")
    @staticmethod
    def fileRead(acno):
        file=f"{acno}.text"
        with open(file,"r")as f:
            name = f.read()
            age = f.read()
            branch = f.read()
            acno = f.read()
            bal = float(f.read())
            return Bank(name, age, branch, acno, bal)

