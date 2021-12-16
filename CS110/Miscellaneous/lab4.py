import math
import random

# print(2**10)
# print(100/3)
# print(100//3)
# print(100%3)

# date = 16;
# print("Today is June", date);
# date +=1;
# print("Tomorrow is June", date);
#
# weight = 30;
# print("My dog weighs", weight, "pounds on earth.");
# weight /= 6;
# print("My dog weights", weight, "pounds on the moon.");

# print("The value of e is", math.e);
#
# print(math.log(math.exp(2)));
# print(math.sin(math.pi/2));
# print(math.sin(math.pi));

# firstRandom = random.gauss(1,3)
# print(firstRandom)

# import sympy as sp;
# print(sp.sin(sp.pi));
# print(sp.sin(math.pi));
#
# sp.sqrt(8)
# x,y = sp.symbols('x y')
# expr = x + 2*y
# print(sp.expand(x*(x+1)))
# print(sp.factor(x**2 + 2*x*y + y**2))
# print(sp.simplify(sp.sin(x)**2+sp.cos(x)**2))
# print(sp.diff(sp.cos(x), x))
# print(sp.integrate(sp.cos(x), x))
# print(sp.limit(sp.sin(x)/x, x, 0))

# import numpy as np;
# x = np.array([1,5,2])
# y = np.array([7,4,1])
# print(x+y)
# print(np.dot(x,y))
# print(np.cross(x,y))

# x = np.array([9, 25, 81])
# y = np.sqrt(x)
# z = np.sin(x)
# print(x)
# print(y)
# print(z)

# x = np.array([2, 3, 4, 9, 9, 10, 11]);
# print(np.nanmean(x))
# print(np.nanstd(x))
# print(np.nanvar(x))

# print(np.poly([2,3]))
# print(np.roots([1,2,1]))

import numpy as np
import matplotlib.pyplot as plt

# xVals = np.array([1,2,3,4]);
# yVals = xVals**2;
#plt.plot(yVals);
#plt.plot(xVals, yVals);
#plt.plot(xVals, yVals, 'r');
#plt.plot(xVals, yVals, 'ro');
#plt.plot(xVals, yVals, 'rx');
#plt.plot(xVals, yVals, 'g+');
# plt.plot(xVals, yVals, 'c*', label='Points')
# plt.axis([0,5,0,18]);
# plt.title("Quadratic");
# plt.grid(True);
# plt.legend(loc='upper left');
# plt.xlabel('x axis title');
# plt.ylabel('y axis title');
# plt.figtext(3,7,'test12341323')
# plt.show();

# x = np.arange(0, 5, .2)
# plt.plot(x,x**2)
# plt.plot(x,x)
# plt.plot(x, x**3)
# plt.plot(x, np.cos(x))
# plt.show();

# import numpy as np
# import matplotlib.pyplot as plt
#
#
# scores = [71, 98, 80, 85, 85, 93, 74, 70, 88, 80, 91, 83, 82, 84, 84, 84, 84, 82, 80, 88, 79, 95, 87, 85, 90]
# plt.hist(scores)
# plt.axis([65, 100, 0, 10])
# mean = np.average(scores)
# stdev = np.nanstd(scores)
# plt.figtext(65,8, mean)
# plt.figtext(65,7, stdev)
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('Histogram')
# plt.grid(True)
# plt.show()

x = math.factorial(52) / ((math.factorial(52-5)) * (math.factorial(5)))
y = math.factorial(51) / ((math.factorial(51-5)) * (math.factorial(5)))
print(x-y)
print((x-y)/x)
