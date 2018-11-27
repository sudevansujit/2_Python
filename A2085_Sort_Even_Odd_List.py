# Python Program to Put even and odd numbers in Separate List

numlist = [1,2,3,4,5,6,7,8,9]

even = []
odd = []

j = 0

while(j< len(numlist)):
    if(numlist[j] % 2 == 0):
        even.append(numlist[j])
    else:
        odd.append(numlist[j])
    j = j + 1

print("Element in even List is : ", even,"\n")

print("Element in odd List is : ", odd)
