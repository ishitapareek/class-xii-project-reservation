from tkinter import *
from Child_Window import *

Pwindow = Tk()
Pwindow.title('Links :)')

def my_open():
    Cwindow = Toplevel(Pwindow)
    Cwindow.title('Child')
    label = Label(Cwindow, text = 'hi')
    label.grid(row = 0, column = 0)

   
    
txtbox = Entry(Pwindow)
txtbox.grid(row = 0, column = 0)
b1 = Button (Pwindow, text = 'Open child', command = lambda: CreateWindow(Pwindow, txtbox.get()))
b1.grid(row = 0, column = 1)


Pwindow.mainloop()

