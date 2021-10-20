# from tkinter import *
# from random import randint
# root = Tk()
# lab = Label(root)
# lab.pack()
# mybutton = Button(root, text="Click Me")
# mybutton.pack()
# def update():
#    lab['text'] = randint(0,1000)
#    root.after(100, update) # run itself again after 1000 ms
#
# # run first time
# update()
#
# root.mainloop()



from tkinter import *
import tkMessageBox
master = Tk()
master.geometry('500x200')
def func():
   tkMessageBox.showinfo( "Hello Educba", "Press any key on the keyboard")
   b1 = Button( master, text='Click me for next step', background = 'Cyan', fg = '#000000', command = func)
   b1.pack()
def Keyboardpress( key):
   key_char = key.char
   print( key_char, 'key button is pressed on the keyboard')

master.bind( '<Key>', lambda i : Keyboardpress(i))
master.mainloop()