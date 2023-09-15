from tkinter import *

root = Tk()
root.title('Suites & Activities')


def CreateLabel(container, caption, r, c):
    label = Label (container, text = caption)
    label.grid (row = r, column = c)


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

r = IntVar()

CreateLabel (frameBooking, 'Breakfast? ', 2, 0)
Ybtn = Radiobutton (frameBooking, text = 'Yes', variable = r, value = 'Y')
Ybtn.grid(row = 2, column = 1)

Nbtn = Radiobutton (frameBooking, text = 'No', variable = r, value = 'N')
Nbtn.grid(row = 2, column = 2)



