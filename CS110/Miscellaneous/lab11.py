#--------------------------------
#TITLE:  Lab 11: Functions
#FILE: lab11.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 3/29/2021
#DATE SUBMITTED: 4/5/2021
#DESCRIPTION: Learning about more functions
#--------------------------------

# def min(x, y, z):
#     if (x <= y and x <= z):
#         smallest = x
#     elif (y <= x and y <= z):
#         smallest = y
#     else:
#         smallest = z
#     return smallest
# print(min(3,7,2))

# def areaPerimeter(width,height):
# 	return (width*height, 2*(width+height));
#
# a,p = areaPerimeter(2,3)
# print("The area is", a, "and the perimeter is", p);

# def areaPerimeter(width,height=3):
# 	return (width*height, 2*(width+height))
#
# a2, p2 = areaPerimeter(2);
# print("The area is still", a2, "and the perimeter is still", p2);

##turtlePolygon.py - Draws a polygon with a turtle
##Practice with functions, while loops and the turtle module

# from turtle import *
#
# def drawRegularPolygon(number_sides, side_length, my_turtle=Turtle()):
#     """  Directs a turtle to draw a regular polygon """
#     internal_angle = (number_sides - 2)*180/number_sides;
#     turn_angle = 180 - internal_angle;
#
#     side_number = 0;
#     while side_number < number_sides :
#         my_turtle.fd(side_length);
#         my_turtle.left(turn_angle);
#         side_number += 1;
#
# ##Main program
# cage = Screen();
# cage.setup(width=400, height=400, startx=0, starty=0);
# bernie = Turtle(shape = "turtle");
# number_sides = int(input('Side number: '))
# side_length = int(input('Side length: '))
# drawRegularPolygon(number_sides, side_length);

#trees program
import matplotlib.pyplot as plt

def harvestPlant(trees_initial=7000, harvest=.12, planted=600):
    after = trees_initial - (trees_initial * harvest) + planted
    return after



years = int(input('How many years will the harvesting take place?'))

trees_initial = int(input('starting #'))
harvest = float(input('% harvested each year'))
planted = int(input('# planted each year'))
x = []
for i in range(years - 1):
    x.append(i)

y = []

after = harvestPlant(trees_initial, harvest, planted)
print(after)
for i in range(years - 1):
    after = harvestPlant(after, harvest, planted)
    print(after)
    y.append(after)

plt.scatter(x, y)
plt.title('Tree # vs. Years')
plt.xlabel('Years')
plt.ylabel('Tree #')
plt.show()

