from tkinter import *
import tkinter.font as font

def SetWindowBG(Window):
    Window['background'] = '#064273'

def SetButtonStyle(Button):
    ButtonFont = font.Font(family = 'californian fb', size = 10, weight = 'bold')
    Button['activebackground'] = '#98BFDD'
    Button['bg'] = '#98BFDD'
    Button['font'] = ButtonFont


def SetFrameBG(Frame):
    Frame ['background'] = '#cfe1f2'

def SetLabelStyle_Input(Label):
    Label ['bg'] = '#cfe1f2'
    Label ['font'] = font.Font(family = 'berlin sans fb', size = 10, weight = 'normal')
    Label ['width'] = 22

def SetLabelStyle_Home(Label):
    Label ['bg'] = '#cfe1f2'

def DropStyle(Drop):
    Drop ['bg'] = '#cfe1f2'
    Drop ['font'] = font.Font(family = 'berlin sans fb', size = 10, weight = 'normal')
    Drop ['width'] = 10
    



    



    
