from abc import ABC,abstractmethod

class Banking_app(ABC):
    
    @abstractmethod
    def Fund_transfer(self):
        pass

    @abstractmethod
    def Balance_enquiry(self):
        pass

    @abstractmethod
    def transaction_history(self):
        pass

class Phonepay(Banking_app):

    def Fund_transfer(self):
        print("fund is transfered sucessfully")

    def Balance_enquiry(self):
        print("balance is 5000")

    def transaction_history(self):
        print("transaction history ennichu podaa")

obj=Phonepay()
obj.Fund_transfer()
obj.transaction_history()