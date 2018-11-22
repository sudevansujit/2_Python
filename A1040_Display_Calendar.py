# Python program to display calendar of given month of the year


import calendar                       # import module

yy = int(input("Enter year: "))       # To ask month and year from the user
mm = int(input("Enter month: "))


print(calendar.month(yy, mm))         # display the calendar  







































#     O/P
#     Enter year: 2018
#     Enter month: 11
#     November 2018
#     Mo Tu We Th Fr Sa Su
#               1  2  3  4
#      5  6  7  8  9 10 11
#     12 13 14 15 16 17 18
#     19 20 21 22 23 24 25
#     26 27 28 29 30
