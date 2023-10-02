from tkinter import *
from tkinter import messagebox
import mysql.connector


def CreateLabel(container, caption, r, c):
    label = Label (container, text = caption)
    label.grid (row = r, column = c)

def Clear():
    txtRegNo.delete(0, 'end')
    clickedRooms.set('')
    Breakfastbtn.set(None)
    txtActivity.delete(0, 'end')
    txtParticipants.delete(0, 'end')

def Save(RegNo, Rooms, Breakfast, Activity, Participants):
    dbconnection = mysql.connector.connect (host = 'localhost', username = 'root', password = 'admin', database = 'class_xii_project')
    dbcursor = dbconnection.cursor()


    InsertQuerySuites = "INSERT INTO Suites (RegNo, Number_of_Rooms, Breakfast, Activity, Participants) VALUES ('" + RegNo + "', '" + Rooms + "', '" + Breakfast + "', '" + Activity + "', '" + Participants + "')"

    #print(InsertQuerySuites)
    dbcursor.execute (InsertQuerySuites)
    dbconnection.commit()


    '''SelectQueryName = 'SELECT Name FROM Personal WHERE RegNo = ' + RegNo
    dbcursor.execute (InsertQuerySuites)
    Record = dbcursor.fetchall

    for i in Record:
        Name = i[0]

    
    
    dbconnection.commit()

    Msg = Name + ', your suite and activity has been confirmed.'
    
    messagebox.showinfo('Suite and Activity Confirmation', Msg)'''

    

def GetValues():
    RegNo = txtRegNo.get()
    Rooms = clickedRooms.get()
    Breakfast = Breakfastbtn.get()
    Activity = txtActivity.get()
    Participants = txtParticipants.get()


    Save(RegNo, Rooms, Breakfast, Activity, Participants)



def RoomsandActivities():

    global txtRegNo
    global clickedRooms
    global Breakfastbtn
    global txtActivity
    global txtParticipants

    
    root = Tk()
    root.title('Suites & Activities')


    frameBooking = LabelFrame (root, text = 'Suite Booking', padx = 7, pady = 10)
    frameBooking.grid(row = 0, column = 0, padx = 20, pady = 20)

    CreateLabel (frameBooking, 'Registration Number: ', 0, 0)
    txtRegNo = Entry (frameBooking)
    txtRegNo.grid (row = 0, column = 1)


    clickedRooms = StringVar()

    CreateLabel (frameBooking, 'Number of Rooms: ', 1, 0)
    dropRooms = OptionMenu (frameBooking, clickedRooms,
                            '1', '2', '3', '4')
    dropRooms.grid(row = 1, column = 1)

    Breakfastbtn = StringVar()
    #Breakfastbtn.set(None)


    CreateLabel (frameBooking, 'Breakfast? ', 2, 0)
    Ybtn = Radiobutton (frameBooking, text = 'Yes', variable = Breakfastbtn, value = 'Y')
    Ybtn.grid(row = 2, column = 1)

    Nbtn = Radiobutton (frameBooking, text = 'No', variable = Breakfastbtn, value = 'N')
    Nbtn.grid(row = 2, column = 2)

    

    frameActivities = LabelFrame (root, text = 'Activities Booking', padx = 7, pady = 10)
    frameActivities.grid(row = 1, column = 0, padx = 20, pady = 20)

    CreateLabel (frameActivities, 'Activity: ', 0, 0)
    txtActivity = Entry (frameActivities)
    txtActivity.grid (row = 0, column = 1)

    CreateLabel (frameActivities, 'Number of Participants: ', 1, 0)
    txtParticipants = Entry (frameActivities)
    txtParticipants.grid (row = 1, column = 1)



    frameAction = LabelFrame (root, padx = 7, pady = 10)
    frameAction.grid(row = 2, column = 0, padx = 20, pady = 20)
       
    btnClear = Button (frameAction, text = 'Clear', command = Clear)
    btnClear.grid(row = 0, column = 0)

        
    btnSubmit = Button (frameAction, text = 'Submit', command = GetValues)
    btnSubmit.grid(row = 0, column = 1)

    root.mainloop()
