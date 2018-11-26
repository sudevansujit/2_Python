# Program to reverse a String

word = str(input("Enter your String:     "))
a = ""
for item in word:
    item = item + a
    a = item

print("Reversed String is:  ", a)

