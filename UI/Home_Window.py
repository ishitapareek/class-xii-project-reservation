from tkinter import *

from Reservation import *
from Login import *
from WindowStyle import *

from PIL import Image, ImageTk
import tkinter.font as font




root = Tk()
root.title('Bermuda Cruise')
root.geometry('700x535')
root.resizable(False, False)


SetWindowBG (root)


ButtonFont = font.Font(family = 'californian fb', size = 10, weight = 'bold')

def Open_Information():
    pass

def Open_Reservation():
    NewReservation(root) #Function in Reservation.py

def Open_Login():
    LoginScreen(root) #Function in Login.py


def temp_text(e):
   txtSearch.delete(0,"end")

def Search():
    SearchReservation(root, txtSearch.get()) #Function in Reservation.py


frameMenuBar = LabelFrame(root, text = '', padx = 5)
frameMenuBar.grid(row = 0, column = 0, padx = 20, pady = 20)

SetFrameBG (frameMenuBar)


Informationbtn = Button (frameMenuBar, text = 'Information', command = Open_Information)
SetButtonStyle(Informationbtn)
Informationbtn.grid (row = 0, column = 0, padx = 5, pady = 10)


Reservationbtn = Button (frameMenuBar, text = 'Make a Reservation', command = Open_Reservation)
SetButtonStyle(Reservationbtn)
Reservationbtn.grid (row = 0, column = 1, padx = 5, pady = 10)



Loginbtn = Button (frameMenuBar, text = 'Employee Login', command = Open_Login)
SetButtonStyle(Loginbtn)
Loginbtn.grid (row = 0, column = 2, padx = 5, pady = 10)


txtSearch = Entry (frameMenuBar, width = 30)
txtSearch.grid(row = 0, column = 3, padx = 25, pady = 20)
txtSearch.insert(0, 'Enter your registeration number: ')
SetLabelStyle_Home(txtSearch)

txtSearch.bind('<FocusIn>', temp_text)

Searchbtn = Button (frameMenuBar, text = 'Search', command = Search)
SetButtonStyle(Searchbtn)
Searchbtn.grid(row = 0, column = 4, padx = 5, pady = 10)





framePhotos = LabelFrame (root, text = '', padx = 7, pady = 10)
framePhotos.grid(row = 1, column = 0, padx = 20, pady = 8)

SetFrameBG (framePhotos)

txtInfo1 = Label (framePhotos, text = '''Bermuda Cruise has been connecting travelers with the perfect cruise vacations since 1998. We pride ourselves in the best service possible,
an accomplishment acknowledged by the most authoritative companies in the cruise industry.''', font = 'Times', wraplength = 305)
SetLabelStyle_Home (txtInfo1)
txtInfo1.grid(row = 0, column = 0, padx = 10, pady = 10)



image1 = Image.open('background.jpg')

resize_image1 = image1.resize((250, 163))
 
img1 = ImageTk.PhotoImage(resize_image1)
lblPhoto1 = Label(framePhotos, image = img1)
SetLabelStyle_Home (lblPhoto1)
lblPhoto1.image = img1
lblPhoto1.grid(row = 0, column = 1)



image2 = Image.open('ship.jpg')

resize_image2 = image2.resize((200, 163))
 
img2 = ImageTk.PhotoImage(resize_image2)
lblPhoto2 = Label(framePhotos, image = img2)
SetLabelStyle_Home(lblPhoto2)
lblPhoto2.image = img2
lblPhoto2.grid(row = 1, column = 0)


txtInfo2 = Label(framePhotos, text = '''m ipsum dolor sit amet, consectetur adipiscing
elit, sed do eiusmod tempor incididunt ut
labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exer''', font = 'Times', wraplength = 305)
SetLabelStyle_Home (txtInfo2)

txtInfo2.grid(row = 1, column = 1, padx = 10, pady = 10)


root.mainloop()
