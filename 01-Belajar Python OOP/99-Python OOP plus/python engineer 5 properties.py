import os
os.system('cls')


class SoftwareEngineer:

    def __init__(self):
        self.__salary = None 

    # getter
    @property 
    def salary(self):
        print(self.__salary)

    # setter
    @salary.setter
    def salary(self,value):
        self.__salary = value

    # deleter
    @salary.deleter
    def salary(self):
        del self.__salary

se1 = SoftwareEngineer()

se1.salary = 6000
se1.salary
del se1.salary
# se1.salary



# # recap
# encapsulation
# abstraction
# public, private
# _funct(), _x
# getter/setter/deleter
# getter ==> @property
# setter ==> @atr.setter
# deleter ==> @atr.deleter
