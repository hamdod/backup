import datetime

class Entry:
    def __init__(self,name,colours,length,guesses,date):
        self.name=name
        self.colours=int(colours)
        self.length=int(length)
        self.guesses=int(guesses)
        self.date=date


n="hamish"
c=5
l=6
g=7
day=str(datetime.date.today())
with open("mastermind_leaderboard", "a") as file:
    file.write(n+","+str(c)+","+str(l)+","+str(g)+","+day+"\n")


list=[]
with open("mastermind_leaderboard","r+") as file:
    for line in file.readlines():
        if line!=None:
            list.append(line.strip("\n"))
list_of_hawks=[]
for item in list:
    name,colours,length,guesses,date=item.split(",")
    list_of_hawks.append(Entry(name,colours,length,guesses,date))
list_of_hawks=sorted(list_of_hawks, key=lambda x: x.colours)
list_of_hawks=sorted(list_of_hawks, key=lambda x: x.length)
list_of_hawks=sorted(list_of_hawks, key=lambda x: x.guesses)


#TABLEOS
longest_name=4
def printos(thing):
    print(" "*(5-len(str(thing)))+str(thing),end="")

for entry in list_of_hawks:
    if len(entry.name)>longest_name:
        longest_name=len(entry.name)

print("Name"+" "*(longest_name-4)+" Gues  Col  Len  Date")
i=len(list_of_hawks)-1
while i>=0:
    entry=list_of_hawks[i]
    print(entry.name+" "*(longest_name-len(entry.name)),end="")
    printos(entry.guesses)
    printos(entry.colours)
    printos(entry.length)
    print("  "+entry.date)
    i-=1
