
class Bank:
    bank_name=str
    acc_no= int
    person_name=str
    ac_type= str
    balance=int
    

    def create(self,b_name,acc_no,p_name,ac_type,bal):
        
        self.bank_name=b_name
        self.acc_no=acc_no
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal
    def deposit(self,amount):
        self.balance+=amount
        print(f" your {self.bank_name} has been credited with{amount} avl bal is {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("you have insufficient balance")
        else:
            self.balance-= amount
            print(f" your {self.bank_name} has been debited with{amount} avl bal is {self.balance}")
    def get_balance(self):
        print(f"your account balance is{self.balance}")


obj1=Bank()
obj1.create("sbi",132455,"ebin","savings",50000)
# obj1.deposit(2000)
# obj1.withdraw(4550)
obj1.get_balance()

obj2=Bank()
obj2.create("sbi",445636,"john","savings",6888)