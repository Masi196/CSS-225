# name : masihullah wardak
# date: 5/23/2025
#descirption: this code multiply each numbers in list to its next index value number



def multiplyNum(numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result


list = [5, 2, 7, -1]

print(multiplyNum(list))