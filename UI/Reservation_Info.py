from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from WindowStyle import *
import mysql.connector

    
def Info():
    dbconnection = mysql.connector.connect(host = 'localhost', username = 'root', password = 'admin', database = 'class_xii_project')
    dbcursor = dbconnection.cursor()

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
        Email = i[3]
        Mobile = i[4]
        RegNo = i[5]
        Members = i[11]
        SuiteType = i[13]
        Activity = i[14]
        Participants = i[15]
        RoomNumber = i[16]
        CardNumber = i[19]

         
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
    root.title ('Bermuda Cruise - Customer Information')

    root.geometry('1350x250')
    root.resizable(False, False)
    SetWindowBG(root)
    root.iconbitmap('icon.ico')
    

    global myTree 
    myTree = ttk.Treeview(root)

    Scrollbar = ttk.Scrollbar(root, orient = 'vertical', command = myTree.yview)

    myTree.configure(yscrollcommand = Scrollbar.set)

    Scrollbar.pack(side = 'right', fill = 'y')
   
    myTree ['columns'] = ('RegNo', 'Name','Email', 'Mobile','Members', 'Suite Type', 'Activity',
                          'Activity Participants', 'Room Number', 'Card Number')


    myTree.column('#0', width = 0)

    ColumnHeading('RegNo')
    ColumnHeading('Name')
    ColumnHeading('Email')
    ColumnHeading('Mobile')
    ColumnHeading('Members')
    ColumnHeading('Suite Type')
    ColumnHeading('Activity')
    ColumnHeading('Activity Participants')
    ColumnHeading('Room Number')
    ColumnHeading('Card Number')


    Info()

    root.mainloop()
