# Program to check String Palindrome or Not

my_str = str(input("Enter your String :   "))   

my_str = my_str.casefold()               # make it suitable for caseless comparison

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):         # check if the string is equal to its reverse
   print("It is palindrome")

else:
   print("It is not palindrome")
    




