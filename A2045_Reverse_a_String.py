# Program to reverse a String

word = str(input("Enter your String:     "))
a = ""
for item in word:
    item = item + a
    a = item

print("Reversed String is:  ", a)








































#    O/P
#    Enter your String:     Python is Good
#    Reversed String is:    dooG si nohtyP
