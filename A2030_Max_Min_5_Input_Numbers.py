# Max and Min of 5 Input Numbers

print("Enter Five Numbers between 1 and 100")
a,b,c,d,e = int(input("a=  ")),int(input("b=  ")),int(input("c=  ")),int(input("d=  ")),int(input("e=  "))
list = [a,b,c,d,e]

count = 0
for item in list:
    if(item > count):
        count = item
print(count, "is Maximum")

number = 101
for i in list:
    if i < number:
        number = i
print(number, "is Minimum")
































#    O/P
#    Enter Five Numbers between 1 and 100
#    a=  23
#    b=  45
#    c=  43
#    d=  76
#    e=  87
#    87 is Maximum
#    23 is Minimum
