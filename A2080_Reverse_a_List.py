# Python Program to Reverse List Elements

newlist = [1,2,3,4,5,6,7]

j = len(newlist)-1 
i = 0

while(i < j):
    element = newlist[i]
    newlist[i] = newlist[j]
    newlist[j] = element
    i = i + 1
    j = j - 1
    
print("\nThe Reversed List is =  ", newlist)


































#    O/P
#    The Reversed List is =   [7, 6, 5, 4, 3, 2, 1]
