listArrayRandom = [5, 6, 3, 1, 2, 73, 50, 12, 4]
listArrayOrdered = []

for i in range (0, 101):
    listArrayOrdered.append(i)

#linear search (does not require sorted list)
def linearSearch():
    valueFound = False
    numToFind = int(input("Input the value you are searching for: "))
    #cycles through for as long as the list is
    for i in range (1, len(listArrayRandom)):
        #if the number is found, print where and break
        if int(listArrayRandom[i]) == numToFind:
            print("Found in position: "+str(i))
            valueFound = True
            break
        else:
            i+=1

    if not valueFound:
        print("This value could not be found")

#binary search (requires sorted list)
def binarySearch():
    valueFound = False
    positionFound = int
    firstValue = 0
    lastValue = len(listArrayOrdered) - 1
    numToFind = int(input("which number would you like to find: "))

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
        print("Value found in position", midpoint)
    else:
        print("Value not found.")
