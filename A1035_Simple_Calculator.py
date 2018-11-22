print("Select No.     Operation")
print("   1               ADD  ")
print("   2         SUBSTRACT  ")
print("   3          MULTIPLY  ")
print("   4            DIVIDE  ")

dict = {1:"ADD",2:"SUBSTRACT",3:"MULTIPLY",4:"DIVIDE"}

user_input = int(input("Enter Operation number:   "))

a = int(input("Enter a Number a: "))
b = int(input("Enter a Number b: "))

if ((dict[user_input])  == "ADD"):
    print(dict[user_input],"a+b =", a+b)
elif ((dict[user_input])== "SUBSTRACT"): 
    print(dict[user_input],"a-b =", a-b)
elif ((dict[user_input])== "MULTIPLY"): 
    print(dict[user_input],"a*b =", a*b)
elif ((dict[user_input])== "DIVIDE"): 
    print(dict[user_input],"a/b =", a/b)
else:
    print("Invalid Input- Choose 1,2,3 or 4")
