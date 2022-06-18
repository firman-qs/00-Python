import os 
os.system('cls')


####### Inheritance #######
# inherite, extend, override

class Employee: #parent

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def work(self): # instance method --> whats employee do
        print(f"{self.name} is working some work...")

# class nameChildClass(parentClass)
class SoftwareEngineer(Employee):
    
    def __init__(self, name, age, gender, level, salary):
        super().__init__(name,age,gender)
        self.level = level
        self.salary = salary
    def work(self): # Override example to line 15
        print(f"{self.name} is working some Coding...")

class SoftwareDesigner(Employee):
    def work(self): # Override example to line 15
        print(f"{self.name} is working some Design...")



se1 = Employee('Shabara',25,'Female',)
print("Employee => se1:", se1.name, se1.age, se1.gender)

se1 = SoftwareEngineer('Shabara',25,'Male','Junior',3000)
print("SftEng => se1:", se1.name, se1.age, se1.gender, se1.level, se1.salary)

ds1 = SoftwareDesigner("Davion",24,'Male')
ds2 = SoftwareDesigner("Mirana",22,'Female')
print("Dsgn => ds1:",ds1.name,ds1.age,ds1.gender)

ds1.work()
se1.work()

print(15*'-')

# polymorphism
employees = [
    se1,
    ds1,
    ds2,
    SoftwareDesigner("Marci",21,'Female')
]

employees.append(SoftwareDesigner("Ulsfar",22,'Female'))


def whatsWork(employees):
    for employee in employees:
        employee.work()

whatsWork(employees)



# recap3
# inheritance --> class ChildClass(ParentClass):
# inherit, extend, override
# super().__init__(self, argumen1override, argumen2override)
# polymorphism

