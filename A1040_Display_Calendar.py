# Python program to display calendar of given month of the year


import calendar                       # import module

yy = int(input("Enter year: "))       # To ask month and year from the user
mm = int(input("Enter month: "))


print(calendar.month(yy, mm))         # display the calendar  
