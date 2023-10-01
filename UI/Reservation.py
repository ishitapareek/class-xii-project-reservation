from tkinter import *
from tkinter import messagebox
import mysql.connector

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

    messagebox.askquestion("Are You Sure?", "Do you want to confirm your reservation?")

    Msg = Name + ', your reservation has been confirmed.' + '\n \n ' + 'Your registration number is: ' + RegNo
    messagebox.showinfo('Confirmation', Msg)


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


def DesignWindow(Pwindow, Name, Address, DOB, Email, Mobile, Dates, Days, Boarding, Leaving, Members):
    resWindow = Toplevel (Pwindow)

    resWindow.title ('Reservation')

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

    lblBoarding = Label (frameReservationInfo, text = 'Boarding Point: ')
    lblBoarding.grid(row = 1, column = 0)

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


    frameAction = LabelFrame (resWindow, padx = 7, pady = 10)
    frameAction.grid(row = 2, column = 0, padx = 20, pady = 20)
       
    btnClear = Button (frameAction, text = 'Clear', command = Clear)
    btnClear.grid(row = 0, column = 0)

    
    
    btnSubmit = Button (frameAction, text = 'Submit', command = GetValues)
    btnSubmit.grid(row = 0, column = 1)

    resWindow.mainloop()

    
def NewReservation(Pwindow):
    DesignWindow(Pwindow, "", "", "", "", "", "", "", "", "", "")
    

def SearchReservation(Pwindow, RegNo):
    
    dbconnection = mysql.connector.connect (host = 'localhost', username = 'root', password = 'admin', database = 'class_xii_project')
    dbcursor = dbconnection.cursor()

    strRegNo = str(RegNo)

    SelectQuery = 'SELECT * FROM Personal AS P, Reservation AS R WHERE P.RegNo = R.RegNo AND P.RegNo = ' + strRegNo
    dbcursor.execute (SelectQuery)

    
    Records = dbcursor.fetchall()

    for i in Records:
        Name = i[0]
        Address = i[1]
        DOB = i[2]
        Email = i[3]
        Mobile = i[4]
        RegNo = i[5]
        Dates = i[7]
        Days = i[8]
        Boarding = i[9]
        Leaving = i[10]
        Members = i[11]

    DesignWindow(Pwindow, Name, Address, DOB, Email, Mobile, Dates, Days, Boarding, Leaving, Members)
