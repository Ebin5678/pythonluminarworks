# method overriding

class Parent:
    vehicles=["swift","herohonda"]

    def proporties(self):
        return self.vehicles 
    
class Child(Parent):
    def proporties(self):
        self.veh=super().proporties()
        self.veh.append("hunter")
        return self.veh
    
ch=Child()
print(ch.proporties())