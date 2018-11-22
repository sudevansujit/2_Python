# Program to sort words in alpahbetical order

my_str = "Python is a wonderful programming language"
new_str = my_str.split(" ")


#new_str.sort()                                             # Another Option


alphabets = """A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z"""
alpha_split=alphabets.split(" ")



for char in alpha_split:
    for item in new_str:
        if item[0] == char:

            print(item)


