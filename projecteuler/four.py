"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

"""
#bad solution iterating through products
palindromes = []
for x in range(100,1000):
    for y in range(100,1000):
        j = True
        for i in range(int(len(str(x*y))/2)):
            if str(x*y)[i]!=str(x*y)[len(str(x*y))-1-i]:
                j = False
                break
        if j==True:
            palindromes.append(x*y)
print(palindromes)
"""


#better solution iterating through palindromes
for x in range(100,1000):
    number = str(x)+str(x)[2]+str(x)[1]+str(x)[0]
    if number[5]=="0":
        pass
    if number[5]=="1":
        pass
