# Greater of three numbers Nested if Statement

a = float(input("Please Enter the First value: "))
b = float(input("Please Enter the Second value: "))
c = float(input("Please Enter the Third value: "))

if (a-b > 0) and (a-c > 0):
    print("{0} is Greater Than both {1} and {2}". format(a, b, c))
else:
    if(b - c > 0):
        print("{0} is Greater Than both {1} and {2}". format(b, a, c))
    else:
        print("{0} is Greater Than both {1} and {2}". format(c, a, b))
