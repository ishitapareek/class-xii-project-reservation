from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Login')


    
def CreateLabel(container, caption, r, c):
    label = Label (container, text = caption)
    label.grid (row = r, column = c)


def Submit():
    Username = Usertxt.get()
    Password = Passwordtxt.get()
    
    if Username == 'admin' and Password == '123':
        messagebox.showinfo ('Login', 'Correct Login.')

        
    else:
        messagebox.showinfo ('Login', 'Incorrect Login. \n \n Check username/password.')




CreateLabel (root, 'Username:', 0, 0)

Usertxt = Entry (root)
Usertxt.grid (row = 0, column = 1)


CreateLabel (root, 'Password: ', 1, 0)

Passwordtxt = Entry (root, show = '*')
Passwordtxt.grid (row = 1, column = 1)



Submitbtn = Button (root, text = 'Submit', command = Submit)
Submitbtn.grid (row = 2, column = 0, columnspan = 2)


root.mainloop()
