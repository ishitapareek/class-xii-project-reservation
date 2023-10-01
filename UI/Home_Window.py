from tkinter import *
import mysql.connector

from Reservation import *
from Login import *

Pwindow = Tk()
Pwindow.title('Home')



def CreateLabel(container, caption, r, c):
    label = Label (container, text = caption)
    label.grid (row = r, column = c)

def Open_AboutUs():
    pass

def Reservation():
    NewReservation(Pwindow) #Function in Reservation.py
    
def Open_Login(): 
    LoginScreen() #Function in Login.py

def Search():
    SearchReservation(Pwindow, Searchtxt.get()) 

   

Aboutbtn = Button (Pwindow, text = 'About Us', command = Open_AboutUs)
Aboutbtn.grid (row = 0, column = 0)

Reservationbtn = Button (Pwindow, text = 'Reservation', command = Reservation)
Reservationbtn.grid (row = 0, column = 1)

Loginbtn = Button (Pwindow, text = 'Employee Login', command = Open_Login)
Loginbtn.grid (row = 0, column = 2)

Searchtxt = Entry(Pwindow)
Searchtxt.grid(row = 1, column = 0)

Searchbtn = Button (Pwindow, text = 'Search', command = Search)
Searchbtn.grid (row = 1, column = 1)

Pwindow.mainloop()
