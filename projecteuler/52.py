"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def same_digits(x):
    a = list(str(x[0]))
    a.sort()
    for i in x:
        b = list(str(i))
        b.sort()
        if a != b:
            return False
    return True



x = 1
a = True
while a:
    if len(str(6*x)) == len(str(x)):
        print(x)
        if same_digits([x,2*x,3*x,4*x,5*x,6*x]):
            print("huzzah: ",x,2*x,3*x,4*x,5*x,6*x)
            a = False
        x+=1
    if len(str(6*x)) != len(str(x)):
        x = 10**len(str(x))
    if x == 10**10:
        a = False
