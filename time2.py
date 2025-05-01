# name: masihullah wardak
# date 4/28/2025
# description: this code asks the user current time and wait time and calculte a final waiting time by adding both current and wait time together.


str_time = input("What time is it now? ")
str_wait_time = input("What is the number of hours to wait? ")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = (time + wait_time)
print(time_when_alarm_go_off)
