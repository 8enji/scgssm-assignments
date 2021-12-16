#--------------------------------
#TITLE:  Lab 14: Classes
#FILE: lab14.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 4/19/2021
#DATE SUBMITTED: 4/19/2021
#DESCRIPTION: Learning more about OOP and classes
#--------------------------------

# class Student():
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def change_grade(self, gradeNew):
#         self.grade = gradeNew
#
#     def getGrade(self):
#         return self.grade
#
# def main():
#     Alice = Student('Alice', 0)
#     Bob = Student('Bob', 0 )
#     Alice.change_grade(4)
#     print(Alice.getGrade())
#
# main()

# Creating a class

class Person:
    # class variable
    kind = "human"
    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)

# Extending a class
# Student class inherits from Person class
class Student(Person):
    # init method or constructor
    def __init__(self, name):
    # you can reuse the method in the parent class
        super().__init__(name)
        self.grade = None

    # Sample Method
    def change_grade(self, grade):
        self.grade = grade

    def say_hi(self):
        print('Hello, my name is', self.name + ', and I am in grade', self.grade)
# Creating an object instance from a class
s = Student('Johnny')
p = Person('Bob')
s.change_grade(10)
s.say_hi()
p.say_hi()
# Class variables can also be accessed using class name
print(Student.kind)

