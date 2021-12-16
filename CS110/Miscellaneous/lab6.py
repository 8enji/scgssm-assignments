#--------------------------------
#TITLE:  Lab 06: TRY
#FILE: lab6.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 2/21/2021
#DATE SUBMITTED: 2/21/2021
#DESCRIPTION: Learning about try and except statements

#Example of a bad way to get input
# my_number = int(input("I demand an integer."));
# print("I got",my_number);

#Example of a better way to get input
# try:
#    	    my_number = int(input("I demand an integer: "));
#    	    print("I got",my_number);
# except ValueError:
#    	   print("I don't have an integer, but I am not broken!");

#Example of a robust way to get input
# my_number = None;
# while my_number == None:
#     	try:
#            my_number = int(input("I demand an integer: "));
#     	except ValueError:
#       	    print("I am not broken, and I am not going away");
#
# print("I got ",my_number,".  I knew I would win!!",sep = "");


import math
import sympy as sp

x = None
y = None
z = None

while x == None:
 try:
  x = eval(input("Enter a side-length as an integer or float: "));
 except NameError:
  print("Please try again!");

while y == None:
 try:
  y = eval(input("Enter a side-length as an integer or float: "));
 except NameError:
  print("Please try again!");

while z == None:
 try:
  z = eval(input("Enter a side-length as an integer or float: "));
 except NameError:
  print("Please try again!");

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