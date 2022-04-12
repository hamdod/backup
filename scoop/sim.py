import random

#inputs from sportsbet
odds = {}
odds["No what to keep"] = 6
odds["La La Land"] = 67
odds["Red Axe"] = 10
odds["Oceanography"] = 2.7
odds["Ocean Villa"] = 15
odds["dickhead"] = 5.5
odds["Morwella"] = 5.5
odds["Tempel One"] = 7
#odds["Loyal Romance"] = 41

#to tally firsts and places in simulations
firsts = odds.copy()
places = odds.copy()

#to obtain initial probabilities
true_odds = odds.copy()
lamb = 0
for x in odds:
    lamb+=1/odds[x]

for x in odds:
    true_odds[x] = 1/(lamb*odds[x])
    firsts[x] = 0
    places[x] = 0

def sim_place(dict):

    #adjusting probabilities for removed horse
    sum_of_probs = 0
    for x in dict:
        sum_of_probs+=dict[x]
    for x in dict:
        dict[x] = dict[x]/sum_of_probs


    horses = []
    probs = []
    sum = 0
    for x in dict:
        horses.append(x)
        sum+=dict[x]
        probs.append(sum)
    n = random.random()
    for i in range(len(probs)):
        if i==0 and n<probs[i]:
            placer = horses[0]
            break
        elif i==len(probs)-1:
            placer = horses[i]
            break
        elif n>=probs[i-1] and n<probs[i]:
            placer = horses[i]
            break
    return placer


backed_horse = "Tempel one"
profit_no_lay = 0
profit_lay = 0
lay_stake = 44
for i in range(1000000):
    horsies = true_odds.copy()
    fst = []
    for j in range(3):
        winner = sim_place(horsies)
        for x in horsies:
            if x==winner:
                if j==0:
                    firsts[x]+=1
                    horsies.pop(winner)
                    fst.append(winner)
                    break
                places[x]+=1
                horsies.pop(winner)
                fst.append(winner)
                break

    if backed_horse in fst:
        if backed_horse==fst[0]:
            profit_lay += 50*(odds[backed_horse]-1) - lay_stake*(3.1-1)
            profit_no_lay += 50*(odds[backed_horse]-1)
        else:
            profit_lay += lay_stake*0.94 - 10
            profit_no_lay -= 10
    else:
        profit_lay += lay_stake*0.94 - 50
        profit_no_lay -= 50


print(profit_no_lay/1000000)
print(profit_lay/1000000)
