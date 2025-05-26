
# name : masihullah wardak
# date: 5/23/2025
# description: this code checks if a number is between 1 to 10 and print the result abed on that

def checkRange(num):
    if num in range(1, 10):
        print(f"{num} is in the range. ")
    else:
        print(f"{num} is not in the range. ")



num = int(input("enter a number"))

print(checkRange(num))
