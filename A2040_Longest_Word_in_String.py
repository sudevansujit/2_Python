# longest word in a string

lists = str(input("Enter your String Sentence:     "))
new = lists.split()

a = ""

for items in new:
    if (len(items) > len(a)):
        a = items

print(new)
print(a)
