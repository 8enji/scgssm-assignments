import tkinter as tk
from CalculatorGUI import App
from CalculatorMath import Evaluate

if __name__ == "__main__":
   root = tk.Tk()
   app = App(root)
   root.mainloop()
   # ev = Evaluate()
   # ev.grapheq("x^2")