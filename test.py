list=["yianni","is","a","fuashtag"]

list[0],list[1]=list[1],list[0]
print(list)

list=["tho","bang","still","would","i"]

i=len(list)-1
while i>=0:
    print(list[i],end=" ")
    i-=1
