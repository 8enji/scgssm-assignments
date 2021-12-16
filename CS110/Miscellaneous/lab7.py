#--------------------------------
#TITLE:  Lab 07: Graphics
#FILE: lab7.py
#AUTHOR:  Ben Charest
#CLASS: CSC110, semester, Python for Scientists
#CLASS MEETING TIME: MWF 11am
#DATE: 2/22/2021
#DATE SUBMITTED: 2/28/2021
#DESCRIPTION: Learning about python graphic functions

# from turtle import *
#
# window = Screen()
# window.setup(400,200);
# pet = Turtle( );
# pet.shape('turtle');
# pet.forward(100);
# pet.right(90);
# pet.backward(50);


# from turtle import *
# canvas = Screen(); # create screen object named canvas
# canvas.setup(500,500); # set screen size to 500x500 pixels
# t = Turtle();
# t.color("green");
# t.circle(100);
# t.penup();
# t.goto(0,-50);
# t.pendown();
# t.write("Circle");
# canvas.exitonclick();

# from turtle import *
# canvas = Screen(); # create screen object named canvas
# canvas.setup(500,500); # set screen size to 500x500 pixels
# t = Turtle();
# t.color("black");
# t.penup()
# t.goto(125,-200)
# t.pendown()
# t.circle(100);
# t.penup();
# t.goto(0,-50);
# t.pendown();
# t.color("red")
# t.write("Circle");
# canvas.exitonclick();

# from turtle import *
#
# n = eval(input('How many sides:'))
# x = eval(input('Length of each side:'))
# total_degrees = (n - 2) * 180
# perangle_degrees = 180 - (total_degrees / n)
# i = 0
#
# canvas = Screen()
# canvas.setup(500,500)
# t = Turtle()
# t.color('black')
#
#
# while (i < n):
#     t.forward(x)
#     t.left(perangle_degrees)
#     i = i + 1
#
# canvas.exitonclick()

# from shapely.geometry import Polygon, Point, LineString;
# import matplotlib.pyplot as plt
#
# p1 = Point(0,1);
# p2  = Point(1,2);
#
# p1x = p1.x
# p1y = p1.y
# p2x = p2.x
# p2y = p2.y
#
# plt.plot(p1x, p1y, 'o');
# plt.plot(p2x, p2y, 'o');
#
# plt.show()

# from shapely.geometry import Polygon, Point, LineString, MultiPolygon
# import matplotlib.pyplot as plt
# from shapely.affinity import scale, translate, skew, rotate
# import shapely_graphics as sg
#
# #creates the triangle with vertices at specified points
# triangle = Polygon([(0,0),(1,0),(0,1)]);
# #scales the side lengths by 2x
# triangle_a = scale(triangle, xfact=2, yfact=2);
# #gets the coordinates of new triangle vertices
# triangle_a.exterior.coords[:];
# #Moves the triangle 3 units right and 4 units up
# triangle_b = translate(triangle,3,4);
# #gets triangle b’s coords
# triangle_b.exterior.coords[:];
# #rotates triangle 45 degrees
# triangle_c = rotate(triangle,45,(0,0), False);
# #gets triangle c coords
# triangle_c.exterior.coords[:];
#
# sg.plot_polygon(triangle, o = 'blue' )
# plt.figtext(0.28, 0.2, 'triangle 1')
#
# sg.plot_polygon(triangle_a, o = 'red' )
# plt.figtext(0.24, 0.13, 'triangle 2')
#
# sg.plot_polygon(triangle_b, o = 'purple' )
# plt.figtext(0.75, 0.7, 'triangle 3')
#
# sg.plot_polygon(triangle_c, o = 'green')
# plt.figtext(0.23, 0.3, 'triangle 4')
#
# plt.show()
import numpy as np
from turtle import *
from shapely.geometry import Polygon, Point, LineString, MultiPolygon
import matplotlib.pyplot as plt
from shapely.affinity import scale, translate, skew, rotate
from numpy import *
from shapely_graphics import *

# def main():
#     s1 = eval(input("Enter first side length (10-400): "))
#     s2 = eval(input("Enter second side length (10-400): "))
#     a1 = eval(input("Enter an angle (1-179): "))
#
#     s3 = np.sqrt( s1**2 + s2**2 - 2 * s1 * s2 * np.cos(a1 * (np.pi/180)))
#
#     largest = 0
#     smallest = 0
#     medium = 0

#     j = (s1 + s2 + s3)/2
#     area = np.sqrt(j * (j-s1) * (j-s2) * (j-s3))
#
#     if (s1 > s2 and s1 > s3):
#         largest = s1
#     elif (s2 > s1 and s2 > s3):
#         largest = s2
#     else:
#         largest = s3
#
#     if (s1 < s2 and s1 < s3):
#         smallest = s1
#     elif (s2 < s1 and s2 < s3):
#         smallest = s2
#     else:
#         smallest = s2
#
#     if (largest != s1 and smallest != s1):
#         medium = s1
#     elif (largest != s2 and smallest != s2):
#         medium = s2
#     else:
#         medium = s3
#
#     print(smallest, medium, largest)
#     print('Area:', area)
#
#     c2 = smallest ** 2
#     b2 = medium ** 2
#     a2 = largest ** 2
#
#     a2 = (np.arccos((a2 + c2 - b2) / (2 * largest * smallest))) * (180 / np.pi)
#     a3 = (180 - a1 -a2)
#
#     print(s1, s2, s3)
#     print(a1, a2, a3)

    # canvas = Screen()
    # canvas.setup(500,500)
    # t = Turtle()
    # t.color('black')
    #
    # t.forward(s1)
    # t.write(t.pos())
    # t.right(180 - a1)
    # t.forward(s2)
    # t.write(t.pos())
    # t.right(180 - a2)
    # t.forward(s3/2)
    # t.write('Here is your triangle!')
    # t.forward(s3/2)
    # t.write(t.pos())
    # t.right(180 - a3)
    #
    #
    #
    #
    #
    # canvas.exitonclick()


#
#     triangle = Polygon([(0, 0),(s1, 0),(0,s3)])
#     plot_polygon(triangle)
#
#
#     st1 = str(s1)
#     st3 = str(s3)
#     plt.figtext(0, 0, " (0,0)")
#     plt.figtext(s1, 0, '(' + st1 + ', 0)')
#     plt.figtext(0, s3, '(' + st3 + ', 0)')
#
#     plt.figtext(.4, .15, 'Here is your triangle!')
#
#     plt.show()
#
#
#
#
# main()

# canvas = Screen()
# canvas.setup(600,600)
# t = Turtle()
# t.color('black')
#
# pointx = 50
# pointy = 50
#
# sidelength = 200
#
# t.penup()
# t.goto(pointx, pointy)
#
# # t.forward(sidelength/2)
# # t.right(90)
# t.pendown()
# t.forward(sidelength)
# t.right(90)
# t.forward(sidelength)
# t.right(90)
# t.forward(sidelength)
# t.right(90)
# t.forward(sidelength)
# t.left(90)
# t.forward(sidelength)
# t.left(90)
# t.forward(sidelength)
# t.left(90)
# t.forward(sidelength)
# t.left(90)
# t.forward(sidelength)
# t.forward(sidelength)
# t.left(90)
# t.forward(sidelength)
# t.left(90)
# t.forward(sidelength)
# t.left(90)
# t.forward(sidelength)
# t.forward(sidelength)
# t.left(90)
# t.forward(sidelength)
# t.left(90)
# t.forward(sidelength)
#
# canvas.exitonclick()

# canvas = Screen()
# canvas.setup(500,500)
# t = Turtle()
# t.color('black')
#
# pointx = 50
# pointy = 50
#
# sidelength = 200
#
# t.penup()
# t.goto(pointx, pointy)
#
# # t.forward(sidelength/2)
# # t.right(120)
# t.pendown()
# t.forward(sidelength)
# t.right(120)
# t.forward(sidelength)
# t.right(120)
# t.forward(sidelength)
# t.right(240)
# t.forward(sidelength)
# t.left(120)
# t.forward(sidelength)
# t.left(120)
# t.forward(sidelength)
# t.forward(sidelength)
# t.right(120)
# t.forward(sidelength)
# t.right(120)
# t.forward(sidelength)
# t.left(120)
# t.forward(sidelength)
# t.left(120)
# t.forward(sidelength)
# t.left(60)
# t.forward(sidelength)
# t.left(60)
# t.forward(sidelength)
# t.left(120)
# t.forward(sidelength)
# t.left(180)
# t.forward(sidelength)
# t.left(120)
# t.forward(sidelength)

# canvas.exitonclick()


# pointx = 50
# pointy = 50
#
# sidelength = 200
#
# triangle = Polygon([(0,0),(3,0),(0,4)]);

from numpy import *

# x = 50
# y = 50
#
# sl = 200
#
# square1 = Polygon([(x, y), (x, y + sl),(x + sl, y + sl), (x + sl, y)])
# square2 = Polygon([(x, y), (x, y - sl),(x - sl, y - sl), (x - sl, y)])
# square3 = Polygon([(x, y), (x, y + sl),(x - sl, y + sl), (x - sl, y)])
# square4 = Polygon([(x, y), (x, y - sl),(x + sl, y - sl), (x + sl, y)])
#
# plot_polygon(square1, 'r')
# plot_polygon(square2, 'g')
# plot_polygon(square3, 'p')
# plot_polygon(square4, 'b')
#
# plt.show()

#
# sl = 200
# x = sl * (3**1/2) / 2
#
# triangle1 = Polygon([(0, 0), (0, -sl), (x, -x / 2)])
# triangle2 = Polygon([(0, 0), (x, -x / 2), (x, x / 2)])
# triangle3 = Polygon([(0, 0), (x, x / 2), (0, sl)])
# triangle4 = Polygon([(0, 0), (0, sl), (-x, x / 2)])
# triangle5 = Polygon([(0, 0), (-x, -x / 2), (-x, x / 2)])
# triangle6 = Polygon([(0, 0), (-x, -x / 2), (0, -sl)])

# plot_polygon(triangle1, 'r')
# plot_polygon(triangle2, 'b')
# plot_polygon(triangle3, 'g')
# plot_polygon(triangle4, 'o')
# plot_polygon(triangle5, 'y')
# plot_polygon(triangle6, 'p')
#
# plt.show()

# s = eval(input('Enter number of sides: '))
# sl = eval(input('Enter side length: '))

# if(s == 3 or s == 4 or s == 6):
#     print('You can tessellate')
#     t = True
# else:
#     print('You can only tessellate shapes that have 3, 4, or 6 sides')
#     t = False
#
# if(t == True):
#     canvas = Screen()
#     canvas.setup(1000, 1000)
#     t = Turtle()
#     t.color('black')
#     if(s == 6):
#         t.right(90)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#
#         t.left(60)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#         t.right(60)
#         t.forward(sl)
#         t.left(60)
#         t.forward(sl)
#         t.left(60)
#         t.forward(sl)
#         t.left(60)
#         t.forward(sl)
#         t.left(60)
#         t.forward(sl)
#
#     if(s == 3):
#         t.forward(sl)
#         t.right(120)
#         t.forward(sl)
#         t.right(120)
#         t.forward(sl)
#         t.right(240)
#         t.forward(sl)
#         t.left(120)
#         t.forward(sl)
#         t.left(120)
#         t.forward(sl)
#         t.forward(sl)
#         t.right(120)
#         t.forward(sl)
#         t.right(120)
#         t.forward(sl)
#         t.left(120)
#         t.forward(sl)
#         t.left(120)
#         t.forward(sl)
#         t.left(60)
#         t.forward(sl)
#         t.left(60)
#         t.forward(sl)
#         t.left(120)
#         t.forward(sl)
#         t.left(180)
#         t.forward(sl)
#         t.left(120)
#         t.forward(sl)
#
#
#     if(s == 4):
#         t.forward(sl)
#         t.right(90)
#         t.forward(sl)
#         t.right(90)
#         t.forward(sl)
#         t.right(90)
#         t.forward(sl)
#         t.left(90)
#         t.forward(sl)
#         t.left(90)
#         t.forward(sl)
#         t.left(90)
#         t.forward(sl)
#         t.left(90)
#         t.forward(sl)
#         t.forward(sl)
#         t.left(90)
#         t.forward(sl)
#         t.left(90)
#         t.forward(sl)
#         t.left(90)
#         t.forward(sl)
#         t.forward(sl)
#         t.left(90)
#         t.forward(sl)
#         t.left(90)
#         t.forward(sl)
#
#     canvas.exitonclick()

s = eval(input('Enter number of sides: '))
sl = eval(input('Enter side length: '))

x = sl * (3**1/2) / 2

if(s == 3 or s == 4 or s == 6):
    print('You can tessellate')
    t = True
else:
    print('You can only tessellate shapes that have 3, 4, or 6 sides')
    t = False

if(t == True):
    if(s == 3):
        triangle1 = Polygon([(0, 0), (0, -sl), (x, -x / 2)])
        triangle2 = Polygon([(0, 0), (x, -x / 2), (x, x / 2)])
        triangle3 = Polygon([(0, 0), (x, x / 2), (0, sl)])
        triangle4 = Polygon([(0, 0), (0, sl), (-x, x / 2)])
        triangle5 = Polygon([(0, 0), (-x, -x / 2), (-x, x / 2)])
        triangle6 = Polygon([(0, 0), (-x, -x / 2), (0, -sl)])

        plot_polygon(triangle1, 'r')
        plot_polygon(triangle2, 'b')
        plot_polygon(triangle3, 'g')
        plot_polygon(triangle4, 'o')
        plot_polygon(triangle5, 'y')
        plot_polygon(triangle6, 'p')


    if (s == 4):
        square1 = Polygon([(0, 0), (0,  sl),(sl, sl), ( sl, 0)])
        square2 = Polygon([(0, 0), (0,  -sl),(-sl,  -sl), ( -sl, 0)])
        square3 = Polygon([(0, 0), (0,  sl),( -sl, sl), ( -sl, 0)])
        square4 = Polygon([(0, 0), (0,  -sl),(sl, -sl), ( sl, 0)])

        plot_polygon(square1, 'r')
        plot_polygon(square2, 'g')
        plot_polygon(square3, 'p')
        plot_polygon(square4, 'b')


    if (s == 6):
        hexagon1 = Polygon([(x, -x / 2), (x, x / 2), (0, sl), (-x, x / 2), (-x, -x / 2), (0, -sl)])
        hexagon2 = Polygon([(-x, -x / 2), (0, -sl), (0, -sl - x), (-x, -2 * sl - x / 2), (-2 * x, -sl - x), (-2 * x, -sl)])
        hexagon3 = Polygon([(-2 * x, sl), (-x, x / 2), (-x, -x / 2), (-2 * x, -sl), (-3 * x, -x / 2), (-3 * x, x / 2)])

        plot_polygon(hexagon1, 'r')
        plot_polygon(hexagon2, 'g')
        plot_polygon(hexagon3, 'b')
    plt.show()