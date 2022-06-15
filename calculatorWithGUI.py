import tkinter
from tkinter import *
import math

screenText = ""

#configures the GUI for the calculator
def GUIConfig():
    GUI = tkinter.Tk()
    GUI.geometry("300x475")
    GUI.title("Calculator")
    GUI.config(bg="#3d4045")
    GUI.resizable(False, False)

    #configure background of "screen"
    screenBG = tkinter.Label(bg="#2d2f33", width=33, height=5).place(relx=0.5, rely=0, anchor=N)
    
    #configure foreground of "screen"
    screenFG = tkinter.Label(text="", width=30, height=3, anchor=E)
    screenFG.place(relx=0.5, rely=0.03, anchor=N)

    #updates the values on the screen
    def updateScreen(value):
        global screenText
        screenText = screenText+value
        screenFG.config(text=screenText)

    #config buttons 1-9
    oneButton = tkinter.Button(GUI, text="1", width=7, height=5, command=lambda:[updateScreen("1")]).place(relx=0.15, rely=0.3, anchor=CENTER)
    twoButton = tkinter.Button(GUI, text="2", width=7, height=5, command=lambda:[updateScreen("2")]).place(relx=0.374, rely=0.3, anchor=CENTER)
    threeButton = tkinter.Button(GUI, text="3", width=7, height=5, command=lambda:[updateScreen("3")]).place(relx=0.598, rely=0.3, anchor=CENTER)
    fourButton=tkinter.Button(GUI, text="4", width=7, height=5, command=lambda:[updateScreen("4")]).place(relx=0.15, rely=0.46, anchor=CENTER)
    fiveButton = tkinter.Button(GUI, text="5", width=7, height=5, command=lambda:[updateScreen("5")]).place(relx=0.374, rely=0.46, anchor=CENTER)
    sixButton = tkinter.Button(GUI, text="6", width=7, height=5, command=lambda:[updateScreen("6")]).place(relx=0.598, rely=0.46, anchor=CENTER)
    sevenButton = tkinter.Button(GUI, text="7", width=7, height=5, command=lambda:[updateScreen("7")]).place(relx=0.15, rely=0.62, anchor=CENTER)
    eightButton = tkinter.Button(GUI, text="8", width=7, height=5, command=lambda:[updateScreen("8")]).place(relx=0.374, rely=0.62, anchor=CENTER)
    nineButton = tkinter.Button(GUI, text="9", width=7, height=5, command=lambda:[updateScreen("9")]).place(relx=0.598, rely=0.62, anchor=CENTER)

    GUI.mainloop()


GUIConfig()