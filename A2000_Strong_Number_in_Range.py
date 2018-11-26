# Python Program to print Strong numbers from 1 to Maximum

# Strong numbers are such numbers in which the sum of the factorials
# of the digits is equal to the given number


import math

maximum = int(input(" Please Enter the Maximum Value: "))

for number in range(1, maximum):

    value = number
    total = 0

    while(value > 0):
        remainder = value % 10
        factorial = math.factorial(remainder)
        total = total + factorial
        value = value // 10
    
    if (total == number):
        print(" %d is a Strong number" %number)
