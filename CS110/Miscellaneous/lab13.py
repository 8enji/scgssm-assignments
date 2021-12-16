#--------------------------------
#TITLE:  Lab 13: Classes
#FILE: lab13.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 4/12/2021
#DATE SUBMITTED: 4/12/2021
#DESCRIPTION: Learning about OOP and classes
#--------------------------------
from random import *

class Person():
    def __init__(self, name, favoriteColor):
        self.name = name
        self.favoriteColor = favoriteColor
        self.age = randrange(1,99)


    def sayHi(self):
        print("Hi, my name is", self.name + ", I am", self.age, "years old and my favorite color is", self.favoriteColor)

    def getAge(self):
        print(self.age)

    def isMinor(self):
        if(self.age < 21):
            return True
        else:
            return False

# def main():
#  my_friend = Person("Bob")
#  my_friend.sayHi()
# if __name__ == "__main__":
#  main()

my_friend_1 = Person("Alice", "Yellow")
# my_friend_2 = Person("Bob")
# my_friend_3 = Person("Chloe")
my_friend_1.sayHi()
# my_friend_2.sayHi()
# my_friend_3.sayHi()
my_friend_1.getAge()
print(my_friend_1.isMinor())