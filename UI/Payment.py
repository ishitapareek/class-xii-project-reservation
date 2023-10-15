from tkinter import *
from tkinter import messagebox
import mysql.connector


from WindowStyle import *
import tkinter.font as font


def Pricing(RegNo):

    dbconnection = mysql.connector.connect(host = 'localhost', username = 'root', password = 'admin', database = 'class_xii_project')
    dbcursor = dbconnection.cursor()

    SelectQuery = 'SELECT Reservation.RegNo, Days, Members, Suite_Type, Activity, Participants from Reservation, Suite_and_Activity where Reservation.RegNo = ' + str(RegNo) + ' and Suite_and_Activity.RegNo = ' + str(RegNo)
    
    
    dbcursor.execute (SelectQuery)
    myrecords = dbcursor.fetchall()


    
    global TicketCost
    global SuiteCost
    global ActivityCost
    global TotalCost

    global Days
    global Members
    global SuiteType
    global Activity
    global Participants


    for i in myrecords:
        if str(RegNo) == str(i[0]):
            Days = i[1]
            Members = i[2]
            SuiteType = i[3]
            Activity = i[4]
            Participants = i[5]

    TicketCost = 30000 * int(Members)


    SuiteCost = 0

    if SuiteType == 'Interior':
        SuiteCost = 1000 * int(Days)

    elif SuiteType == 'Ocean View':
        SuiteCost = 1200 * int(Days)

    elif SuiteType == 'Balcony':
        SuiteCost = 1500 * int(Days)
        
    elif SuiteType == 'Presidential':
        SuiteCost = 1700 * int(Days)

    ActivityCost = 0

    if Activity == 'Golf':
        ActivityCost = 500 * int(Participants)

    elif Activity == 'Surfing':
        ActivityCost = 300 * int(Participants)

    elif Activity == 'Rock Climbing':
        ActivityCost = 400 * int(Participants)

    elif Activity == 'Zip Lining':
        ActivityCost = 700 * int(Participants)

    elif Activity == 'Parachuting':
        ActivityCost = 900 * int(Participants)

    TotalCost = TicketCost + SuiteCost + ActivityCost

    dbconnection.close()


def CreateLabel(container, caption, r, c):
    label = Label (container, text = caption)
    SetLabelStyle_Input(label)
    label.grid (row = r, column = c)

def Submit(RegNo, Name):
    CardNumber = txtCardNumber.get()
    ExpirationYear = txtExpirationYear.get()
    ExpirationMonth = txtExpirationMonth.get()

    dbconnection = mysql.connector.connect(host = 'localhost', username = 'root', password = 'admin', database = 'class_xii_project')
    dbcursor = dbconnection.cursor()

    InsertQuery = "INSERT INTO Payment_Info VALUES ('" + str(RegNo) + "', '" + str(TotalCost) + "', '" + CardNumber + "', '" + ExpirationMonth + "', '" + ExpirationYear +  "')"
    dbcursor.execute (InsertQuery)

    dbconnection.commit()

    dbconnection.close()

    Msg = Name + ', your payment has been recieved. \n \n Itinerary details will be sent via email.' 
    messagebox.showinfo('Confirmation', Msg)
        

def Layout(Pwindow, Name, RegNo):
    
    root = Toplevel(Pwindow)
    root.geometry('400x450')
    root.title('Bermuda Cruise - Payment')
    root.resizable(False, False)
    SetWindowBG(root)
    root.iconbitmap('icon.ico')


    Pricing(RegNo)

    framePrice = LabelFrame(root, text = 'Total Cost', font = 'Times', padx = 7, pady = 10)
    SetFrameBG(framePrice)
    framePrice.grid (row = 0, column = 0, padx = 20, pady = 20)

    CreateLabel (framePrice,  'Name: ', 0, 0)
    CreateLabel (framePrice, Name, 0, 1)

    CreateLabel (framePrice, 'Registeration Number: ', 1, 0)
    CreateLabel (framePrice, RegNo, 1, 1)

    CreateLabel (framePrice, 'Ticket Cost: ', 2, 0)
    CreateLabel (framePrice, TicketCost, 2, 1)

    CreateLabel (framePrice, 'Suite Cost: ', 3, 0)
    CreateLabel (framePrice, SuiteCost, 3, 1)

    CreateLabel (framePrice, 'Activity Cost: ', 4, 0)
    CreateLabel (framePrice, ActivityCost, 4, 1)

    CreateLabel (framePrice, 'Total Cost: ', 5, 0)
    CreateLabel (framePrice, TotalCost, 5, 1)


    global txtCardNumber
    global txtExpirationYear
    global txtExpirationMonth

    frameCard = LabelFrame (root, text = 'Payment', font = 'Times', padx = 7, pady = 10)
    SetFrameBG(frameCard)
    frameCard.grid (row = 1, column = 0, padx = 20, pady = 20)
    
    CreateLabel (frameCard, 'Credit Card Number: ', 0, 0)

    txtCardNumber = Entry(frameCard)
    txtCardNumber.grid (row = 0, column = 1)

    CreateLabel (frameCard, 'Expiration Year: ', 1, 0)

    txtExpirationYear = Entry(frameCard)
    txtExpirationYear.grid (row = 1, column = 1)

    CreateLabel (frameCard, 'Expiration Month: ', 2, 0)
    txtExpirationMonth = Entry(frameCard)
    txtExpirationMonth.grid (row = 2, column = 1)

    CreateLabel (frameCard, 'CVV: ', 3, 0)
    txtCVV = Entry (frameCard, show = '*')
    txtCVV.grid (row = 3, column = 1)


    frameAction = LabelFrame (root, text = '', padx = 7, pady = 10)
    SetFrameBG(frameAction)
    frameAction.grid (row = 2, column = 0)
    
    btnSubmit = Button (frameAction, text = 'Submit', command = lambda: Submit(RegNo, Name))
    SetButtonStyle(btnSubmit)
    btnSubmit.grid(row = 0, column = 0)

    root.mainloop()
