import sys
import os

dict_of_teams={} #key is team name and value is number of wins
results=[]

def nope():
	print("Could not read file")
	sys.exit()

if len(sys.argv)<2:
	print("No file specified")
	sys.exit()

if not os.path.isfile(sys.argv[1]):
	nope()

with open(sys.argv[1],"r+") as file:
	for x in file.readlines():
		results.append(x.strip("\n"))

for x in results:
	try:
		winner,loser=x.split(" d. ")
		if winner not in dict_of_teams:
			dict_of_teams[winner]=1
		else:
			dict_of_teams[winner]+=1
		if loser not in dict_of_teams:
			dict_of_teams[loser]=0
	except:
		nope()



champion=max(dict_of_teams,key=lambda x:dict_of_teams[x])

spooner=None
for og_team in dict_of_teams.keys():
	team=og_team
	if dict_of_teams[og_team]==0 and og_team!="Bye":
		ok=True
		while ok==True:
			for x in results:
				winner,loser=x.split(" d. ")
				if loser==team:
					if dict_of_teams[winner]==dict_of_teams[team]+1:
						team=winner
						if team==champion:
							ok=False
					else:
						ok=False
					break

		if team==champion:
			spooner=og_team

final_results=[]
if spooner!=None:
	print(spooner+" wins the wooden spoon!")

	team=champion
	ok=True
	while ok==True:
		for x in results:
			winner,loser=x.split(" d. ")
			if team==winner:
				if dict_of_teams[loser]==dict_of_teams[winner]-1:
					team=loser
					final_results.append(x)
			if team==spooner:
				ok=False

	final_results=list(reversed(final_results))

	print("")
	for i in range(len(final_results)):
		if len(final_results)-i>3:
			round=i+1
			print("R{}: {}".format(round,final_results[i]))
		elif len(final_results)-i==3:
			print("QF: {}".format(final_results[i]))
		elif len(final_results)-i==2:
			print("SF: {}".format(final_results[i]))
		else:
			print("F: {}".format(final_results[i]))

else:
	print("No one wins the wooden spoon.")
