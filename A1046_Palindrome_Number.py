# Python Palindrome Program for a number using While loop

 
number = int(input("Please Enter any Number: "))

reverse = 0
value = number

while(value > 0):
    remainder = value % 10
    reverse = (reverse * 10) + remainder
    value = value //10
 
print("Reverse of given number = %d" %reverse)

if(number == reverse):
    print("%d is a Palindrome Number" %number)
else:
    print("%d is not a Palindrome Number" %number)
