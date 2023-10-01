from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()
root.title ('Customer Information')



def Info():
    dbconnection = mysql.connector.connect (host = 'localhost', username = 'root', password = 'admin', database = 'class_xii_project')
    dbcursor = dbconnection.cursor()

    SelectQuery = 'SELECT * FROM Personal, Reservation WHERE Reservation.RegNo = Personal.RegNo'
    
    dbcursor.execute (SelectQuery)
    myrecords = dbcursor.fetchall()

    ID = 0

    for i in myrecords:
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

        myTree.insert(parent = '', index = 'end', iid = ID, text = '', values = (Name, Address, DOB, Email, Mobile, RegNo, Dates, Days, Boarding, Leaving, Members))
        myTree.pack(pady = 20)


        ID = ID + 1


def ColumnHeading(Text):
    myTree.column(Text, anchor = W, width = 120)
    myTree.heading(Text, text = Text, anchor = W)

       
myTree = ttk.Treeview(root)
myTree ['columns'] = ('Name', 'Address', 'DOB', 'Email', 'Mobile', 'RegNo', 'Dates', 'Days', 'Boarding', 'Leaving', 'Members')

myTree.column('#0', width = 0)

ColumnHeading('Name')
ColumnHeading('Address')
ColumnHeading('DOB')
ColumnHeading('Email')
ColumnHeading('Mobile')
ColumnHeading('RegNo')
ColumnHeading('Dates')
ColumnHeading('Days')
ColumnHeading('Boarding')
ColumnHeading('Leaving')
ColumnHeading('Members')

Info()


root.mainloop() 
