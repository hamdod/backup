D = [1,2,3,4,5]

def func(A):
    n = len(A)
    B = [n]
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(1,n):
        stored_sum = 0
        for j in range(i,n):
            stored_sum = stored_sum + A[j]
            C[i][j] = stored_sum / (j-i+1)
    return C

print(func(D))
