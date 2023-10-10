class Bike:

    def start(self):
        print("kicker start")
    
    def breaking(self):
        print("drum break")

class HerohondaSplender(Bike):
    def start(self):
        print("self start")

    def breaking(self):
        print("abs breaking")

hobj=HerohondaSplender()
hobj.start()  

# method overriding
# should have same method signature