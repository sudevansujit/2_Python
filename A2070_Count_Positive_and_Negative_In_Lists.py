# Count positive and negative numbers in a list

L1 = [1,-3,-5,-7,-2,2,4,8,9]

positive = 0
negative = 0

for item in L1:
    if (item >= 0):
        positive = positive + 1
    else:
        negative = negative + 1

print(positive, "numbers are positive")
print(negative, "numbers are negative")


































#    O/P
#    5 numbers are positive
#    4 numbers are negative
