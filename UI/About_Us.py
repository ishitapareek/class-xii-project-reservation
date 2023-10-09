from tkinter import *

root = Tk()
root.title('About Us')
root.geometry('500x500')

def CreateLabel(container, caption, a, r, c):
    label = Label (container, text = caption, anchor = a)
    label.grid (row = r, column = c)


CreateLabel (root, '''
   ABOUT US''', NW, 0, 0)

CreateLabel (root, '''
   WAYS TO THRILL''', CENTER, 1, 0)



CreateLabel (root, '''Turn up the thrills like never before! Here,
                      Bermuda Cruise puts adventure in the fast lane with shriek-inducing slides
                      and rushing tides.  Have some fun at the casino where you can feel like
                      you are in Las Vegas. Kids can enjoy their
                      time at our gaming arcade. Max out your relaxation with endless
                      ways to chill.''', CENTER, 2, 0)

