# Python Program to find Perfect Number using For loop
# A number is a perfect mumber if total of all positive divisors excluding\
# the number itself is equal to that number. eg 6 has divisors 1,2,3,and 6\
# so 1+2+3 = 6


number = int(input("Please Enter any Number: "))
total = 0
for i in range(1, number):
    if(number % i == 0):
        total = total + i
if (total == number):
    print(" %d is a Perfect Number" %number)
else:
    print(" %d is not a Perfect Number" %number)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

 #      Please Enter any Number: 496
 #      496 is a Perfect Number  
