# Largest element and its index

L1 = [ 99,23,34,5,67,65,90,89,100]

L2 = len(L1) 

largest = 0

for j in range(L2):
    if L1[j] > largest:
        largest = L1[j]
        position = j

print(largest, "is the largest element in the list")
print(position, "is the index position of the element")


































#    O/P
#    100 is the largest element in the list
#    8 is the index position of the element
