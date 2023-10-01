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




'''Userbtn = StringVar()

CreateLabel (root, 'Employee or Customer: ', 0, 0)
Customerbtn = Radiobutton (root, text = 'Customer', variable = Breakfastbtn, value = 'Customer')
Customerbtn.grid(row = 0, column = 1)

Employeebtn = Radiobutton (frameBooking, text = 'Employee', variable = Breakfastbtn, value = 'Employee')
Employeebtn.grid(row = 0, column = 2)

Userbtn.set(None)'''

CreateLabel (root, 'Username:', 1, 0)

Usertxt = Entry (root)
Usertxt.grid (row = 1, column = 1)


CreateLabel (root, 'Password: ', 2, 0)

Passwordtxt = Entry (root, show = '*')
Passwordtxt.grid (row = 2, column = 1)



Submitbtn = Button (root, text = 'Submit', command = Submit)
Submitbtn.grid (row = 3, column = 0, columnspan = 2)


root.mainloop()
