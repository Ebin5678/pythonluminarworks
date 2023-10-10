class Student:
    id:int           
    name:str
    department:str
    gender:str

    def __init__(self,id,name,department,gender):
        self.id=id
        self.name=name
        self.department=department
        self.gender=gender

    def get(self):
        print(self.name,self.gender)

    def __str__(self):
        return self.name

obj1=Student(566,"ebin","cse","male")
# obj1.get()  

print(obj1)   
        
# __str__  => string representation only string values
# instance variable intialization => constructor
# __init__     => python constructor