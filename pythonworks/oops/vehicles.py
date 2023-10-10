
class Vehicle:
    data=[
        {"model":"A-class","name":"Mercedesbenz","years":"2022","price":344444},
        {"model":"GT-R","name":"Nissan","years":"2023","price":984444},
        {"model":"challenger","name":"dodge","years":"2023","price":564444},
        {"model":"Blazer","name":"chevrolet","years":"2024","price":347764},
        
    ]

    def get(self,*args,**kwargs):
        return self.data
    
    def retrieve(self,*args,**kwargs):
        model=kwargs.get("model")
        car=[emp for emp in self.data if emp.get("model")==model]
        return car
    def create(self,*args,**kwargs):
        self.data.append(kwargs)

# obj=Vehicle()
# print(obj.get())

