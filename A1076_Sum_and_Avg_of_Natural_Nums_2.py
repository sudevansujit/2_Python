# Python Program to find Sum and Average of N Natural Numbers
 
number = int(input("Please Enter any Number: "))

total = 0
value = 1

while (value <= number):
    total = total + value
    value = value + 1

average = total / number

print("The Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total))
print("Average of Natural Numbers from 1 to {0} =  {1}".format(number, average))


































#  Please Enter any Number: 10
#  The Sum of Natural Numbers from 1 to 10 =  55
#  Average of Natural Numbers from 1 to 10 =  5.5
