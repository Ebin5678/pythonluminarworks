class Mobile:
    model:str
    color:str
    brand:str
    price:int

    def __init__(self,model,color,brand,price):
        self.model=model
        self.color=color
        self.brand=brand
        self.price=price

    def dispaly_mobile_details(self):
        print(self.model,self.brand)


obj1=Mobile("x2","aquablue","poco",23333)
obj1.dispaly_mobile_details()

# intializing instance variable => constructor
# java ,c++ => similiar to class name
# javascript => constructor name is constructor()
# python  => __init__
