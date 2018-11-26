# longest word in a string

lists = str(input("Enter your String Sentence:     "))
new = lists.split()

a = ""

for items in new:
    if (len(items) > len(a)):
        a = items

print(new)
print(a)




































#    O/P
#    Enter your String Sentence:     Programming with Python is fun
#    ['Programming', 'with', 'Python', 'is', 'fun']
#    Programming
