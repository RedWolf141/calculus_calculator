# import
import tkinter
from tkinter import ttk
import random
from sympy import *

def random_position(num1):
    num2 = 1/num1
    print(num1, num2)
    dset = pow((sqrt(2) -num1),2) + pow(sqrt(2)-num2,2)
    dse = sqrt(dset)
    d2set = pow( (sqrt(2) * -1 - num1),2 ) + pow(sqrt(2) * -1 - num2, 2)
    d2se = sqrt(d2set)
    k = abs(dse - d2se).evalf()
    return k
# instance
window = tkinter.Tk()

# title
window.title("First Window")

# geomerty
window.geometry('300x100')

# preventing GUI from resizing
window.resizable(False, False)


def buttonClicked():
    label.configure(foreground='blue')
    k = rand_max.get()
    p = int(k)
    labelNew.configure(text=random_position(p))
    a = random.randrange(1,p)
    ap = str(a)
    ap2 = str(round(1/a,4))
    rand_x.configure(text=ap)
    rand_reverse_x.configure(text=ap2)

# Label
label = ttk.Label(window, text="이름을 입력하세요")
label.grid(column=0, row=0)

# Button
button = ttk.Button(window, text="클릭", command=buttonClicked)
button.grid(column=1, row=1)

# Text Box
rand_max = tkinter.StringVar()
textbox = ttk.Entry(window, width=12, textvariable=rand_max)
textbox.grid(column=0, row=1)

# Label
labelNew = ttk.Label(window, text="")
labelNew.grid(column=1, row=2)

rand_x = ttk.Label(window, text="")
rand_x.grid(column=1, row=4)

rand_reverse_x = ttk.Label(window, text="")
rand_reverse_x.grid(column=2, row=4)
# start GUI
window.mainloop()