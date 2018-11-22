# Find all Factors of a Number

def num_factors(x):

    print("The factors of " ,x , "are:")

    for i in range(1,(x+1)):
        if x %i == 0 :
            print(i)

num = int(input("Enter a number:   "))
num_factors(num)





































#O/P
#Enter a number:   46
#The factors of  46 are:
#1
#2
#23
#46
