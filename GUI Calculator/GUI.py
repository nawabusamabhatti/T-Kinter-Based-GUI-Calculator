#NaWaB-UsAmA-BhAtti
#Python 3.0 ! / T-Kinter 1 / AnaConda 3-Environment


from tkinter import *
from math import *
from datetime import *
from random import *
import  os as os
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def Equals(N1, N2, S1):
    LED.delete(0, END)
    if S1 == "+":
        LED.insert(0, N1 + N2)
    if S1 == "-":
        LED.insert(0, N1 - N2)
    if S1 == "/":
        LED.insert(0, N1 / N2)
    if S1 == "*":
        LED.insert(0, N1 * N2)
    if S1 == "Pow":
        LED.insert(0, N1**N2)
    if S1 == "LOG2N":
        LED.insert(0, log(N2,N1))



def LTI():
    Temp = list(LED.get())
    Temp = "".join(Temp)
    return float(Temp)

def Click(A):
    Previous = LED.get()
    LED.delete(0, END)
    LED.insert(0, str(Previous)+str(A))


def OP(S):
    global Num1, Num2, State
    if S == "C":
        LED.delete(0, END)
    elif S == "<-":
        Temp = list(LED.get())
        Temp.pop()
        Temp = "".join(Temp)
        LED.delete(0, END)
        LED.insert(0, Temp)
    if S == "+":
        State = "+"
        Num1 = LTI()
        LED.delete(0, END)
    if S == "-":
        State = "-"
        Num1 = LTI()
        LED.delete(0, END)
    if S == "/":
        State = "/"
        Num1 = LTI()
        LED.delete(0, END)
    if S == "*":
        State = "*"
        Num1 = LTI()
        LED.delete(0, END)
    if S == "=":
        Num2 = LTI()
        Equals(Num1, Num2, State)
    if S == ".":
        LED.insert(0, ".")
    if S == "SQ":
        Num1 = LTI()
        LED.delete(0, END)
        LED.insert(0, "%.2f"%sqrt(Num1))
    if S == "S":
        Num1 = LTI()
        LED.delete(0, END)
        LED.insert(0, Num1*Num1)
    if S == "SP":
        State = "Pow"
        Num1 = LTI()
        LED.delete(0, END)
    if S == "LOG":
        Num1 = LTI()
        LED.delete(0, END)
        LED.insert(0, "%.4f"%log2(Num1))
    if S == "LOG10":
        State = "LOG"
        Num1 = LTI()
        LED.delete(0, END)
        LED.insert(0, "%.4f"%log10(Num1))
    if S == "LOG2N":
        State = "LOG2N"
        Num1 = LTI()
        LED.delete(0, END)
    if S == "X!":
        Num1 = LTI()
        LED.delete(0, END)
        LED.insert(0, factorial(Num1))


def DT():
    Date = now.strftime("%Y-%m-%d %H:%M:%S")
    Label3 = Label(Base, text=Date, bg="black", fg="white").place(x=150, y=360)
    Base.after(2000, DT)

def Event(event):
    Temp = event.keysym
    if Temp ==  "1" or Temp == "2" or\
            Temp == "3" or Temp == "4" \
            or Temp == "5" or Temp == "6" \
            or Temp == "7" or Temp == "8" or\
            Temp == "9" or Temp == "0" or Temp == "period":
        if Temp == "period":
            Click(".")
        else:
            Click(Temp)
    if Temp == "slash":
        OP("/")
    if Temp == "asterisk":
        OP("*")
    if Temp == "minus":
        OP("-")
    if Temp == "plus":
        OP("+")
    if Temp == "Return":
        OP("=")
    if Temp == "BackSpace":
        OP("<-")
    if Temp == "c" or Temp == "C":
        OP("C")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #.


Base = Tk() #className="Calculator V2"
Base.title("Calculator V2")
Base.geometry("280x440")
# Base.iconbitmap('Icon.ico')
Base.configure(bg='Black')
now = datetime.now()
Date = now.strftime("%Y-%m-%d %H:%M:%S")



Label2 = Label(Base, text=Date, bg="black", fg="white").place(x=170, y=0)

var = StringVar()
LED = Entry(Base, width=45,  borderwidth=1, font=('calibri',12))
LED.grid(row=0, column=0, columnspan=1, padx=1, pady=25)
# LED.insert(0, "Enter Data: ")

ButtonHeightThresold = 35
ButtonSizeThresold_X = 30
ButtonSizeThresold_Y = 15

Button1 = Button(Base, text="1", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: Click(1)).place(x=0, y=20+ButtonHeightThresold)
Button2 = Button(Base, text="2", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: Click(2)).place(x=70, y=20+ButtonHeightThresold)
Button3 = Button(Base, text="3", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: Click(3)).place(x=140, y=20+ButtonHeightThresold)

ButtonHeightThresold = 85
ButtonSizeThresold_X = 30
ButtonSizeThresold_Y = 15

Button4 = Button(Base, text="4", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: Click(4)).place(x=0, y=20+ButtonHeightThresold)
Button5 = Button(Base, text="5", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: Click(5)).place(x=70, y=20+ButtonHeightThresold)
Button6 = Button(Base, text="6", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: Click(6)).place(x=140, y=20+ButtonHeightThresold)


ButtonHeightThresold = 135
ButtonSizeThresold_X = 30
ButtonSizeThresold_Y = 15

Button7 = Button(Base, text="7", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: Click(7)).place(x=0, y=20+ButtonHeightThresold)
Button8 = Button(Base, text="8", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: Click(8)).place(x=70, y=20+ButtonHeightThresold)
Button9 = Button(Base, text="9", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: Click(9)).place(x=140, y=20+ButtonHeightThresold)

ButtonHeightThresold = 185
ButtonSizeThresold_X = 30
ButtonSizeThresold_Y = 15

Button10 = Button(Base, text="C", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: OP("C")).place(x=0, y=20+ButtonHeightThresold)
Button11 = Button(Base, text="0", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: Click(0)).place(x=70, y=20+ButtonHeightThresold)
Button12 = Button(Base, text="<-", padx=ButtonSizeThresold_X-3, pady=ButtonSizeThresold_Y, command=lambda: OP("<-")).place(x=140, y=20+ButtonHeightThresold)
Button18 = Button(Base, text=".", padx=30, pady=15, command=lambda: Click(".")).place(x=140, y=255)
Button21 = Button(Base, text="x^▯", padx=30, pady=15, command=lambda: OP("SP")).place(x=0, y=255)
Button20 = Button(Base, text="x^2", padx=30, pady=15, command=lambda: OP("S")).place(x=70, y=255)
Button19 = Button(Base, text="√", padx=30, pady=15, command=lambda: OP("SQ")).place(x=140, y=255)
Button22 = Button(Base, text="㏒▯(2)", padx=30, pady=15, command=lambda: OP("LOG")).place(x=-15, y=305)
Button23 = Button(Base, text="㏒▯(10)", padx=30, pady=15, command=lambda: OP("LOG10")).place(x=60, y=305)
ButtonSizeThresold_X = 30
ButtonSizeThresold_Y = 15
Button13 = Button(Base, text="+", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: OP("+")).place(x=210, y=55)
Button14 = Button(Base, text="-", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: OP("-")).place(x=210, y=105)
Button15 = Button(Base, text="/", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: OP("/")).place(x=210, y=155)
Button16 = Button(Base, text="*", padx=ButtonSizeThresold_X, pady=ButtonSizeThresold_Y, command=lambda: OP("*")).place(x=210, y=205)
Button17 = Button(Base, text="=", padx=30, pady=15, command=lambda: OP("=")).place(x=210, y=255)
Button23 = Button(Base, text="▯㏒▯", padx=30, pady=15, command=lambda: OP("LOG2N")).place(x=150, y=305)
Button24 = Button(Base, text="X!", padx=30, pady=15, command=lambda: OP("X!")).place(x=220, y=305)
lab = Label(Base, bg="black", fg="white").place(x=150, y=360)
Base.bind("<Key>", Event)
image = PhotoImage(file="IG.png")
resource_path("IG.png")
ADLabel = Label(image=image, bg='black').place(x=35, y=360)
Label1 = Label(Base, text="Developed By NaWaB Usama BhAtti", bg="black", fg="white").place(x=40, y=410)
Label3 = Label(Base, text="@nawab_usama_bhatti", bg="black", fg="white").place(x=112, y=380)
# DT()


Base.mainloop()


