import tkinter as tk
import tkinter.font as tkFont
from CalculatorMath import Evaluate

class App:
   eq = ''

   def __init__(self, root):
        self.evaluate = Evaluate()
        self.root = root
        # setting title
        self.root.title("Python Calculator")
        # setting window size
        width = 700
        height = 800
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        GLabel_306 = tk.Label(self.root)
        GLabel_306["bg"] = "#000181"
        ft = tkFont.Font(family='Times', size=10)
        GLabel_306["font"] = ft
        GLabel_306["fg"] = "#333333"
        GLabel_306["justify"] = "center"
        GLabel_306["text"] = ""
        GLabel_306["relief"] = "flat"
        GLabel_306.place(x=0, y=0, width=700, height=800)

        GButton_544 = tk.Button(self.root)
        GButton_544["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_544["font"] = ft
        GButton_544["fg"] = "#000000"
        GButton_544["justify"] = "center"
        GButton_544["text"] = "1"
        GButton_544["relief"] = "flat"
        GButton_544.place(x=20, y=680, width=150, height=100)
        GButton_544["command"] = self.GButton_544_command

        GButton_70 = tk.Button(self.root)
        GButton_70["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_70["font"] = ft
        GButton_70["fg"] = "#000000"
        GButton_70["justify"] = "center"
        GButton_70["text"] = "2"
        GButton_70.place(x=190, y=680, width=150, height=100)
        GButton_70["command"] = self.GButton_70_command

        GButton_413 = tk.Button(self.root)
        GButton_413["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_413["font"] = ft
        GButton_413["fg"] = "#000000"
        GButton_413["justify"] = "center"
        GButton_413["text"] = "3"
        GButton_413.place(x=360, y=680, width=150, height=100)
        GButton_413["command"] = self.GButton_413_command

        GButton_701 = tk.Button(self.root)
        GButton_701["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_701["font"] = ft
        GButton_701["fg"] = "#000000"
        GButton_701["justify"] = "center"
        GButton_701["text"] = "enter"
        GButton_701.place(x=530, y=680, width=150, height=100)
        GButton_701["command"] = self.GButton_701_command

        GButton_253 = tk.Button(self.root)
        GButton_253["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_253["font"] = ft
        GButton_253["fg"] = "#000000"
        GButton_253["justify"] = "center"
        GButton_253["text"] = "4"
        GButton_253.place(x=20, y=560, width=150, height=100)
        GButton_253["command"] = self.GButton_253_command

        GButton_435 = tk.Button(self.root)
        GButton_435["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_435["font"] = ft
        GButton_435["fg"] = "#000000"
        GButton_435["justify"] = "center"
        GButton_435["text"] = "7"
        GButton_435.place(x=20, y=440, width=150, height=100)
        GButton_435["command"] = self.GButton_435_command

        GButton_45 = tk.Button(self.root)
        GButton_45["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_45["font"] = ft
        GButton_45["fg"] = "#000000"
        GButton_45["justify"] = "center"
        GButton_45["text"] = "0"
        GButton_45.place(x=20, y=320, width=150, height=100)
        GButton_45["command"] = self.GButton_45_command

        GButton_110 = tk.Button(self.root)
        GButton_110["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_110["font"] = ft
        GButton_110["fg"] = "#000000"
        GButton_110["justify"] = "center"
        GButton_110["text"] = "^"
        GButton_110.place(x=20, y=200, width=150, height=100)
        GButton_110["command"] = self.GButton_110_command

        GButton_648 = tk.Button(self.root)
        GButton_648["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_648["font"] = ft
        GButton_648["fg"] = "#000000"
        GButton_648["justify"] = "center"
        GButton_648["text"] = "'x'"
        GButton_648.place(x=190, y=200, width=150, height=100)
        GButton_648["command"] = self.GButton_648_command

        GButton_204 = tk.Button(self.root)
        GButton_204["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_204["font"] = ft
        GButton_204["fg"] = "#000000"
        GButton_204["justify"] = "center"
        GButton_204["text"] = "."
        GButton_204.place(x=190, y=320, width=150, height=100)
        GButton_204["command"] = self.GButton_204_command

        GButton_181 = tk.Button(self.root)
        GButton_181["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_181["font"] = ft
        GButton_181["fg"] = "#000000"
        GButton_181["justify"] = "center"
        GButton_181["text"] = "8"
        GButton_181.place(x=190, y=440, width=150, height=100)
        GButton_181["command"] = self.GButton_181_command

        GButton_640 = tk.Button(self.root)
        GButton_640["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_640["font"] = ft
        GButton_640["fg"] = "#000000"
        GButton_640["justify"] = "center"
        GButton_640["text"] = "5"
        GButton_640.place(x=190, y=560, width=150, height=100)
        GButton_640["command"] = self.GButton_640_command

        GButton_532 = tk.Button(self.root)
        GButton_532["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_532["font"] = ft
        GButton_532["fg"] = "#000000"
        GButton_532["justify"] = "center"
        GButton_532["text"] = "6"
        GButton_532.place(x=360, y=560, width=150, height=100)
        GButton_532["command"] = self.GButton_532_command

        GButton_622 = tk.Button(self.root)
        GButton_622["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_622["font"] = ft
        GButton_622["fg"] = "#000000"
        GButton_622["justify"] = "center"
        GButton_622["text"] = "+"
        GButton_622.place(x=530, y=560, width=150, height=100)
        GButton_622["command"] = self.GButton_622_command

        GButton_793 = tk.Button(self.root)
        GButton_793["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_793["font"] = ft
        GButton_793["fg"] = "#000000"
        GButton_793["justify"] = "center"
        GButton_793["text"] = "9"
        GButton_793.place(x=360, y=440, width=150, height=100)
        GButton_793["command"] = self.GButton_793_command

        GButton_905 = tk.Button(self.root)
        GButton_905["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_905["font"] = ft
        GButton_905["fg"] = "#000000"
        GButton_905["justify"] = "center"
        GButton_905["text"] = "-"
        GButton_905.place(x=530, y=440, width=150, height=100)
        GButton_905["command"] = self.GButton_905_command

        GButton_778 = tk.Button(self.root)
        GButton_778["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=40)
        GButton_778["font"] = ft
        GButton_778["fg"] = "#000000"
        GButton_778["justify"] = "center"
        GButton_778["text"] = "Graph"
        GButton_778.place(x=360, y=320, width=150, height=100)
        GButton_778["command"] = self.GButton_778_command

        GButton_911 = tk.Button(self.root)
        GButton_911["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_911["font"] = ft
        GButton_911["fg"] = "#000000"
        GButton_911["justify"] = "center"
        GButton_911["text"] = "x"
        GButton_911.place(x=530, y=320, width=150, height=100)
        GButton_911["command"] = self.GButton_911_command

        GButton_16 = tk.Button(self.root)
        GButton_16["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=28)
        GButton_16["font"] = ft
        GButton_16["fg"] = "#000000"
        GButton_16["justify"] = "center"
        GButton_16["text"] = ":)"
        GButton_16.place(x=360, y=200, width=150, height=100)
        GButton_16["command"] = self.GButton_16_command

        GButton_131 = tk.Button(self.root)
        GButton_131["bg"] = "#ffe6b6"
        ft = tkFont.Font(family='Times', size=48)
        GButton_131["font"] = ft
        GButton_131["fg"] = "#000000"
        GButton_131["justify"] = "center"
        GButton_131["text"] = "/"
        GButton_131.place(x=530, y=200, width=150, height=100)
        GButton_131["command"] = self.GButton_131_command

        self.changeLabel("")

   def changeLabel(self, text):
       GLabel_136 = tk.Label(self.root)
       GLabel_136["bg"] = "#1e90ff"
       ft = tkFont.Font(family='Times', size=48)
       GLabel_136["font"] = ft
       GLabel_136["fg"] = "#000000"
       GLabel_136["justify"] = "center"
       GLabel_136["text"] = text
       GLabel_136["relief"] = "flat"
       GLabel_136.place(x=30, y=30, width=633, height=148)

   def GButton_544_command(self):
       self.eq = self.eq + '1'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_70_command(self):

       self.eq = self.eq + '2'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_413_command(self):

       self.eq = self.eq + '3'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_701_command(self):
       print('enter')
       try:
           nstr = self.evaluate.toPost(self.eq)
           self.eq = self.evaluate.evalPostfix(nstr)
           self.changeLabel(self.eq)
           self.eq = ''
       except:
           self.eq = ''
           self.changeLabel(self.eq)

   def GButton_253_command(self):

       self.eq = self.eq + '4'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_435_command(self):

       self.eq = self.eq + '7'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_45_command(self):

       self.eq = self.eq + '0'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_110_command(self):

       self.eq = self.eq + '^'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_648_command(self):
       self.eq = self.eq + 'x'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_204_command(self):

       self.eq = self.eq + '.'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_181_command(self):

       self.eq = self.eq + '8'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_640_command(self):

       self.eq = self.eq + '5'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_532_command(self):

       self.eq = self.eq + '6'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_622_command(self):

       self.eq = self.eq + '+'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_793_command(self):

       self.eq = self.eq + '9'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_905_command(self):

       self.eq = self.eq + '-'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_778_command(self):
       self.eq = self.evaluate.grapheq(self.eq)

   def GButton_911_command(self):

       self.eq = self.eq + '*'
       print(self.eq)
       self.changeLabel(self.eq)

   def GButton_16_command(self):
       self.eq = "Go play in the street"
       print(self.eq)
       self.changeLabel(self.eq)




   def GButton_131_command(self):

       self.eq = self.eq + '/'
       print(self.eq)
       self.changeLabel(self.eq)

