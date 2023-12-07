'''
May 2017
@alpha release 1.0.1
적분 계산 추가

@alpha release 1.0.2
상/하 부정적분
'''
#======================
# imports
#======================
from sympy import *
import tkinter as tk
from tkinter import ttk

# Sympy Set Symbol
init_printing()
x = Symbol('x')

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# Modify adding a Label
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0, row=0)

cnt =0
# Modified Button Click Function
def click_me():

    if (number_chosen.get()=="미분"):
        k = sympify(function.get())
        f = diff(k,x)
        f = str(f)
        action.configure(text = f)
    elif (number_chosen.get()=="적분"):
        k = sympify(function.get())
        a, b= sympify(lower_entered.get()), sympify(upper_entered.get())
        f = integrate(k,(x,a,b))
        f = str(f)
        action.configure(text=f)
'''
def setting():
    cnt=0
    if (cnt==0):
        x = Symbol(sympify(xyz_entered.get()))
        cnt +=1
    elif (cnt==1):
        y = Symbol(sympify(xyz_entered.get()))
        cnt +=1
    elif (cnt==2):
        z = Symbol(sympify(xyz_entered.get()))
        cnt += 1
'''
# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
ttk.Label(win, text="하한값").grid(column=0,row=4)
ttk.Label(win, text="상한값").grid(column=1,row=4)
# ttk.Label(win, text="변수설정").grid(column=0, row=6)

# Adding a Textbox Entry widget
function = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=function)
name_entered.grid(column=0, row=1)

lower = tk.StringVar() # 적분 하한값
lower_entered = ttk.Entry(win, width=12, textvariable=lower)
lower_entered.grid(column=0,row=5)

upper = tk.StringVar()
upper_entered = ttk.Entry(win, width=12, textvariable=upper)
upper_entered.grid(column=1, row=5)

'''
xyz = tk.StringVar()
xyz_entered = ttk.Entry(win, width=12, textvariable=xyz)
xyz_entered.grid(column=0, row=7)
'''

#result = tk.StringVar() # 적분 하한값
#result_output = ttk.Entry(win, width=12, textvariable=result)
#result_output.grid(column=0,row=5)


# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)                                 # <= change column to 2

'''
xyz_setting = ttk.Button(win, text="변수설정", command=setting)
xyz_setting.grid(column=1, row=6)
'''

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = ("미분", "적분", "변수등록", "???", "???")
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

name_entered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()
