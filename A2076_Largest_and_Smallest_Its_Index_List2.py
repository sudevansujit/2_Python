# Largest and amallest element and its index

L1 = [ 99,23,34,5,67,65,90,89,100]

L2 = len(L1) 

largest = 0
smallest = 101

for j in range(L2):
    if L1[j] > largest:
        largest = L1[j]
        large_pos = j
    if L1[j] < smallest:
        smallest = L1[j]
        small_pos = j
        
print(largest, "is the largest element in the list")
print(large_pos, "is the index position of the largest element""\n")

print(smallest, "is the smallest element in the list")
print(small_pos, "is the index position of the smallest element")



























#    O/P
#    100 is the largest element in the list
#    8 is the index position of the largest element

#    5 is the smallest element in the list
#    3 is the index position of the smallest element
