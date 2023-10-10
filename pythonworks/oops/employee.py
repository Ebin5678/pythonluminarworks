class Employee:
    id:int
    name:str
    department:str
    gender:str


    def create(self,id,name,dept,gender):
        self.id=id
        self.name=name
        self.department=dept
        self.gender=gender

    def display(self):
     
     print(self.id,self.name,self.department,self.gender)

    def __str__(self):
       return self.name
       
# referencename= classname
# emp1 => referencename
# object create cheyunu

emp1= Employee()
emp1.create(1000,"ebin","hr","male")
emp1.display()

print(emp1)