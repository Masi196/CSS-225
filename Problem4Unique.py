# name : masihullah wardak
# date: 5/23/2025
#descirption: this code remove repaeting  number in a list by creating a new list



def uniqueElememts(numbers):
    uniqueList = []
    for num in numbers:
        if num not in uniqueList:
            uniqueList.append(num)
    return uniqueList


list = [1, 3, 3, 3, 6, 2, 3, 5]
print(uniqueElememts(list))