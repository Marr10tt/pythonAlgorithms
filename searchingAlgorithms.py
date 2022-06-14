import tkinter
from tkinter import *
listArrayRandom = [5, 6, 3, 1, 2, 73, 50, 12, 4]
listArrayOrdered = []

linearResults = ""
binaryResults = ""

for i in range (0, 101):
    listArrayOrdered.append(i)

#linear search (does not require sorted list)
def linearSearch(numToFind):
    global linearResults

    valueFound = False
    #tries to convert value to integer, if not throws error
    try:
        #converts to int, cycles through until result is determined
        numToFind = int(numToFind)
        for i in range (0, len(listArrayRandom)):
            #if the number is found, print where and break
            if int(listArrayRandom[i]) == numToFind:
                linearResults=("Value found in position: "+str(i))
                valueFound = True
                break
            else:
                i+=1

        if not valueFound:
            linearResults = "This value could not be found."

    except:
        linearResults = "Error - invalid input"

#binary search (requires sorted list)
def binarySearch(numToFind):
    global binaryResults

    valueFound = False
    firstValue = 0
    lastValue = len(listArrayOrdered) - 1

    try:
        numToFind = int(numToFind)
        while firstValue<=lastValue:
            midpoint = int(round((firstValue+lastValue)/2))
            #checks to see if numToFind is at the position of midpoint
            if listArrayOrdered[midpoint] == numToFind:
                valueFound = True
                positionFound = midpoint
                break
            #if numToFind is bigger than position of midpoint, firstValue increases to midpoint+1
            elif numToFind > listArrayOrdered[midpoint]:
                firstValue = midpoint+1
            #if numToFind is smaller that position of midpoint, lastValue decreases to midpoint-1
            elif numToFind < listArrayOrdered[midpoint]:
                lastValue = midpoint-1    
        if valueFound == True:
            binaryResults = ("Value found in position: " +str(midpoint))

        else:
            binaryResults = ("This value could not be found.")

    except:
        binaryResults = ("Error - invalid input")

def __main__():
    #defines user interface
    mainScreen = tkinter.Tk()

    #configuration of the screen
    mainScreen.geometry("700x500+350+200")
    mainScreen.config(bg="#363b3e")
    mainScreen.title("Searching algorithms")

    #Linear search section
    linearTextBox = tkinter.Entry(width=24)
    linearTextBox.place(relx=0.25, rely=0.5, anchor=CENTER)

    linearResult  = tkinter.Label(textvariable=linearResults, height=1, width=25, anchor=W)
    linearResult.place(relx=0.25, rely=0.6, anchor=CENTER)

    def updateLinearResults():
        linearResult.config(text=linearResults)

    linearButton = tkinter.Button(text="Linear search", height=5, width=15, command=lambda:[linearSearch(linearTextBox.get()), updateLinearResults()]).place(relx=0.25, rely=0.35, anchor=CENTER)

    #Binary search section
    binaryTextBox = tkinter.Entry(width=24)
    binaryTextBox.place(relx=0.75, rely=0.5, anchor=CENTER)

    binaryResult = tkinter.Label(textvariable=binaryResults, height=1, width=25, anchor=W)
    binaryResult.place(relx=0.75, rely=0.6, anchor=CENTER)

    def updateBinaryResults():
        binaryResult.config(text=binaryResults)

    binaryButton = tkinter.Button(text="Binary search", height=5, width=15, command=lambda:[binarySearch(binaryTextBox.get()), updateBinaryResults()]).place(relx=0.75, rely=0.35, anchor=CENTER)

    #calls user interface
    mainScreen.mainloop()

__main__()