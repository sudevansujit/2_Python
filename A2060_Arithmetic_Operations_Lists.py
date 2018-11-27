# Python Program to Perform List Arithmetic Operations
 
NumList1 = [10, 20, 30]
NumList2 = [5, 10, 15]
add   = []
sub   = []
multi = []
div   = []
mod   = []
expo  = []
 
for j in range(3):
    add.append( NumList1[j] + NumList2[j])
    sub.append( NumList1[j] - NumList2[j])
    multi.append( NumList1[j] * NumList2[j])
    div.append( NumList1[j] / NumList2[j])
    mod.append( NumList1[j] % NumList2[j])
    expo.append( NumList1[j] ** NumList2[j])
 
print("\nThe List Items after Addition =  ", add)
print("The List Items after Subtraction =  ", sub)
print("The List Items after Multiplication =  ", multi)
print("The List Items after Division =  ", div)
print("The List Items after Modulus =  ", mod)
print("The List Items after Exponent =  ", expo)
























#    O/P
#    The List Items after Addition =   [15, 30, 45]
#    The List Items after Subtraction =   [5, 10, 15]
#    The List Items after Multiplication =   [50, 200, 450]
#    The List Items after Division =   [2.0, 2.0, 2.0]
#    The List Items after Modulus =   [0, 0, 0]
#    The List Items after Exponent =   [100000, 10240000000000, 14348907000000000000000]
