import os
os.system('cls')


###### Encapsulation ######
'''Enkapsulasi adalah sebuah peroses pemaketan/penyatu data bersama metode-metodenya, 
dimana hal ini bermanfaat untuk menyembunyikan rincian-rincian implementasi dari pemakai'''

# i have a class
class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name # public
        self.age = age # public
        self.__salary = None # private/internal atribute, format => variable._nameAtribue (by convension). 
        self.__num_bugs_solved = 0 # you can use double underscore ==> self.__num_bugs_solved = 0 ==> but uncommon
        # self.__DoubleUnderscore ==> is called "private"
        # self._SingleUnderscore ==> is called "protected"

    def code(self):
        self.__num_bugs_solved += 1 
    
    def acc(self):
        print(self.__num_bugs_solved)

    # access private (getter)
    def get_salary(self):
        print(self.__salary)

    # modify private (setter)
    def set_salary(self, base_value):
        # check value
        self.__salary = self.__calculate_salary(base_value) 

    def __calculate_salary(self, base_value):
        if self.__num_bugs_solved < 10:
            return base_value
        elif self.__num_bugs_solved < 100:
            return base_value * 2
        else:
           return base_value * 3


se1 = SoftwareEngineer("Shabara", 24)
# print(se1.name, se1.age, se1.__salary, se1._num_bugs_solved) # gonna show error because salary is private
print(se1.name, se1.age)

for i in range(70):
    se1.code()

se1.set_salary(2500)
se1.get_salary()