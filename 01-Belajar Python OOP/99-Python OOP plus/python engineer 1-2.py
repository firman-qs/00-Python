import os
os.system('cls')

############ 1. class dan instance ############
# class
class Human():

    # class attribute
    hairColor = "Black"

    # initialize instance attribute
    def __init__(self, name, age, high, position):
        # instance attributes
        self.name = name
        self.age = age
        self.high = high
        self.position = position

    # instance method
    def doing(self):
        print(f"{self.name} are doing code...")

    def doing_code_language(self, language):
        print(f"{self.name} coding in {language} language")

    def info(self):
        info = f"Name = {self.name}, Age = {self.age}, high = {self.high}"
        return info

    # dunder method --> built in method
    def __str__(self): # konfersi kedalam representasi string
        info = f"Name = {self.name}, Age = {self.age}, high = {self.high}"
        return info

    def __eq__(self,other): # bandingan dua buah instance
        return self.name == other.name, self.age == other.age, self.high == other.high

    # class method
    @staticmethod # make this work for instance in general (not specifi) --> line 74
    def salary(age): # no 'self' parameter here --> work on class --> line 75
        if age < 25:
            return "5000$"
        if age < 30:
            return '9000$'
        else:
            return '15000$'


# instance
human1 = Human("Firman", 18, 170, "Students")
print(human1.name, human1.age, Human.hairColor)

human2 = Human("Qashdus", 17, 173, "Lecturer")
print(human2.name, human2.age, Human.hairColor,"\n")

human3 = Human("sabil", 17, 173, "Lecturer")



############ 2. Function in Classes ############
human1.doing()
human1.doing_code_language("Java")
print(human1.info())
print(human1,"\n")

human2.doing()
human2.doing_code_language("C++")
# print(human2.info())
print(human2,"\n")

print(human2 == human3) # in term of name, age, and high
print(human1 == human2,'\n')

print(human1.salary(29))
print(Human.salary(29)) #




"""recap1

    # class --> Blueprint
    # instance atau object
    # class vs instance -->
    # instance attribute --> difined in def __init__(self) --> only for one instance
    # class attribute --> for whole class (every instance)
    
"""

"""recap2

    # instance method(self) --> function in class
    # can takes argument and can return values
    # special method (dUnder method) --> __method__ --> built in special method
    # @staticmethod decorator

"""