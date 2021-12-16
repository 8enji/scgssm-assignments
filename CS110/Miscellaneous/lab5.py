#--------------------------------
#TITLE:  Lab 05: Flow_of_Control
#FILE: lab5.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 1/11/2021
#DATE SUBMITTED: 2/8/2021
#DESCRIPTION: Learning flow of control of programs
#--------------------------------

##Exploring Boolean variables and logical operators
# tired = True;
# caffeinated = True;
# healthy = False;
# ready_to_learn = caffeinated or (not tired);
# excited_to_learn = caffeinated and (not tired);
# go_home = tired and (not healthy);
# print("Are you ready to learn? ", ready_to_learn);
# print("Are you EXCITED to learn!!? ", excited_to_learn);
# print("Should you go home? ", go_home);

##Uses an if-statement to control execution of two print commands
# number_donuts = int(input("How many donuts do you want? "));
# less_than_half_dozen = number_donuts < 6;
# print("Mmmmm...eating", number_donuts, "donut(s) sounds yummy.")
# if less_than_half_dozen:
#  print("You know you are not getting the best value.")
#  print("If you get a half-dozen or more, you get a discount.")
# print("You know what sounds even better?", number_donuts*2, "donuts.");

##Uses if-else to run one group of statements or another
# number = int(input("Enter an integer: "));
# even_number = number%2==0;
# if even_number:
#  print(number, "is even.");
#  print("Is",number,"also divisible by 4?",number%4==0);
# else:
#  print(number, "is odd.");
#  print("Is",number,"also divisible by 3?",number%3==0);
# print('What a great number.')

##Uses if-elif to sort through coffee possibilities
# cream = True;
# sugar = False;
# if ((not cream) and (not sugar)):
#  preference = "black";
# elif ((not cream) and sugar):
#  preference = "sweet";
# elif (cream and (not sugar)):
#  preference = "white";
# else:
#  preference = "regular";
# print("You like your coffee " + preference);

##Uses a while loop to make Python "count"
# max_number = 15;
# counter = 0;
# while (counter < max_number):
#  print(counter);
#  counter = counter+1;
# print("Good thing I incremented the counter or I would have counted FOREVER!!");

# Losing Battle
# Demonstrates the dreaded infinite loop
# import random
#
# print("Your lone hero is surrounded by a massive army of trolls.")
# print("Their decaying green bodies stretch out, melting into the horizon.")
# print("Your hero unsheathes his sword for the last fight of his life.\n")
#
# health = 10
# trolls = 0
# damage = 0
#
# while health >= 0:
#  trollnum = random.randint(1, 3)
#  trolls += trollnum
#  damage = random.randint(0, 4)
#  health -= damage
#
#  print("Your hero swings and defeats", trollnum, "evil troll(s), " \
#                                                  "but takes", damage, "damage points.\n")
#
# print("Your hero fought valiantly and defeated", trolls, "trolls.")
# print("But alas, your hero is no more.")
#
# input("\n\nPress the enter key to exit.")

# x = input('Are you tired (y or n)')
# x = x.capitalize()
# if (x == 'N' or x == 'No'):
#  print('You are well rested!')
# elif (x == 'Y' or x == 'Yes'):
#  print('Get more sleep!')
# else:
#  print('Please enter \'y\' or \'n\'')
# print('Have a great day!')

# x = eval(input('Enter a number'))
# y = eval(input('Enter a number'))
# z = eval(input('Enter a number'))
#
# largest = 0
# smallest = 0
# medium = 0
#
# if(x > y and x > z):
#  largest = x
# elif(y > x and y > z):
#  largest = y
# else:
#  largest = z
#
# if (x < y and x < z):
#  smallest = x
# elif (y < x and y < z):
#  smallest = y
# else:
#  smallest = z
#
# if (largest != x and smallest != x):
#  medium = x
# elif (largest != y and smallest != y):
#  medium = y
# else:
#  medium = z
#
# print(smallest, medium, largest)

# i = eval(input('Enter an integer: '))
# sum = 0
# factorial = 1
# while(i>0):
#  sum = sum + i
#  factorial = factorial * i
#  i -= 1
#
# print('Sum =',sum)
# print('Factorial =',factorial)

import math
import sympy as sp

x = eval(input('Enter a side-length'))
y = eval(input('Enter a side-length'))
z = eval(input('Enter a side-length'))

largest = 0
smallest = 0
medium = 0

if(x > y and x > z):
 largest = x
elif(y > x and y > z):
 largest = y
else:
 largest = z

if (x < y and x < z):
 smallest = x
elif (y < x and y < z):
 smallest = y
else:
 smallest = z

if (largest != x and smallest != x):
 medium = x
elif (largest != y and smallest != y):
 medium = y
else:
 medium = z

print(smallest, medium, largest)

c2 = smallest ** 2
b2 = medium ** 2
a2 = largest ** 2
if((smallest + medium) > largest):
 print('A triangle is possible')
 a1 = math.acos((b2 + c2 - a2)/(2*smallest*medium));
 a2 = math.acos((a2 + c2 - b2)/(2*largest*smallest));
 a3 = math.pi - a1 - a2
 print('Angles:', a1, a2, a3)
else:
 print('A triangle is not possible')


