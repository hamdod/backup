#import random

fivemovewin = []
sixmovewin = []
sevenmovewin = []
eightmovewin = []
ninemovewin = []
nowinner = []

def insert(array, thing, position):
    arrayindex=0
    for i in range(9):
        if array[i] == 0:
            if arrayindex == position:
                array[i] = thing
                print(array)
                return array
            arrayindex+=1

def addmove(array, a, b, c, d, e, f, g, h):
    array = insert(array, 1, a)
    array = insert(array, 2, b)
    array = insert(array, 1, c)
    array = insert(array, 2, d)
    array = insert(array, 1, e)
    if array[0]==array[1]==array[2]!=0 or array[3]==array[4]==array[5]!=0 or array[6]==array[7]==array[8]!=0\
    or array[0]==array[3]==array[6]!=0 or array[1]==array[4]==array[7]!=0 or array[2]==array[5]==array[8]!=0\
    or array[0]==array[4]==array[8]!=0 or array[2]==array[4]==array[6]!=0:
        return array
    array = insert(array, 2, f)
    if array[0]==array[1]==array[2]!=0 or array[3]==array[4]==array[5]!=0 or array[6]==array[7]==array[8]!=0\
    or array[0]==array[3]==array[6]!=0 or array[1]==array[4]==array[7]!=0 or array[2]==array[5]==array[8]!=0\
    or array[0]==array[4]==array[8]!=0 or array[2]==array[4]==array[6]!=0:
        return array
    array = insert(array, 1, g)
    if array[0]==array[1]==array[2]!=0 or array[3]==array[4]==array[5]!=0 or array[6]==array[7]==array[8]!=0\
    or array[0]==array[3]==array[6]!=0 or array[1]==array[4]==array[7]!=0 or array[2]==array[5]==array[8]!=0\
    or array[0]==array[4]==array[8]!=0 or array[2]==array[4]==array[6]!=0:
        return array
    array = insert(array, 2, h)
    if array[0]==array[1]==array[2]!=0 or array[3]==array[4]==array[5]!=0 or array[6]==array[7]==array[8]!=0\
    or array[0]==array[3]==array[6]!=0 or array[1]==array[4]==array[7]!=0 or array[2]==array[5]==array[8]!=0\
    or array[0]==array[4]==array[8]!=0 or array[2]==array[4]==array[6]!=0:
        return array
    array = insert(array, 1, 0)
    return array


array = [0,0,0,0,0,0,0,0,0]
for a in range(9):
    for b in range(8):
        for c in range(7):
            for d in range(6):
                for e in range(5):
                    for f in range(4):
                        for g in range(3):
                            for h in range(2):
                                print(a,b,c,d,e,f,g,h)
                                addmove( array,a,b,c,d,e,f,g,h)

                                if array[0]==array[1]==array[2]==1 or array[3]==array[4]==array[5]==1 or array[6]==array[7]==array[8]==1\
                                or array[0]==array[3]==array[6]==1 or array[1]==array[4]==array[7]==1 or array[2]==array[5]==array[8]==1\
                                or array[0]==array[4]==array[8]==1 or array[2]==array[4]==array[6]==1:
                                    winner=1
                                else:
                                    winner=0


                                n=0
                                for i in range(9):
                                    if array[i]!=0:
                                        n+=1

                                arraystring = ""
                                for i in range(9):
                                    array[i]=str(array[i])
                                    arraystring = arraystring + array[i]
                                #print(arraystring, "\n")

                                z = True
                                if n==5:
                                    for i in range(len(fivemovewin)):
                                        if arraystring==fivemovewin[i]:
                                            z = False
                                    if z ==True:
                                        fivemovewin.append(arraystring)
                                        print(arraystring, "added to fivemovewin")
                                if n==6:
                                    for i in range(len(sixmovewin)):
                                        if arraystring==sixmovewin[i]:
                                            z = False
                                    if z ==True:
                                        sixmovewin.append(arraystring)
                                        print(arraystring, "added to sixmovewin")
                                if n==7:
                                    for i in range(len(sevenmovewin)):
                                        if arraystring==sevenmovewin[i]:
                                            z = False
                                    if z ==True:
                                        sevenmovewin.append(arraystring)
                                        print(arraystring, "added to sevenmovewin")
                                if n==8:
                                    for i in range(len(eightmovewin)):
                                        if arraystring==eightmovewin[i]:
                                            z = False
                                    if z ==True:
                                        eightmovewin.append(arraystring)
                                        print(arraystring, "added to eightmovewin")
                                if n==9 and winner==1:
                                    for i in range(len(ninemovewin)):
                                        if arraystring==ninemovewin[i]:
                                            z = False
                                    if z ==True:
                                        ninemovewin.append(arraystring)
                                        print(arraystring, "added to ninemovewin")
                                if n==9 and winner==0:
                                    for i in range(len(nowinner)):
                                        if arraystring==nowinner[i]:
                                            z = False
                                    if z ==True:
                                        nowinner.append(arraystring)
                                        print(arraystring, "added to nowinner")
                                if z==False:
                                    print(arraystring, "didn't add: fk you lilian")
                                array = [0,0,0,0,0,0,0,0,0]

print()
print( len(fivemovewin), len(sixmovewin), len(sevenmovewin), len(eightmovewin), len(ninemovewin), len(nowinner) )

"""
#checking all possible no winner combos
for x in nowinner:
    list = [" "," "," "," "," "," "," "," "," "]
    for i in range(9):
        if x[i]=="1":
            list[i] = "X"
        if x[i]=="2":
            list[i] = "O"
    print("\n"+list[0]+"|"+list[1]+"|"+list[2]+"\n-----\n"+list[3]+"|"+list[4]+"|"+list[5]+"\n-----\n"+list[6]+"|"+list[7]+"|"+list[8]+"\n")

"""
