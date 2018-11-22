# Python program to find the H.C.F of two input number


def computeHCF(x, y):            # define a function

                               
    if x > y:                    # Select the smaller number 
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The H.C.F. of", num1,"and", num2,"is  ", computeHCF(num1, num2))




























#O/P
# Enter first number: 12
# Enter second number: 48
# The H.C.F. of 12 and 48 is   12
