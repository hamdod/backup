"""Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms."""

#naive soln
fibnos = []
fibnos.append(1)
fibnos.append(2)
i = 2
x = 0
while x<4000000:
    x = fibnos[len(fibnos)-1] + fibnos[len(fibnos)-2]
    if x%2==0:
        i+=x
    fibnos.append(x)
print(i)
