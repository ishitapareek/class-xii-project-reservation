from tkinter import *
from tkinter import messagebox

from Reservation_Info import *

from WindowStyle import *
import tkinter.font as font

    
def CreateLabel(container, caption, r, c):
    label = Label(container, text = caption)
    SetLabelStyle_Input(label)
    label.grid (row = r, column = c)


def Submit():
    Username = Usertxt.get()
    Password = Passwordtxt.get()

    
    if Username == 'admin' and Password == '123':
        messagebox.showinfo ('Login', 'Correct Login.')
        InfoScreen() #Function in Reservation_Info.py
        root.destroy()

        
    else:
        messagebox.showinfo ('Login', 'Incorrect Login. \n \n Check username/password.')



def LoginScreen(Pwindow):
    global Usertxt
    global Passwordtxt
    global root

    
    root = Toplevel(Pwindow)
    root.title('Bermuda Cruise - Login')

    root.iconbitmap("doodle.ico")

    root.geometry('290x85')
    root.resizable(False, False)

    SetWindowBG(root)

    CreateLabel (root, 'Username:', 1, 0)

    Usertxt = Entry (root)
    Usertxt.grid (row = 1, column = 1)

    CreateLabel (root, 'Password: ', 2, 0)

    Passwordtxt = Entry (root, show = '*')
    Passwordtxt.grid (row = 2, column = 1)
    

    Submitbtn = Button (root, text = 'Submit', command = Submit)
    SetButtonStyle(Submitbtn)
    Submitbtn.grid (row = 3, column = 0, columnspan = 2)


    root.mainloop()

