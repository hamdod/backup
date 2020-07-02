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
                #print(array)
                return array
            arrayindex+=1

def addmove(array, a, b, c, d, e, f, g, h, arraytwo):
    array = insert(array, 1, a)
    arraytwo=arraytwo+str(a)
    array = insert(array, 2, b)
    arraytwo=arraytwo+str(b)
    array = insert(array, 1, c)
    arraytwo=arraytwo+str(c)
    array = insert(array, 2, d)
    arraytwo=arraytwo+str(d)
    array = insert(array, 1, e)
    arraytwo=arraytwo+str(e)
    if array[0]==array[1]==array[2]!=0 or array[3]==array[4]==array[5]!=0 or array[6]==array[7]==array[8]!=0\
    or array[0]==array[3]==array[6]!=0 or array[1]==array[4]==array[7]!=0 or array[2]==array[5]==array[8]!=0\
    or array[0]==array[4]==array[8]!=0 or array[2]==array[4]==array[6]!=0:
        return arraytwo
    array = insert(array, 2, f)
    arraytwo=arraytwo+str(f)
    if array[0]==array[1]==array[2]!=0 or array[3]==array[4]==array[5]!=0 or array[6]==array[7]==array[8]!=0\
    or array[0]==array[3]==array[6]!=0 or array[1]==array[4]==array[7]!=0 or array[2]==array[5]==array[8]!=0\
    or array[0]==array[4]==array[8]!=0 or array[2]==array[4]==array[6]!=0:
        return arraytwo
    array = insert(array, 1, g)
    arraytwo=arraytwo+str(g)
    if array[0]==array[1]==array[2]!=0 or array[3]==array[4]==array[5]!=0 or array[6]==array[7]==array[8]!=0\
    or array[0]==array[3]==array[6]!=0 or array[1]==array[4]==array[7]!=0 or array[2]==array[5]==array[8]!=0\
    or array[0]==array[4]==array[8]!=0 or array[2]==array[4]==array[6]!=0:
        return arraytwo
    array = insert(array, 2, h)
    arraytwo=arraytwo+str(h)
    if array[0]==array[1]==array[2]!=0 or array[3]==array[4]==array[5]!=0 or array[6]==array[7]==array[8]!=0\
    or array[0]==array[3]==array[6]!=0 or array[1]==array[4]==array[7]!=0 or array[2]==array[5]==array[8]!=0\
    or array[0]==array[4]==array[8]!=0 or array[2]==array[4]==array[6]!=0:
        return arraytwo
    array = insert(array, 1, 0)
    arraytwo=arraytwo+str(0)
    if array[0]==array[1]==array[2]==1 or array[3]==array[4]==array[5]==1 or array[6]==array[7]==array[8]==1\
    or array[0]==array[3]==array[6]==1 or array[1]==array[4]==array[7]==1 or array[2]==array[5]==array[8]==1\
    or array[0]==array[4]==array[8]==1 or array[2]==array[4]==array[6]==1:
        return arraytwo
    arraytwo=arraytwo+"x"
    return arraytwo



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
                                arraytwo = ""
                                arraytwo = addmove( array,a,b,c,d,e,f,g,h, arraytwo)

                                #TRAVERSE THESE ARRAYS IN REVERSE ORDER!
                                z = True
                                if len(arraytwo)==5:
                                    if len(fivemovewin)!=0 and arraytwo ==fivemovewin[len(fivemovewin)-1]:
                                        z = False
                                    if z ==True:
                                        fivemovewin.append(arraytwo)
                                        print(arraytwo, "added to fivemovewin\n")
                                if len(arraytwo)==6:
                                    if len(sixmovewin)!=0 and arraytwo==sixmovewin[len(sixmovewin)-1]:
                                        z = False
                                    if z ==True:
                                        sixmovewin.append(arraytwo)
                                        print(arraytwo, "added to sixmovewin\n")
                                if len(arraytwo)==7:
                                    if len(sevenmovewin)!=0 and arraytwo==sevenmovewin[len(sevenmovewin)-1]:
                                        z = False
                                    if z ==True:
                                        sevenmovewin.append(arraytwo)
                                        print(arraytwo, "added to sevenmovewin\n")
                                if len(arraytwo)==8:
                                    if len(eightmovewin)!=0 and arraytwo==eightmovewin[len(eightmovewin)-1]:
                                        z = False
                                    if z ==True:
                                        eightmovewin.append(arraytwo)
                                        print(arraytwo, "added to eightmovewin\n")
                                if len(arraytwo)==9:
                                    if len(ninemovewin)!=0 and arraytwo==ninemovewin[len(ninemovewin)-1]:
                                        z = False
                                    if z ==True:
                                        ninemovewin.append(arraytwo)
                                        print(arraytwo, "added to ninemovewin\n")
                                if len(arraytwo)==10:
                                    if len(nowinner)!=0 and arraytwo==nowinner[len(nowinner)-1]:
                                        z = False
                                    if z ==True:
                                        nowinner.append(arraytwo)
                                        print(arraytwo, "added to nowinner\n")
                                if z==False:
                                    print(arraytwo, "didn't add: fk you lilian\n")
                                array = [0,0,0,0,0,0,0,0,0]

print()
print( len(fivemovewin), len(sixmovewin), len(sevenmovewin), len(eightmovewin), len(ninemovewin), len(nowinner), "\n" )

print("There are ",str(len(fivemovewin)+len(sixmovewin)+len(sevenmovewin)+len(eightmovewin)+len(ninemovewin)+len(nowinner))," possible games of noughts and crosses.\n")

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
