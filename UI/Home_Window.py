from tkinter import *

from Reservation import *
from Login import *
from Rooms_and_Activities import *
from PIL import Image, ImageTk



root = Tk()
root.title(':)')
root.geometry('800x575')
root.resizable(False, False)



def Open_AboutUs():
    pass

def Open_Reservation():
    NewReservation(root) #Function in Reservation.py

def Open_RoomActivity():
    RoomsandActivities() #Function in Rooms_and_Activities.py


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

RoomActivitybtn = Button (frameMenuBar, text = 'Suite and Activity Booking', command = Open_RoomActivity)
RoomActivitybtn.grid (row = 0, column = 2, padx = 5, pady = 10)

Loginbtn = Button (frameMenuBar, text = 'Employee Login', command = Open_Login)
Loginbtn.grid (row = 0, column = 3, padx = 5, pady = 10)

txtSearch = Entry (frameMenuBar, width = 30)
txtSearch.grid(row = 0, column = 4, padx = 25, pady = 20)
txtSearch.insert(0, 'Enter your reservation number: ')
txtSearch.bind('<FocusIn>', temp_text)

Searchbtn = Button (frameMenuBar, text = 'Search', command = Search)
Searchbtn.grid(row = 0, column = 5, padx = 5, pady = 10)



framePhotos = LabelFrame (root, text = '', padx = 7, pady = 10)
framePhotos.grid(row = 1, column = 0, padx = 20, pady = 20)

txtInfo = Label (framePhotos, text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse c',font="helvetica 14", wraplength = 200)
txtInfo.grid(row = 0, column = 0, padx = 20, pady = 20)



image1 = Image.open('background.jpg')

resize_image1 = image1.resize((500, 325))
 
img1 = ImageTk.PhotoImage(resize_image1)
lblPhoto1 = Label(framePhotos, image = img1)
lblPhoto1.image = img1
lblPhoto1.grid(row = 0, column = 1)



'''image2 = Image.open('boat.jpg')

resize_image2 = image2.resize((380, 210))
 
img2 = ImageTk.PhotoImage(resize_image2)
lblPhoto2 = Label(framePhotos, image = img2)
lblPhoto2.image = img2
lblPhoto2.grid(row = 1, column = 0)'''




root.mainloop()
