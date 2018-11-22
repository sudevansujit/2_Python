# Python Program to find the L.C.M. of two input number


def lcm(x, y):                                 # define a function
   """This function takes two
   integers and returns the L.C.M."""

   
   if x > y:                                   # choose the greater number
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))
























#O/P
#Enter first number: 25
#Enter second number: 125
#The L.C.M. of 25 and 125 is 125 
