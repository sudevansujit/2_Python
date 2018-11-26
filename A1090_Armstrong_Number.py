# A positive integer abcd is an Armstrong Number if eg(4 digit number abcd) n = 4
# ( a**n + b**n + c**n + d**n) = abcd

# Python Program For Armstrong Number using While Loop

number = int(input("\nPlease Enter the Number to Check for Armstrong: "))


total = 0                        # Initializing Sum and Number of Digits
digits = 0
           

value = number                  # Calculating Number of individual digits
while value > 0:
    digits = digits + 1
    value = value // 10


value = number                  # Finding Armstrong Number
while value > 0:
    remainder = value % 10
    total = total + (remainder ** digits)
    value //= 10

if number == total:
    print("\n %d is Armstrong Number.\n" %number)
else:
    print("\n %d is Not an Armstrong Number.\n" %number)
