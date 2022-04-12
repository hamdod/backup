"""
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003,
being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

from three import PrimeFactors


"len prime factos = 1 means prime number"

def subsets(x):
    if x==0:
        return [ [] ]
    else:
        returner = []
        for i in subsets(x-1):
            returner.append(i)
            returner.append(i+[x-1])
    return returner

def anti_subset(subset, length_of_set):
    returner = []
    for i in range(length_of_set):
        if i not in subset:
            returner.append(i)
    return returner

def anti_subsets(x):
    returner = []
    for i in subsets(x):
        returner.append(anti_subset(i,x))
    return returner



a = True
x = 2
while a:
    print(x)
    s = subsets(x)
    ass = anti_subsets(x)
    for i in range(len(s)):
        number = [0]*x
        if len(s[i]) !=0 and len(s[i])!=x:
            for j in range(10**len(s[i])):
                sj = [int(p) for p in str(j)]
                for l in range(len(s[i])-len(sj)):
                    sj = [0]+sj
                m = 0
                for n in s[i]:
                    number[n] = sj[m]
                    m+=1
                counter = 0
                for k in range(10):
                    for n in ass[i]:
                        number[n]=k
                    for p in range(len(number)):
                        number[p] = str(number[p])
                    if len(PrimeFactors(int("".join(number))))==1 and number[0] != "0" and number[0] != 0:
                        counter+=1
                if counter==8:
                    for k in range(10):
                        for n in ass[i]:
                            number[n]=k
                        for p in range(len(number)):
                            number[p] = str(number[p])
                        if len(PrimeFactors(int("".join(number))))==1 and number[0] != "0" and number[0] != 0:
                            abcd = "".join(number)
                            print(abcd, end = ", ")
                    print()
    if x==10:
        a = False
    x+=1
