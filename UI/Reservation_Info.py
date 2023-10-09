from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from WindowStyle import *
import mysql.connector

    
def Info():
    dbconnection = mysql.connector.connect(host = 'localhost', username = 'root', password = 'admin', database = 'class_xii_project')
    dbcursor = dbconnection.cursor()

    SelectQuery = 'SELECT * FROM Personal, Reservation WHERE Reservation.RegNo = Personal.RegNo'
    SelectQuery = '''SELECT PER.*, RES.*, SA.*, PAY.*
    FROM reservation RES
    NATURAL JOIN personal PER
    NATURAL JOIN suite_and_activity SA
    NATURAL JOIN  payment_info PAY'''

    dbcursor.execute (SelectQuery)
    myrecords = dbcursor.fetchall()

    ID = 0

    for i in myrecords:
        Name = i[0]
        #Address = i[1]
        #DOB = i[2]
        Email = i[3]
        Mobile = i[4]
        RegNo = i[5]
        #Dates = i[7]
        #Days = i[8]
        #Boarding = i[9]
        #Leaving = i[10]
        Members = i[11]
        SuiteType = i[13]
        Activity = i[14]
        Participants = i[15]
        RoomNumber = i[16]
        #Amount = i[18]
        CardNumber = i[19]
        #ExpiryMonth = i[20]
        #ExpiryYear = i[21]

        #myTree.insert(parent = '', index = 'end', iid = ID, text = '', values = (Name, Address, DOB, Email, Mobile, RegNo, Dates, Days, Boarding, Leaving, Members,
         #                                                                        SuiteType, Activity, Participants, RoomNumber, Amount, CardNumber, ExpiryMonth, ExpiryYear))
        #myTree.pack(pady = 20)
         
        myTree.insert(parent = '', index = 'end', iid = ID, text = '', values = (RegNo, Name, Email, Mobile, Members,
                                                                                 SuiteType, Activity, Participants, RoomNumber, CardNumber))
        myTree.pack(pady = 20)


        ID = ID + 1
        
    dbconnection.close()


def ColumnHeading(Text):
    myTree.column(Text, anchor = W, width = 130)
    myTree.heading(Text, text = Text, anchor = W)


def InfoScreen():
    root = Tk()
    root.title ('Customer Information')

    root.geometry('1500x500')
    root.resizable(False, False)
    SetWindowBG(root)


    

    global myTree 
    myTree = ttk.Treeview(root)
    #myTree ['columns'] = ('Name', 'Address', 'DOB', 'Email', 'Mobile', 'RegNo', 'Dates', 'Days', 'Boarding', 'Leaving', 'Members', 'Suite Type', 'Activity',
     #                     'Participants', 'Room Number', 'Amount', 'Card Number', 'Expiry Month', 'Expiry Year')

    myTree ['columns'] = ('RegNo', 'Name','Email', 'Mobile','Members', 'Suite Type', 'Activity',
                          'Activity Participants', 'Room Number', 'Card Number')


    myTree.column('#0', width = 0)

    ColumnHeading('RegNo')
    ColumnHeading('Name')
    #ColumnHeading('Address')
    #ColumnHeading('DOB')
    ColumnHeading('Email')
    ColumnHeading('Mobile')
    #ColumnHeading('Dates')
    #ColumnHeading('Days')
    #ColumnHeading('Boarding')
    #ColumnHeading('Leaving')
    ColumnHeading('Members')
    ColumnHeading('Suite Type')
    ColumnHeading('Activity')
    ColumnHeading('Activity Participants')
    ColumnHeading('Room Number')
    #ColumnHeading('Amount')
    ColumnHeading('Card Number')
    #ColumnHeading('Expiry Month')
    #ColumnHeading('Expiry Year')

    Info()

    root.mainloop()
