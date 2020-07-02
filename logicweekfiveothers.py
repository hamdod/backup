D = ["1","2","3","4","5"]
R = ["11","22","33","44","55","21","31","41","51","34","24","35","25","23"]
c = "5"

print("kristof")
def qone(x):
    for y in D:
        if y+x not in R:
            return False
    return True


def qtwo(x):
    for y in D:
        if x+y not in R:
            for z in D:
                if y+z not in R:
                    if x=="2":
                        print(y+z)
                    return False





def qthree(x):
    for y in D:
        if x+y in R:
            if y+x not in R:
                for z in D:
                    if z+y not in R:
                        return False
    return True


def qfour(x):
    return False

def qfive(x):
    return False




#test answers
passed = True
if qone("1")==False:
    print("Q1 failed: false for x = 1")
    passed = False

for i in D:
    if i!="1" and qone(i):
        print("Q1 failed: truth holds for x = "+i)
        passed = False
if passed:
    print("Q1 passed")

passed = True
if qtwo("3")==False:
    print("Q2 failed: false for x = 3")
    passed = False

for i in D:
    if i!="3" and qtwo(i):
        print("Q2 failed: truth holds for x = "+i)
        passed = False
if passed:
    print("Q2 passed")


passed = True
if qthree("4")==False:
    print("Q3 failed: false for x = 4")
    passed = False
elif qthree("5")==False:
    print("Q3 failed: false for x = 5")
    passed = False

for i in D:
    if i!="4" and i!="5" and qthree(i):
        print("Q3 failed: truth holds for x = "+i)
        passed = False
if passed:
    print("Q3 passed")


passed = True
if qfour("4")==False:
    print("Q4 failed: false for x = 4")
    passed = False

for i in D:
    if i!="4" and qfour(i):
        print("Q4 failed: truth holds for x = "+i)
        passed = False
if passed:
    print("Q4 passed")


passed = True
if qfive("5")==False:
    print("Q5 failed: false for x = 5")
    passed = False

for i in D:
    if i!="5" and qfive(i):
        print("Q5 failed: truth holds for x = "+i)
        passed = False
if passed:
    print("Q5 passed")
