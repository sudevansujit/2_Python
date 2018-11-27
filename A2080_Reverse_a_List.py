# Python Program to Reverse List Elements

newlist = [1,2,3,4,5,6,7]

#number = int(input("Please enter the Total number of List Elements: "))

#for i in range(1, number + 1):
#    value = int(input("Please enter the Value of %d Element : " %i))
#    newlist.append(value)

j = len(newlist)-1 
i = 0

while(i < j):
    element = newlist[i]
    newlist[i] = newlist[j]
    newlist[j] = element
    i = i + 1
    j = j - 1
    
print("\nThe Reversed List is =  ", newlist)

