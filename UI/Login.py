from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')


def CorrectLogin():
    messagebox.showinfo('Login','Correct Login.')

def IncorrectLogin():
    messagebox.showinfo('Login','Incorrect Login. \n Check username/password.')


def CreateLabel(container, caption, r, c):
    label = Label (container, text = caption)
    label.grid (row = r, column = c)


def Enter():
    Username = txtUsername.get()
    Password = txtPassword.get()

    if Username == 'admin' and Password == 'xyz':
        btnLogin = Button(root, text = 'Login', command = CorrectLogin)

    else:
        btnLogin = Button(root, text = 'Login', command = IncorrectLogin)

    btnLogin.grid(row = 2, column = 0)


frameLoginInfo = LabelFrame (root, text = 'Login Info', padx = 7, pady = 10)

CreateLabel (root, 'Username: ', 0, 0)

txtUsername = Entry (root, bd = 5)
txtUsername.grid (row = 0, column = 1, padx = 15, pady = 5)


CreateLabel (root, 'Password: ', 1, 0)

txtPassword = Entry (root, bd = 5)
txtPassword.grid (row = 1, column = 1, padx = 15, pady = 20, columnspan = 3)


frameButton = LabelFrame (root, padx = 7, pady = 10)

Enter()


'''link = Label(root, text="www.tutorialspoint.com", font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.grid(row = 3, column = 0)
link.bind("<Button-1>", lambda e: callback("http://www.tutorialspoint.com"))'''

root.mainloop()
