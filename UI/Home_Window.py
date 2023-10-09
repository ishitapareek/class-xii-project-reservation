from tkinter import *

from Reservation import *
from Login import *
from PIL import Image, ImageTk



root = Tk()
root.title(':)')
root.geometry('800x575')
root.resizable(False, False)



def Open_AboutUs():
    pass

def Open_Reservation():
    NewReservation(root) #Function in Reservation.py

def Open_Login():
    LoginScreen() #Function in Login.py


def temp_text(e):
   txtSearch.delete(0,"end")

def Search():
    SearchReservation(root, txtSearch.get()) #Function in Reservation.py


frameMenuBar = LabelFrame(root, text = '', padx = 7, pady = 10)
frameMenuBar.grid(row = 0, column = 0, padx = 20, pady = 20)


#Title = Text (frameMenuBar, height = 3000)
#Title.grid(row = 0, column = 0, padx = 20, pady = 20)

Aboutbtn = Button (frameMenuBar, text = 'About Us', command = Open_AboutUs)
Aboutbtn.grid (row = 0, column = 0, padx = 5, pady = 10)

Reservationbtn = Button (frameMenuBar, text = 'Make a Reservation', command = Open_Reservation)
Reservationbtn.grid (row = 0, column = 1, padx = 5, pady = 10)

Loginbtn = Button (frameMenuBar, text = 'Employee Login', command = Open_Login)
Loginbtn.grid (row = 0, column = 2, padx = 5, pady = 10)

txtSearch = Entry (frameMenuBar, width = 30)
txtSearch.grid(row = 0, column = 3, padx = 25, pady = 20)
txtSearch.insert(0, 'Enter your reservation number: ')
txtSearch.bind('<FocusIn>', temp_text)

Searchbtn = Button (frameMenuBar, text = 'Search', command = Search)
Searchbtn.grid(row = 0, column = 4, padx = 5, pady = 10)



framePhotos = LabelFrame (root, text = '', padx = 7, pady = 10)
framePhotos.grid(row = 1, column = 0, padx = 20, pady = 20)

txtInfo = Label (framePhotos, text = 'Lorem ipsum dolor sit ameta. Ut enim ad minim veniam', font = 'helvetica 14', wraplength = 60)
txtInfo.grid(row = 0, column = 0, padx = 20, pady = 20)



image1 = Image.open('background.jpg')

resize_image1 = image1.resize((250, 163))
 
img1 = ImageTk.PhotoImage(resize_image1)
lblPhoto1 = Label(framePhotos, image = img1)
lblPhoto1.image = img1
lblPhoto1.grid(row = 0, column = 1)

root.mainloop()
