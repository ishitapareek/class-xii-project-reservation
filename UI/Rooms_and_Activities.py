from tkinter import *
from tkinter import messagebox
import mysql.connector

from Payment import *

from WindowStyle import *
import tkinter.font as font


def CreateLabel(container, caption, r, c):
    label = Label (container, text = caption)
    SetLabelStyle_Input(label)
    label.grid (row = r, column = c)

def Clear():
    clickedRooms.set('')
    clickedActivity.set('')
    txtParticipants.delete(0, 'end')

def Save(Name, RegNo):

    Rooms = clickedRooms.get()
    Activity = clickedActivity.get()
    Participants = txtParticipants.get()

    dbconnection = mysql.connector.connect (host = 'localhost', username = 'root', password = 'admin', database = 'class_xii_project')
    dbcursor = dbconnection.cursor()

    InsertQuerySuites = "INSERT INTO Suite_and_Activity (RegNo, Suite_Type, Activity, Participants) VALUES ('" + str(RegNo) + "', '" + Rooms + "', '" + Activity    + "', '" + Participants + "')"

    #print(InsertQuerySuites)
    dbcursor.execute (InsertQuerySuites)
    dbconnection.commit()
    RoomNo = str(dbcursor.lastrowid)

    Msg = Name + ', your suite and activity has been confirmed.' + '\n \n ' + 'Your room number is: ' + RoomNo
    messagebox.showinfo('Confirmation', Msg)
    
    dbconnection.close()
    Layout(root, Name, RegNo)

def RoomsandActivities(Pwindow, RegNo, Name):
        
    global root
    global clickedRooms
    global clickedActivity
    global txtParticipants
    
    root = Toplevel(Pwindow)
    root.title('Bermuda Cruise - Suites & Activity')
    SetWindowBG(root)
    root.iconbitmap('icon.ico')

    frameBooking = LabelFrame (root, text = 'Suite and Activity Booking', font = 'Times', padx = 7, pady = 10)
    SetFrameBG(frameBooking)
    frameBooking.grid(row = 0, column = 0, padx = 20, pady = 20)

    CreateLabel (frameBooking, 'Registration Number: ', 0, 0)
    CreateLabel (frameBooking, RegNo, 0, 1)
   
    CreateLabel (frameBooking, 'Name: ', 0, 2)
    CreateLabel (frameBooking, Name, 0, 3)
    
    clickedRooms = StringVar()
    clickedRooms.set('')
       
    CreateLabel (frameBooking, 'Type of Suite : ', 1, 0)
    dropRooms = OptionMenu (frameBooking, clickedRooms, 'Interior', 'Ocean View', 'Balcony', 'Presidential')
    DropStyle(dropRooms)
    dropRooms.grid(row = 1, column = 1)

    clickedActivity = StringVar()
    CreateLabel (frameBooking, 'Activity: ', 2, 0)
    dropActivity = OptionMenu (frameBooking, clickedActivity, 'Golf', 'Surfing', 'Rock Climbing', 'Zip Lining', 'Parachuting')
    DropStyle(dropActivity)
    dropActivity.grid (row = 2, column = 1)

    CreateLabel (frameBooking, 'Number of Participants: ', 2, 2)
    txtParticipants = Entry (frameBooking)
    txtParticipants.grid (row = 2, column = 3)

    frameAction = LabelFrame (root, padx = 7, pady = 10)
    SetFrameBG(frameAction)
    frameAction.grid(row = 1, column = 0, padx = 20, pady = 20)
       
    btnClear = Button (frameAction, text = 'Clear', command = Clear)
    SetButtonStyle(btnClear)
    btnClear.grid(row = 0, column = 0)
        
    btnSubmit = Button (frameAction, text = 'Submit', command = lambda: Save (Name, RegNo))
    SetButtonStyle(btnSubmit)
    btnSubmit.grid(row = 0, column = 1)

    root.mainloop()
