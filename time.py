# name: masihullah wardak
# date 4/28/2025
# description: this code asks the user current time and wait time and calculte a final waiting time by adding both current and wait time together.



currentTimeStr = input("What is the current time (in hours 0-23)?")

waitTimeStr = input("How many hours do you want to wait")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)
