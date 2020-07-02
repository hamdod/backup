"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""
import math


def PrimeFactors(x):
    if int(x/2)<2:
        return [int(x)]
    for i in range(2,int(math.sqrt(x))+1):          #could we replace sqrt with something more efficient?
        if x%i==0:
            return [i]+PrimeFactors(x/i)
    return [int(x)]
def largestPrimeFactor(x):
    return max(PrimeFactors(x))


#print(largestPrimeFactor(600851475143))
#print(largestPrimeFactor(32*12349807254*1249857234095743259078*435328764325078*234598723450978*234579802345))
#print(PrimeFactors(60085147514300224806))
#print(PrimeFactors(32726700))
