import sys
from functools import reduce

if len(sys.argv)!=2:
    print("Invalid number of arguments.")
    sys.exit()

class Team:
    def __init__(self,name):
        self.name=name
        self.played=0
        self.points=0
        self.wins=0
        self.draws=0
        self.losses=0
        self.gfor=0
        self.gagainst=0

    def win(self,gfor,gagainst):
        self.played+=1
        self.wins+=1
        self.points+=3
        self.gfor+=gfor
        self.gagainst+=gagainst
        self.diff=self.gfor-self.gagainst

    def loss(self,gfor,gagainst):
        self.played+=1
        self.losses+=1
        self.gfor+=gfor
        self.gagainst+=gagainst
        self.diff=self.gfor-self.gagainst

    def draw(self,gfor):
        self.played+=1
        self.points+=1
        self.draws+=1
        self.gfor+=gfor
        self.gagainst+=gfor
        self.diff=self.gfor-self.gagainst

    def result(self,gfor,gagainst):
        if gfor>gagainst:
            self.win(gfor,gagainst)
        elif gfor<gagainst:
            self.loss(gfor,gagainst)
        elif gfor==gagainst:
            self.draw(gfor)


with open(sys.argv[1],"r") as file:
    results=file.read().split("\n")
for item in results:
    if item=="":
        results.remove(item)

list_of_teams=[]
list_of_teams_teams=[]

i=0
while i<len(results):
    t1,t1s,t2s,t2=results[i].split("-")
    if t1 not in list_of_teams:
        list_of_teams.append(t1)
        list_of_teams_teams.append(Team(t1))
    if t2 not in list_of_teams:
        list_of_teams.append(t2)
        list_of_teams_teams.append(Team(t2))
    t1s=int(t1s)
    t2s=int(t2s)
    for team in list_of_teams_teams:
        if team.name==t1:
            team.result(t1s,t2s)
        elif team.name==t2:
            team.result(t2s,t1s)
    i+=1

#SORT THE TEAMS AND STORE IN new_list
new_list = sorted(list_of_teams_teams, key = lambda x : x.gfor)
new_list = sorted(new_list, key = lambda x : x.diff)
new_list = sorted(new_list, key = lambda x : x.points)

#LONGEST NAAAAAME
longest_name=4
for team in new_list:
    if len(team.name)>longest_name:
        longest_name=len(team.name)

#PRINT THE TABLE
def printos(thing):
    print(" "*(3-len(str(thing)))+str(thing),end=" ")

print("Team"+" "*((longest_name)-4)+"   P   W   D   L  GF  GA DIF PTS")
i=len(new_list)-1
while i >=0:
    x=new_list[i]
    print(x.name+" "*(longest_name-len(x.name)),end=" ")
    printos(x.played)
    printos(x.wins)
    printos(x.draws)
    printos(x.losses)
    printos(x.gfor)
    printos(x.gagainst)
    printos(x.diff)
    printos(x.points)
    print("")
    i-=1
