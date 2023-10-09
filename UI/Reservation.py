from tkinter import *
from tkinter import messagebox
import mysql.connector

from Rooms_and_Activities import *

def Clear():
    txtName.delete(0, 'end')
    txtDOB.delete(0, 'end')
    txtMobile.delete(0, 'end')
    txtEmail.delete(0, 'end')
    txtAddress.delete(0, 'end')
    
    txtDates.delete(0, 'end')
    txtDays.delete(0, 'end')
    clickedBoarding.set('')
    clickedLeaving.set('')
    txtMembers.delete(0, 'end')


def Save(Name, DOB, PhoneNo, Email, Address, Dates, Days, Boarding, Leaving, Members):
    dbconnection = mysql.connector.connect (host = 'localhost', username = 'root', password = 'admin', database = 'class_xii_project')
    dbcursor = dbconnection.cursor()
    
    InsertQueryPersonal = "insert into personal (Name, DOB, Mobile, Email, Address) values ('" + Name + "', '" + DOB + "', '" + PhoneNo + "', '" + Email + "', '" + Address + "')"
    dbcursor.execute (InsertQueryPersonal)
    RegNo = str(dbcursor.lastrowid)

    InsertQueryReservation = "insert into Reservation values ('" + str(dbcursor.lastrowid) + "', '" + Dates + "', '" + Days + "', '" + Boarding + "', '" + Leaving + "', '" + Members + "')"
    dbcursor.execute (InsertQueryReservation)
    
    dbconnection.commit()


    Msg = Name + ', your reservation has been confirmed.' + '\n \n ' + 'Your registration number is: ' + RegNo
    messagebox.showinfo('Confirmation', Msg)

    RoomsandActivities(resWindow, RegNo, Name)

    dbconnection.close()


def GetValues():
    Name = txtName.get()
    DOB = txtDOB.get()
    PhoneNo = txtMobile.get()
    Email = txtEmail.get()
    Address = txtAddress.get()

    Dates = txtDates.get()
    Days = txtDays.get()
    Boarding = clickedBoarding.get()
    Leaving = clickedLeaving.get()
    Members = txtMembers.get()
    Save(Name, DOB, PhoneNo, Email, Address, Dates, Days, Boarding, Leaving, Members)
        
    
def CreateLabel(container, caption, r, c):
    label = Label (container, text = caption)
    label.grid (row = r, column = c)

def MoreDetailsFrames(SuiteType, Activity, Participants, RoomNumber, Amount):

    frameMoreDetails = LabelFrame(resWindow, text = 'More Details', padx = 7, pady = 10)
    frameMoreDetails.grid (row = 2, column = 0, padx = 20, pady = 20)

    CreateLabel (frameMoreDetails, 'Suite: ', 0, 0)
    CreateLabel (frameMoreDetails, SuiteType, 0, 1)

    CreateLabel (frameMoreDetails, 'Activity: ', 1, 0)
    CreateLabel (frameMoreDetails, Activity, 1, 1)


    CreateLabel (frameMoreDetails, 'Participants: ', 2, 0)
    CreateLabel (frameMoreDetails, Participants, 2, 1)
    
    CreateLabel (frameMoreDetails, 'Room Number: ', 3, 0)
    CreateLabel (frameMoreDetails, RoomNumber, 3, 1)
    
    CreateLabel (frameMoreDetails, 'Amount: ', 4, 0)
    CreateLabel (frameMoreDetails, Amount, 4, 1)

def PersonalReservationFrames(Pwindow, Name, Address, DOB, Email, Mobile, Dates, Days, Boarding, Leaving, Members):
    global resWindow
    
    resWindow = Toplevel(Pwindow)

    resWindow.title ('Reservation')
    resWindow.geometry('600x400')
    resWindow.resizable(False, False)


    framePersonalInfo = LabelFrame(resWindow, text = 'Personal Info', padx = 7, pady = 10)
    framePersonalInfo.grid(row = 0, column = 0, padx = 20, pady = 20)

    global txtName
    global txtDOB
    global txtMobile
    global txtEmail
    global txtAddress
    global txtDates
    global txtDays
    global clickedBoarding
    global clickedLeaving
    global txtMembers
    global clickedActivity

    
    CreateLabel (framePersonalInfo, 'Name: ', 0, 0)
    txtName = Entry(framePersonalInfo)
    txtName.grid (row = 0, column = 1)
    txtName.insert(0, Name)


    CreateLabel (framePersonalInfo, 'Date of Birth: ', 0, 2)
    txtDOB = Entry (framePersonalInfo)
    txtDOB.grid (row = 0, column = 3)
    txtDOB.insert(0, DOB)



    CreateLabel (framePersonalInfo, 'Phone Number: ', 1, 0)
    txtMobile = Entry (framePersonalInfo)
    txtMobile.grid (row = 1, column = 1)
    txtMobile.insert(0, Mobile)

    

    CreateLabel (framePersonalInfo, 'Email: ', 1, 2)
    txtEmail = Entry (framePersonalInfo)
    txtEmail.grid (row = 1, column = 3)
    txtEmail.insert(0, Email)



    CreateLabel (framePersonalInfo, 'Address: ', 2, 0)
    txtAddress = Entry (framePersonalInfo)
    txtAddress.grid (row = 2, column = 1)
    txtAddress.insert(0, Address)

        
    frameReservationInfo = LabelFrame (resWindow, text = 'Reservation', padx = 7, pady = 10)
    frameReservationInfo.grid(row = 1, column = 0, padx = 20, pady = 20)

    CreateLabel (frameReservationInfo, 'Dates: ', 0, 0)

    txtDates = Entry (frameReservationInfo)
    txtDates.grid (row = 0, column = 1)
    txtDates.insert(0, Dates)

    CreateLabel (frameReservationInfo, 'Days: ', 0, 2)
    txtDays = Entry (frameReservationInfo)
    txtDays.grid (row = 0, column = 3)
    txtDays.insert(0, Days)



    clickedBoarding = StringVar()
    clickedLeaving = StringVar()

    CreateLabel(frameReservationInfo, 'Boarding Point: ', 1, 0)

    dropBoarding = OptionMenu (frameReservationInfo, clickedBoarding, 'Boarding 1', 'Boarding 2', 'Boarding 3')
    dropBoarding.grid(row = 1, column = 1)
    clickedBoarding.set(Boarding)


    lblLeaving = Label (frameReservationInfo, text = 'Leaving Point: ')
    lblLeaving.grid(row = 1, column = 2)

    dropLeaving = OptionMenu (frameReservationInfo, clickedLeaving, 'Leaving 1', 'Leaving 2', 'Leaving 3')
    dropLeaving.grid(row = 1, column = 3)
    clickedLeaving.set(Leaving)


    CreateLabel (frameReservationInfo, 'Number of Group Members: ', 2, 0)
    txtMembers = Entry (frameReservationInfo)
    txtMembers.grid (row = 2, column = 1)
    txtMembers.insert(0, Members)

    
def NewReservation(Pwindow):
    PersonalReservationFrames(Pwindow, "", "", "", "", "", "", "", "", "", "")

    frameAction = LabelFrame (resWindow, padx = 7, pady = 10)
    frameAction.grid(row = 2, column = 0, padx = 20, pady = 20)
       
    btnClear = Button (frameAction, text = 'Clear', command = Clear)
    btnClear.grid(row = 0, column = 0)
    
    btnSubmit = Button (frameAction, text = 'Submit', command = GetValues)
    btnSubmit.grid(row = 0, column = 1)


def SearchReservation(Pwindow, RegNo):
    
    dbconnection = mysql.connector.connect (host = 'localhost', username = 'root', password = 'admin', database = 'class_xii_project')
    dbcursor = dbconnection.cursor()

    SelectQuery = '''SELECT PER.*, Dates, Days, Boarding_Point, Leaving_Point, Members, Suite_Type, Activity, Participants, Room_Number, Amount 
                    FROM reservation RES
                    NATURAL JOIN personal PER
                    NATURAL JOIN suite_and_activity SA
                    NATURAL JOIN payment_info PAY
                    WHERE RES.RegNo = ''' + str(RegNo)

    dbcursor.execute (SelectQuery)
    Records = dbcursor.fetchall()

    for i in Records:
        Name = i[0]
        Address = i[1]
        DOB = i[2]
        Email = i[3]
        Mobile = i[4]
        RegNo = i[5]
        Dates = i[6]
        Days = i[7]
        Boarding = i[8]
        Leaving = i[9]
        Members = i[10]
        SuiteType = i[11]
        Activity = i[12]
        Participants = i[13]
        RoomNumber = i[14]
        Amount = i[15]

    PersonalReservationFrames(Pwindow, Name, Address, DOB, Email, Mobile, Dates, Days, Boarding, Leaving, Members)

    MoreDetailsFrames(SuiteType, Activity, Participants, RoomNumber, Amount)

    resWindow.mainloop()
