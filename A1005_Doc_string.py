#"""It is a string that occurs as the first statement in a module,
#function, class, or method definition. We must write what a
#function/class does in the docstring."""


def double(num):
    """Function to double the value"""
    return 2*num

num=2

print(double.__doc__)
print(double(num))




































#O/P
#Function to double the value
#4
