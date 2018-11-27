# Count Even and odd numbers in a list

L1 = [1,2,3,4,5,6,7,8,9]

even_count = 0
odd_count = 0

for item in L1:
    if (item % 2) == 0 :
        even_count = even_count + 1

    else:
        odd_count = odd_count + 1
        
print(even_count,"odd numbers")
print(odd_count,"even numbers")

































#    O/P
#    4 odd numbers
#    5 even numbers
