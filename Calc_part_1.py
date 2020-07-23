import tkinter
from tkinter import *
import math
import parser
from tkinter import messagebox

root = tkinter.Tk()
root.title("Calculator")

root.geometry("350x520+0+0")

# functions for button clicking event

val = ""
A=0
operator = ""


def btn1_is_clicked():
    global val
    val +="1"
    data.set(val)

def btn2_is_clicked():
    global val
    val +="2"
    data.set(val)

def btn3_is_clicked():
    global val
    val +="3"
    data.set(val)

def btn4_is_clicked():
    global val
    val +="4"
    data.set(val)

def btn4_is_clicked():
    global val
    val +="4"
    data.set(val)

def btn5_is_clicked():
    global val
    val +="5"
    data.set(val)

def btn6_is_clicked():
    global val
    val +="6"
    data.set(val)

def btn7_is_clicked():
    global val
    val +="7"
    data.set(val)

def btn8_is_clicked():
    global val
    val +="8"
    data.set(val)

def btn9_is_clicked():
    global val
    val +="9"
    data.set(val)

def btn0_is_clicked():
    global val
    val +="0"
    data.set(val)

def btn_plus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val += "+"
    data.set(val)

def btn_sub_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val += "-"
    data.set(val)

def btn_mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val += "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val += "/"
    data.set(val)

def C_presed():
    global A
    global operator
    global val
    A = 0
    operator = ""
    val = ""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2= val
    if operator == "+":
        x= int((val2.split("+")[1]))
        C=A+x
        data.set(C)
        val = str(C)

    elif operator == "-":
        x= int((val2.split("-")[1]))
        C= A-x
        data.set(C)
        val = str(C)

    elif operator == "*":
        x= int((val2.split("*")[1]))
        C=A*x
        data.set(C)
        val = str(C)

    elif operator == "/":
        x= int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error" , "Division by zero not supported")
            A = ""
            val = ""
            data.set(val)
        else:    
            C = int(A / x)
            data.set(C)
            val = str(C)


data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verdana" ,20),
    textvariable = data,
    background = "white",
    fg  = "black",
)
lbl.pack(expand =True , fill = "both")

btnrow1= Frame(root, bg="#000000")
btnrow1.pack(expand = True , fill = "both" ,)


btnrow2= Frame(root)
btnrow2.pack(expand = True , fill = "both" ,)


btnrow3= Frame(root)
btnrow3.pack(expand = True , fill = "both" ,)


btnrow4= Frame(root)
btnrow4.pack(expand = True , fill = "both" ,)

## ************************************************************* ROW 1  *********************************************************
btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn1_is_clicked,
)
btn1.pack(side = LEFT, expand = True, fill= "both")


btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn2_is_clicked,
)
btn2.pack(side = LEFT, expand = True, fill= "both")

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn3_is_clicked,
)
btn3.pack(side = LEFT, expand = True, fill= "both")

btn_plus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_plus_clicked,
    
)
btn_plus.pack(side = LEFT, expand = True, fill= "both")


#************************************************************* ROW 2  *************************************************

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn4_is_clicked,
)
btn4.pack(side = LEFT, expand = True, fill= "both")


btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn5_is_clicked,
)
btn5.pack(side = LEFT, expand = True, fill= "both")

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn6_is_clicked,
)
btn6.pack(side = LEFT, expand = True, fill= "both")

btn_sub = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_sub_clicked,
)
btn_sub.pack(side = LEFT, expand = True, fill= "both")

# ********************************************************************** ROW 3 ******************************************************


btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn7_is_clicked,
)
btn7.pack(side = LEFT, expand = True, fill= "both")


btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn8_is_clicked,
)
btn8.pack(side = LEFT, expand = True, fill= "both")

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn9_is_clicked,
)
btn9.pack(side = LEFT, expand = True, fill= "both")

btn_mul = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_mul_clicked,
)
btn_mul.pack(side = LEFT, expand = True, fill= "both")

#************************************************************************ ROW 4 ******************************************

btn_C = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = C_presed,
)
btn_C.pack(side = LEFT, expand = True, fill= "both")


btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn0_is_clicked,
)
btn0.pack(side = LEFT, expand = True, fill= "both")

btn_Equal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btn_Equal.pack(side = LEFT, expand = True, fill= "both")

btn_div = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn_div_clicked,
)
btn_div.pack(side = LEFT, expand = True, fill= "both")
# *************************************************************************************************************


root.mainloop()
