from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk ()

root.title ('Reservation')

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



framePersonalInfo = LabelFrame(root, text = 'Personal Info', padx = 7, pady = 10)
framePersonalInfo.grid(row = 0, column = 0, padx = 20, pady = 20)

CreateLabel (framePersonalInfo, 'Name: ', 0, 0)
txtName = Entry (framePersonalInfo)
txtName.grid (row = 0, column = 1)


CreateLabel (framePersonalInfo, 'Date of Birth: ', 0, 2)
txtDOB = Entry (framePersonalInfo)
txtDOB.grid (row = 0, column = 3)


CreateLabel (framePersonalInfo, 'Phone Number: ', 1, 0)
txtMobile = Entry (framePersonalInfo)
txtMobile.grid (row = 1, column = 1)


CreateLabel (framePersonalInfo, 'Email: ', 1, 2)
txtEmail = Entry (framePersonalInfo)
txtEmail.grid (row = 1, column = 3)


CreateLabel (framePersonalInfo, 'Address: ', 2, 0)
txtAddress = Entry (framePersonalInfo)
txtAddress.grid (row = 2, column = 1)


frameReservationInfo = LabelFrame (root, text = 'Reservation', padx = 7, pady = 10)
frameReservationInfo.grid(row = 1, column = 0, padx = 20, pady = 20)

CreateLabel (frameReservationInfo, 'Dates: ', 0, 0)

txtDates = Entry (frameReservationInfo)
txtDates.grid (row = 0, column = 1)

CreateLabel (frameReservationInfo, 'Days: ', 0, 2)
txtDays = Entry (frameReservationInfo)
txtDays.grid (row = 0, column = 3)


clickedBoarding = StringVar()
clickedLeaving = StringVar()

lblBoarding = Label (frameReservationInfo, text = 'Boarding Point: ')
lblBoarding.grid(row = 1, column = 0)

dropBoarding = OptionMenu (frameReservationInfo, clickedBoarding, 'Boarding 1', 'Boarding 2', 'Boarding 3')
dropBoarding.grid(row = 1, column = 1)

lblLeaving = Label (frameReservationInfo, text = 'Leaving Point: ')
lblLeaving.grid(row = 1, column = 2)

dropLeaving = OptionMenu (frameReservationInfo, clickedLeaving, 'Leaving 1', 'Leaving 2', 'Leaving 3')
dropLeaving.grid(row = 1, column = 3)


CreateLabel (frameReservationInfo, 'Number of Group Members: ', 2, 0)
txtMembers = Entry (frameReservationInfo)
txtMembers.grid (row = 2, column = 1)

frameAction = LabelFrame (root, padx = 7, pady = 10)
frameAction.grid(row = 2, column = 0, padx = 20, pady = 20)
   
btnClear = Button (frameAction, text = 'Clear', command = Clear)
btnClear.grid(row = 0, column = 0)

    
    
btnSubmit = Button (frameAction, text = 'Submit', command = GetValues)
btnSubmit.grid(row = 0, column = 1)


root.mainloop()
