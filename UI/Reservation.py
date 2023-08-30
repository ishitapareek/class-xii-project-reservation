from tkinter import *
from tkinter import messagebox


root = Tk ()

root.title ('Reservation')

def button_clear():
    a = 10
    return a

    
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
txtMoblie = Entry (framePersonalInfo)
txtMoblie.grid (row = 1, column = 1)


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
   
btnClear = Button (frameAction, text = 'Clear', command = button_clear)
btnClear.grid(row = 0, column = 0)

def button_submit():
    Name = txtName.get()
    DOB = txtDOB.get()
    PhoneNo = txtMoblie.get()
    Email = txtEmail.get()
    Address = txtAddress.get()

    Dates = txtDates.get()
    Days = txtDays.get()
    #Boarding = dropBoarding.get()
    #Leaving = dropLeaving.get()
    Members = txtMembers.get()
    
    Personal = Name + '\n' + DOB + '\n' + PhoneNo + '\n' + Email + '\n' + Address + '\n'

    Reservation = Dates + '\n' + Days + '\n' + Members
    
    Msg = Personal + Reservation
    messagebox.showinfo("Confirmation", Msg)
    
    
btnSubmit = Button (frameAction, text = 'Submit', command = button_submit)
btnSubmit.grid(row = 0, column = 1)


'''messagebox.showinfo("showinfo", "Information")
messagebox.showwarning("showwarning", "Warning")
messagebox.showerror("showerror", "Error")
messagebox.askquestion("askquestion", "Are you sure?") 
messagebox.askokcancel("askokcancel", "Want to continue?")
messagebox.askyesno("askyesno", "Find the value?")
messagebox.askretrycancel("askretrycancel", "Try again?")'''



root.mainloop()
