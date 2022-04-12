
"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them
in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
from three import isPrime
primes=[]

"""
#returns a list of all the combinations of *number_of_adders* numbers which sum to *number*
#returned list is just one long continuous list but the combinations can be accessed
#by dividing the list up into quantities of length *number_of_adders*
def possible_sums(number,number_of_adders):
    if number<number_of_adders:
        return None
    if number==number_of_adders:
        return [1]*number_of_adders
    returner = []
    prev = possible_sums(number-1,number_of_adders)
    for i in range(len(prev)//number_of_adders):
        for j in range(number_of_adders):
            #If you concatenate two numbers which are identical, the result will not be prime,
            #so in the following line we use < instead of <=
            if j==number_of_adders-1 or prev[number_of_adders*i+j]+1 < prev[number_of_adders*i+j+1]:
                prev[number_of_adders*i+j]+=1
                for k in range(number_of_adders):
                    returner.append(prev[number_of_adders*i+k])
                prev[number_of_adders*i+j]-=1
    return returner
"""

#for testing divisibility by 3
def sum_of_digits(x):
    i = 0
    for j in range(len(str(x))):
        i += int(str(x)[j])
    return i

#takes a list of numbers and tells you
#i) if they are all prime
#ii) if their pairwise concatenations are all prime
def concatenos(x):
    #i)
    """
    for i in range(len(x)):
        if not isPrime(x[i]):
            return False
    """
    #ii)
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if not isPrime( int(str(x[i])+str(x[j])) ):
                return False
            if not isPrime( int(str(x[j])+str(x[i])) ):
                return False
    return True


for x in range(20000):
    if isPrime(x):
        primes.append(x)

primes.remove(2)
primes.remove(5)

def doit():
    for i in range(len(primes)-4):
        a = primes[i]
        for j in range(i+1,len(primes)-3):
            b = primes[j]
            #print to check progress
            print(a,b)
            #concat
            if concatenos([a,b]):
                for k in range(j+1,len(primes)-2):
                    c = primes[k]
                    #concat
                    if concatenos([a,b,c]):
                        for l in range(k+1,len(primes)-1):
                            d = primes[l]
                            #concat
                            if concatenos([a,b,c,d]):
                                for m in range(l+1,len(primes)):
                                    e = primes[m]
                                    #concat
                                    if concatenos([a,b,c,d,e]):
                                        z = [a,b,c,d,e]
                                        y = a+b+c+d+e
                                        print("HUZZAH")
                                        print(z)
                                        print(y)

doit()
