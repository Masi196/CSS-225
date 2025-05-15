#name: masihullah wardak
#date:5/13/2025
#description:  Use a for statement to calculate the factorial of a user input value. Print this value as well as the calculated value using the factorial function in the math module






import math


num = int(input("enter a number to calculate its factorial"))

factorial = 1
for numb in range(1, num + 1):
    factorial = factorial * numb 




print(num)
print(factorial)