import time 

##the current seconds and minutes
currentSeconds = 0
currentMinutes = 0

##the overall time and time limit in seconds
overallSecs = (currentSeconds+(currentMinutes*60))
timeLimitSecs = 0

##gathers input data to set a time limit
timeLimitSecs = int(input("Input time limit in seconds: "))

while overallSecs!=(timeLimitSecs+1):
    if currentSeconds<10:
        print(currentMinutes, ":", "0" + str(currentSeconds))
    else:
        print(currentMinutes, ":", currentSeconds)
    if currentSeconds == 59:
        currentSeconds = 0
        currentMinutes+=1
    else:
        currentSeconds+=1
    
    #updates overall seconds
    overallSecs = (currentSeconds+(currentMinutes*60))
    #waits 1 second
    time.sleep(1)