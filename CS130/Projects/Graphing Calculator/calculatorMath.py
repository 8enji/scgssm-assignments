import matplotlib.pyplot as plt

class Evaluate:
   def toPost(self, x):
       new = ""
       for n in x:
           if n in "0123456789.":
               new = new + n
           else:
               new = new + "," + n + ","
       new = new.split(',')
       x = new
       nstack = []
       ostack = []
       final = ''
       precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
       for char in x:
           try:
               intx = float(char)
               final = final + " " + str(float(intx))
           except:
               if (len(ostack) == 0 or precedence[char] > precedence[ostack[-1]]):
                   ostack.append(char)
               else:
                   while (precedence[char] <= precedence[ostack[-1]]):
                       final = final + " " + ostack.pop(-1)
                       if len(ostack) == 0:
                           break
                   ostack.append(char)
       for i in range(len(ostack)):
           final = final + " " + str(ostack.pop(-1))
       return final

   def evalPostfix(self, nstr):
       s = list()
       nstr = nstr.replace("^", "**")
       nstr = nstr.split(" ")
       # print(nstr)
       nstr.remove("")
       # print(nstr)
       for n in nstr:
           if n not in "-/**+":
               s.insert(0, float(n))
               plus = None
           elif n == "/":
               plus = float(s.pop(1)) / float(s.pop(0))
               s.insert(0, plus)
           elif n == "*":
               plus = float(s.pop(1)) * float(s.pop(0))
               s.insert(0, plus)
           elif n == "**":
               plus = float(s.pop(1)) ** float(s.pop(0))
               s.insert(0, plus)
           elif n == "+":
               plus = float(s.pop(1)) + float(s.pop(0))
               s.insert(0, plus)
           elif n == "-":
               plus = float(s.pop(1)) - float(s.pop(0))
               s.insert(0, plus)
           # print(s)
       eq = s.pop()
       if str(eq)[-2:] == ".0":
           eq = int(eq)
       return eq

   def grapheq(self, eq):

       try:
           eq = eq.replace("^", "**")
       except:
           pass

       # x axis values
       xs = [n for n in range(-20,20)]
       ys = []
       # corresponding y axis values
       for x in xs:
           x = eq.replace("x", str(x))
           ys.append(eval(x))

       print(xs)
       print(ys)

       plt.plot(xs, ys)

       plt.xlabel('x - axis')

       plt.ylabel('y - axis')
       plt.grid()
       plt.show()

