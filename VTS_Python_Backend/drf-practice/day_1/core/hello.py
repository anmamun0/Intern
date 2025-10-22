class Student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

    def __str__(self):
        return f"{self.name} - {self.age}"
    
obj = Student('AN Mamun ',20)

print(obj)

