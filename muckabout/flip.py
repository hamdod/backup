import numpy as np

number_of_tests = 100000

def condition(listo):
    if len(listo)<2:
        return False
    if listo[-1]==1 and listo[-2]==0:
        return True
    else:
        return False

total_flips = 0

for i in range(number_of_tests):
    flips = 0
    y = []
    b = False
    while b == False:
        flips+=1
        x = np.random.randint(0,2)
        y.append(x)
        if condition(y):
            print(y)
            print(len(y))
            b = True
            total_flips+=flips

print(total_flips/number_of_tests)
