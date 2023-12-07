import random
from sympy import *

def random_position():
    num1 = random.randrange(1, 100)
    num2 = 1/num1
    print(num1, num2)
    dset = pow((sqrt(2) -num1),2) + pow(sqrt(2)-num2,2)
    dse = sqrt(dset)
    d2set = pow( (sqrt(2) * -1 - num1),2 ) + pow(sqrt(2) * -1 - num2, 2)
    d2se = sqrt(d2set)
    k = abs(dse - d2se).evalf()
    print(k)
    return k
for x in range(10):
    random_position()

'''
May 2017
@author: Burkhard A. Meier
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# Modify adding a Label
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

# Modified Button Click Function
def click_me():
    name.configure(text=random_position())
#     print(number)
#     print(number.get())

# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)                          # column 0

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)                                # <= change column to 2

name_entered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()