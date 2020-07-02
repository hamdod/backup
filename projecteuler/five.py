"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from three import PrimeFactors

def PrimeFactorsDict(x):
    list = PrimeFactors(x)
    dict = {}
    for i in range(len(list)):
        if list[i] in dict:
            dict[list[i]]+=1
        else:
            dict[list[i]]=1
    return dict

def LowestCommonMultiple(x,y):
    a = PrimeFactorsDict(x)
    b = PrimeFactorsDict(y)
    c = {}
    for i in a:
        if i in b:
            c[i] = max([a[i],b[i]])
        else:
            c[i] = a[i]
    for i in b:
        if i not in a:
            c[i]=b[i]
    number = 1
    for i in c:
        number = number * (i**c[i])
    return number

x = 1
for i in range(2,21):
    x = LowestCommonMultiple(x,i)
print(x)
print(PrimeFactorsDict(x))
