from tkinter import *

from Reservation import *
from Login import *
from WindowStyle import *

from PIL import Image, ImageTk
import tkinter.font as font


root = Tk()
root.title('Bermuda Cruise')
root.iconbitmap('icon.ico')


root.geometry('660x600')
root.resizable(False, False)



SetWindowBG (root)

frameInfo = LabelFrame (root, text = '', padx = 7, pady = 10)
frameHome = LabelFrame (root, text = '', padx = 7, pady = 10)

def Home():
    
    frameHome.grid(row = 1, column = 0, padx = 20, pady = 8)

    SetFrameBG (frameHome)

    lblInfo1 = Label (frameHome, text = '''With us, you experience a lavish lifestyle for your travel duration and get to experience all basic and extravagant amenities under your budget! From inbuilt swimming pool to comfortable rooms/suites which gives you home-ly vibes and from musical concerts twice a week to the most delightful dishes, we have everything that you’d want us to have, to provide, for you. ''', font = 'Times', wraplength = 275)
    SetLabelStyle_Home (lblInfo1)
    BasicFont(lblInfo1)

    lblInfo1.grid(row = 0, column = 0, padx = 10, pady = 10)



    image1 = Image.open('ship.jpg')

    resize_image1 = image1.resize((250, 150))
     
    img1 = ImageTk.PhotoImage(resize_image1)
    lblPhoto1 = Label(frameHome, image = img1)

    SetLabelStyle_Home (lblPhoto1)
    lblPhoto1.image = img1
    lblPhoto1.grid(row = 0, column = 1)
    


    image2 = Image.open('lounge.jpeg')

    resize_image2 = image2.resize((220, 125))
     
    img2 = ImageTk.PhotoImage(resize_image2)
    lblPhoto2 = Label(frameHome, image = img2)
    SetLabelStyle_Home(lblPhoto2)
    lblPhoto2.image = img2
    lblPhoto2.grid(row = 1, column = 0)


    lblInfo2 = Label(frameHome, text = '''Satisfying and serving guests with the best of everything and safety is our first priority. Choose Bermuda for your next vacay and cherish the memories life long! You are our Guest, You are our Family, You are served better, at Bermuda,''', font = 'Times', wraplength = 275)
    SetLabelStyle_Home (lblInfo2)
    BasicFont(lblInfo2)

    lblInfo2.grid(row = 1, column = 1, padx = 10, pady = 10)

    global lblPhoto3

    image3 = Image.open('collage.jpg')

    resize_image3 = image3.resize((600, 140))
     
    img3 = ImageTk.PhotoImage(resize_image3)
    lblPhoto3 = Label(root, image = img3)
    SetLabelStyle_Home(lblPhoto3)
    lblPhoto3.image = img3
    lblPhoto3.grid(row = 2, column = 0) 


def Info():

 
    frameInfo.grid(row = 1, column = 0, padx = 20, pady = 8)

    SetFrameBG (frameInfo)

    
    globeImage = Image.open('globe.png')

    resize_globeImage = globeImage.resize((75, 75))
     
    globeImg = ImageTk.PhotoImage(resize_globeImage)
    globePhoto = Label(frameInfo, image = globeImg)
    SetLabelStyle_Home (globePhoto)
    globePhoto.image = globeImg
    globePhoto.grid(row = 0, column = 0)

    lblBlank = Label (frameInfo, text = ' ')
    SetLabelStyle_Home (lblBlank)
    lblBlank.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    lblGlobe = Label (frameInfo, text = '''Cruises with Bermuda Cruise unlock some of the best and most iconic corners of the world. With us, there’s no limit on adventure — whether you dream of island-hopping to beautiful beaches in the Caribbean and the South Pacific, exploring national parks in Alaska and northern Europe or immersing yourself in Asia’s many exotic wonders. No matter where you wander, you’re in for a getaway unlike any other.''', anchor = 'w', wraplength = 465)
    SetLabelStyle_Home (lblGlobe)
    BasicFont(lblGlobe)
    lblGlobe.grid(row = 0, column = 2, padx = 10, pady = 10)




    seasonImage = Image.open('activity.png')

    resize_seasonImage = seasonImage.resize((75, 75))
     
    seasonImg = ImageTk.PhotoImage(resize_seasonImage)
    seasonPhoto = Label(frameInfo, image = seasonImg)
    SetLabelStyle_Home (seasonPhoto)
    seasonPhoto.image = seasonImg
    seasonPhoto.grid(row = 1, column = 0)

    lblBlank = Label (frameInfo, text = ' ')
    SetLabelStyle_Home (lblBlank)
    lblBlank.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    lblSeason = Label (frameInfo, text = '''Turn up the thrills like never before. Here, Bermuda Cruise puts adventure in the fast lane with shriek-inducing slides and rushing tides. Get your adrenaline fix zip lining across the sunny, blue sky. Have some fun at the casino where you can feel like you are in Las Vegas. Kids can enjoy their time at our gaming arcade. Max out your relaxation with endless ways to chill. Jam to DJ spun beats with a signature Coco Loco from the bustling swim-up bar at Oasis Lagoon. Wind down shore side in a private cabana at Chill Island.''', font = 'Times', wraplength = 465)
    SetLabelStyle_Home (lblSeason)
    BasicFont(lblSeason)

    lblSeason.grid(row = 1, column = 2, padx = 10, pady = 10)




    cuisineImage = Image.open('eat.png')

    resize_cuisineImage = cuisineImage.resize((75, 75))
     
    cuisineImg = ImageTk.PhotoImage(resize_cuisineImage)
    cuisinePhoto = Label(frameInfo, image = cuisineImg)
    SetLabelStyle_Home (cuisinePhoto)
    cuisinePhoto.image = cuisineImg
    cuisinePhoto.grid(row = 2, column = 0)

    lblBlank = Label (frameInfo, text = ' ')
    SetLabelStyle_Home (lblBlank)
    lblBlank.grid(row = 2, column = 1, padx = 10, pady = 10)
    
    lblCuisine = Label (frameInfo, text = '''Perfect Day at Bermuda Cruise offers loads of options to fuel up in between adventures. From mouth-watering Caribbean-style bites at Chill Grill to irresistible chicken sandwiches at Snack Shack, there’s plenty of complimentary delicious options everywhere you turn. Plus, discover even more ways to indulge at Coco Beach Club with elevated dishes like Bahamian lobster rolls, and grilled Caribbean grouper.''', font = 'Times', wraplength = 465)
    SetLabelStyle_Home (lblCuisine)
    BasicFont(lblCuisine)
    lblCuisine.grid(row = 2, column = 2, padx = 10, pady = 10)





    pricingImage = Image.open('hotel.png')

    resize_pricingImage = pricingImage.resize((75, 75))
     
    pricingImg = ImageTk.PhotoImage(resize_pricingImage)
    pricingPhoto = Label(frameInfo, image = pricingImg)
    SetLabelStyle_Home (pricingPhoto)
    pricingPhoto.image = pricingImg
    pricingPhoto.grid(row = 3, column = 0)

    lblBlank = Label (frameInfo, text = ' ')
    SetLabelStyle_Home (lblBlank)
    lblBlank.grid(row = 3, column = 1, padx = 10, pady = 10)
    
    lblPricing = Label (frameInfo, text = '''Our staterooms are designed with every type of guest in mind. Whether you’re sailing with your significant other, your family, a group of friends, or traveling solo. Our Interior staterooms include a wide array of amenities for your whole family to enjoy. Savor the seaside and snapshots of landscapes from shore to shore. Claim your slice of paradise with balcony views just outside your door. Enjoy expansive accommodations that take luxury to the next level.''', font = 'Times', wraplength = 465)
    SetLabelStyle_Home (lblPricing)
    BasicFont(lblPricing)

    lblPricing.grid(row = 3, column = 2, padx = 10, pady = 10)

def btnInfoClick():
    lblPhoto3.grid_remove()

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
    frameInfo.grid_remove()
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
txtSearch.insert(0, 'Reservation #')

txtSearch.bind('<FocusIn>', temp_text)

Searchbtn = Button (frameMenuBar, text = 'Search', command = btnSearchClick)
SetButtonStyle(Searchbtn)
Searchbtn.grid(row = 0, column = 5, padx = 5, pady = 10)



Home()

root.mainloop()
