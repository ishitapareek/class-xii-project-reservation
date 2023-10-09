from tkinter import *

from Reservation import *
from Login import *
from WindowStyle import *

from PIL import Image, ImageTk
import tkinter.font as font


root = Tk()
root.title('Bermuda Cruise')
root.iconbitmap("doodle.ico")


root.geometry('700x535')
root.resizable(False, False)



SetWindowBG (root)

frameInfo = LabelFrame (root, text = '', padx = 7, pady = 10)
frameHome = LabelFrame (root, text = '', padx = 7, pady = 10)

def Home():
    
    frameHome.grid(row = 1, column = 0, padx = 20, pady = 8)

    SetFrameBG (frameHome)

    lblInfo1 = Label (frameHome, text = '''Bermuda Cruise has been connecting travelers with the perfect cruise vacations since 1998. We pride ourselves in the best service possible,
    an accomplishment acknowledged by the most authoritative companies in the cruise industry.''', font = 'Times', wraplength = 305)
    SetLabelStyle_Home (lblInfo1)
    lblInfo1.grid(row = 0, column = 0, padx = 10, pady = 10)



    image1 = Image.open('background.jpg')

    resize_image1 = image1.resize((250, 163))
     
    img1 = ImageTk.PhotoImage(resize_image1)
    lblPhoto1 = Label(frameHome, image = img1)
    SetLabelStyle_Home (lblPhoto1)
    lblPhoto1.image = img1
    lblPhoto1.grid(row = 0, column = 1)



    image2 = Image.open('ship.jpg')

    resize_image2 = image2.resize((200, 163))
     
    img2 = ImageTk.PhotoImage(resize_image2)
    lblPhoto2 = Label(frameHome, image = img2)
    SetLabelStyle_Home(lblPhoto2)
    lblPhoto2.image = img2
    lblPhoto2.grid(row = 1, column = 0)


    lblInfo2 = Label(frameHome, text = '''m ipsum dolor sit amet, consectetur adipiscing
    elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua. Ut
    enim ad minim veniam, quis nostrud exer''', font = 'Times', wraplength = 305)
    SetLabelStyle_Home (lblInfo2)

    lblInfo2.grid(row = 1, column = 1, padx = 10, pady = 10)


def Info():

 
    frameInfo.grid(row = 1, column = 0, padx = 20, pady = 8)

    SetFrameBG (frameInfo)

    
    globeImage = Image.open('globe.jpg')

    resize_globeImage = globeImage.resize((75, 75))
     
    globeImg = ImageTk.PhotoImage(resize_globeImage)
    globePhoto = Label(frameInfo, image = globeImg)
    SetLabelStyle_Home (globePhoto)
    globePhoto.image = globeImg
    globePhoto.grid(row = 0, column = 0)

    lblBlank = Label (frameInfo, text = '  ')
    SetLabelStyle_Home (lblBlank)
    lblBlank.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    lblGlobe = Label (frameInfo, text = '''globe.''', font = 'Times', wraplength = 305)
    SetLabelStyle_Home (lblGlobe)
    lblGlobe.grid(row = 0, column = 2, padx = 10, pady = 10)




    seasonImage = Image.open('season.jpg')

    resize_seasonImage = seasonImage.resize((75, 75))
     
    seasonImg = ImageTk.PhotoImage(resize_seasonImage)
    seasonPhoto = Label(frameInfo, image = seasonImg)
    SetLabelStyle_Home (seasonPhoto)
    seasonPhoto.image = seasonImg
    seasonPhoto.grid(row = 1, column = 0)

    lblBlank = Label (frameInfo, text = '  ')
    SetLabelStyle_Home (lblBlank)
    lblBlank.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    lblSeason = Label (frameInfo, text = '''season.''', font = 'Times', wraplength = 305)
    SetLabelStyle_Home (lblSeason)
    lblSeason.grid(row = 1, column = 2, padx = 10, pady = 10)




    cuisineImage = Image.open('cuisine.jpg')

    resize_cuisineImage = cuisineImage.resize((75, 75))
     
    cuisineImg = ImageTk.PhotoImage(resize_cuisineImage)
    cuisinePhoto = Label(frameInfo, image = cuisineImg)
    SetLabelStyle_Home (cuisinePhoto)
    cuisinePhoto.image = cuisineImg
    cuisinePhoto.grid(row = 2, column = 0)

    lblBlank = Label (frameInfo, text = '  ')
    SetLabelStyle_Home (lblBlank)
    lblBlank.grid(row = 2, column = 1, padx = 10, pady = 10)
    
    lblCuisine = Label (frameInfo, text = '''cuisine.''', font = 'Times', wraplength = 305)
    SetLabelStyle_Home (lblCuisine)
    lblCuisine.grid(row = 2, column = 2, padx = 10, pady = 10)





    pricingImage = Image.open('pricing.jpg')

    resize_pricingImage = pricingImage.resize((75, 75))
     
    pricingImg = ImageTk.PhotoImage(resize_pricingImage)
    pricingPhoto = Label(frameInfo, image = pricingImg)
    SetLabelStyle_Home (pricingPhoto)
    pricingPhoto.image = pricingImg
    pricingPhoto.grid(row = 3, column = 0)

    lblBlank = Label (frameInfo, text = '  ')
    SetLabelStyle_Home (lblBlank)
    lblBlank.grid(row = 3, column = 1, padx = 10, pady = 10)
    
    lblPricing = Label (frameInfo, text = '''pricing.''', font = 'Times', wraplength = 305)
    SetLabelStyle_Home (lblPricing)
    lblPricing.grid(row = 3, column = 2, padx = 10, pady = 10)

def btnInfoClick():
    frameHome.grid_remove()
    Info()

def btnReservationClick():
    NewReservation(root) #Function in Reservation.py

def btnLoginClick():
    LoginScreen(root) #Function in Login.py


def temp_text(e):
   txtSearch.delete(0,"end")

def btnSearchClick():
    SearchReservation(root, txtSearch.get()) #Function in Reservation.py

def btnHomeClick():
    Home()
    



frameMenuBar = LabelFrame(root, text = '', padx = 5)
frameMenuBar.grid(row = 0, column = 0, padx = 20, pady = 20)

SetFrameBG (frameMenuBar)


Homebtn = Button (frameMenuBar, text = 'Home', command = btnHomeClick)
SetButtonStyle(Homebtn)
Homebtn.grid (row = 0, column = 0, padx = 5, pady = 10)

Informationbtn = Button (frameMenuBar, text = 'Information', command = btnInfoClick)
SetButtonStyle(Informationbtn)
Informationbtn.grid (row = 0, column = 1, padx = 5, pady = 10)


Reservationbtn = Button (frameMenuBar, text = 'Make a Reservation', command = btnReservationClick)
SetButtonStyle(Reservationbtn)
Reservationbtn.grid (row = 0, column = 2, padx = 5, pady = 10)



Loginbtn = Button (frameMenuBar, text = 'Employee Login', command = btnLoginClick)
SetButtonStyle(Loginbtn)
Loginbtn.grid (row = 0, column = 3, padx = 5, pady = 10)


txtSearch = Entry (frameMenuBar, width = 15)
txtSearch.grid(row = 0, column = 4, padx = 25, pady = 20)
txtSearch.insert(0, 'Registeration #')

txtSearch.bind('<FocusIn>', temp_text)

Searchbtn = Button (frameMenuBar, text = 'Search', command = btnSearchClick)
SetButtonStyle(Searchbtn)
Searchbtn.grid(row = 0, column = 5, padx = 5, pady = 10)



Home()

root.mainloop()

