#Program to count vowels in a string

vowels = [ "a", "e", "i", "o", "u"]

sentence = str(input("Enter String:   "))
sent = sentence.casefold()
print(sent)

count = 0

for item in sent:
    if item in vowels:
        a = str(item)
        count += 1
        print(a)
print("Total Vowels  =",count)

































#   Enter String:   Python is a wonderful language
#   python is a wonderful language
#   o
#   i
#   a
#   o
#   e
#   u
#   a
#   u
#   a
#   e
#   Total Vowels  = 10
