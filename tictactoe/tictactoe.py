import random

fivemovewin = []
sixmovewin = []
sevenmovewin = []
eightmovewin = []
ninemovewin = []
nowinner = []

def addmove(array, numberofmoves):
    if numberofmoves % 2 == 0:
        insert = 1
    elif numberofmoves % 2 == 1:
        insert = 2

    position = random.randint(0,8-numberofmoves)
    arrayindex=0
    for i in range(9):
        if array[i] == 0:
            if arrayindex == position:
                array[i] = insert
                #arrayindex += 1
            arrayindex += 1
    #print(insert, position)
    #print(array)
    return array

j=0
while j<100000:
    array = [0,0,0,0,0,0,0,0,0]
    n=0
    while n<9:
        array = addmove(array, n)
        n+=1
        if array[0]==array[1]==array[2]!=0 or array[3]==array[4]==array[5]!=0 or array[6]==array[7]==array[8]!=0\
        or array[0]==array[3]==array[6]!=0 or array[1]==array[4]==array[7]!=0 or array[2]==array[5]==array[8]!=0\
        or array[0]==array[4]==array[8]!=0 or array[2]==array[4]==array[6]!=0:
            #print("fk you lilian")
            if n%2==0:
                winner=2
            if n%2==1:
                winner=1
            #print("winner was", winner)
            #print("number of moves:", n)
            break

        if n==9:
            winner = 0
            print("no winner")

    arraystring = ""
    for i in range(9):
        array[i]=str(array[i])
        arraystring = arraystring + array[i]
    #print(arraystring, "\n")


    b = True
    if n==5:
        for i in range(len(fivemovewin)):
            if arraystring==fivemovewin[i]:
                b = False
        if b ==True:
            fivemovewin.append(arraystring)
    if n==6:
        for i in range(len(sixmovewin)):
            if arraystring==sixmovewin[i]:
                b = False
        if b ==True:
            sixmovewin.append(arraystring)
    if n==7:
        for i in range(len(sevenmovewin)):
            if arraystring==sevenmovewin[i]:
                b = False
        if b ==True:
            sevenmovewin.append(arraystring)
    if n==8:
        for i in range(len(eightmovewin)):
            if arraystring==eightmovewin[i]:
                b = False
        if b ==True:
            eightmovewin.append(arraystring)
    if n==9 and winner==1:
        for i in range(len(ninemovewin)):
            if arraystring==ninemovewin[i]:
                b = False
        if b ==True:
            ninemovewin.append(arraystring)
    if n==9 and winner==0:
        for i in range(len(nowinner)):
            if arraystring==nowinner[i]:
                b = False
        if b ==True:
            nowinner.append(arraystring)
    if b==False:
        print(arraystring, "didn't add: fk you lilian")
    else:
        print(arraystring)

    j+=1

print( len(fivemovewin), len(sixmovewin), len(sevenmovewin), len(eightmovewin), len(ninemovewin), len(nowinner) )
