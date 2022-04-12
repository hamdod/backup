import random


#Start with an ordered list of horse odds
#ISSUE WITH CODE: we are assuming that bookie odds and true odds occur in same horse order

#used for evaluating returns
#usually take best odds available on punters.com.au
bookie_odds = [6,6.5,4,71,5,17,3.8,9]

#used for evaluating win probabilities
#usually take lay odds on betfair
true_odds = [6,6.5,4,71,5,17,3.8,9]

number_of_horses = len(true_odds)
bookie_odds.sort()
true_odds.sort()
print("Bookie odds:",bookie_odds)
print("Betfair odds:",true_odds)

#estimate the probability of each horse winning based on these odds
reciprocals = []
for i in range(len(true_odds)):
    reciprocals.append(1/true_odds[i])

#TESTY TEST TEST TEST
lamb = 0
for i in range(len(bookie_odds)):
    lamb+=1/bookie_odds[i]
print("Horses:", number_of_horses)
print("Lambda:", lamb)

#This function simulates which horse comes next in placings
def next_horse(listo,placings):

    #if we have already placed the top 3, stop the iteration
    #can swap 3 for len(listo) if you want to place the entire race
    if len(placings) == 3:
        return placings
    #pick a random # between zero and one
    n = random.random()

    #where that random # falls determines the next horse to place

    #sum of reciprocals of odds of remaining horses
    lamb = 0
    for i in range(len(listo)):
        lamb+=listo[i]

    #find out which horse is next to place
    tally = 0
    for j in range(len(listo)):
        tally = tally + ( listo[j] / lamb )
        if n < tally:

            #put the horse into the placings
            placings.append(j)

            #make the probability of this horse zero, so that they don't place again
            listo[j]=0

            #continue placing the next horses
            return next_horse(listo,placings)

#store data from simulated races here
#key = race results in list form e.g. [0,3,2,4,1]
#value = number of races which came up with that result out of total simulated
race_simulations = {}

#simulate races
print("Starting simulations...")
for i in range(1000000):
    #create a copy because we will be editing the list of probabilities
    rcopy = reciprocals.copy()

    #convert the list to a tuple because you can't make a list the key of a dictionary
    result = next_horse(rcopy,[])
    result_tuple = tuple(result)

    #add the result to the dictionary of simulations
    if result_tuple in race_simulations.keys():
        race_simulations[result_tuple] += 1
    else:
        race_simulations[result_tuple] = 1

    #if (i+1)%100000==0:
    #    print(str(i+1),"simulations completed.")


profit=-50000000
for x in race_simulations.keys():
    if x[0]==0:
        profit += bookie_odds[0]*50*race_simulations[x]
    if x[1]==0 or x[2]==0:
        profit += 35*race_simulations[x]
expected_value = profit/1000000
print("Your expected return from betting on the favourite is",expected_value)

profit=-50000000
for x in race_simulations.keys():
    if x[0]==1:
        profit += bookie_odds[1]*50*race_simulations[x]
    if x[1]==1 or x[2]==1:
        profit += 35*race_simulations[x]
expected_value = profit/1000000
print("Your expected return from betting on 2nd favourite is",expected_value)

profit=-50000000
for x in race_simulations.keys():
    if x[0]==2:
        profit += bookie_odds[2]*50*race_simulations[x]
    if x[1]==2 or x[2]==2:
        profit += 35*race_simulations[x]
expected_value = profit/1000000
print("Your expected return from betting on 3rd favourite is",expected_value)

profit=-50000000
for x in race_simulations.keys():
    if x[0]==3:
        profit += bookie_odds[3]*50*race_simulations[x]
    if x[1]==3 or x[2]==3:
        profit += 35*race_simulations[x]
expected_value = profit/1000000
print("Your expected return from betting on 4th favourite is",expected_value)

profit=-50000000
for x in race_simulations.keys():
    if x[0]==4:
        profit += bookie_odds[4]*50*race_simulations[x]
    if x[1]==4 or x[2]==4:
        profit += 35*race_simulations[x]
expected_value = profit/1000000
print("Your expected return from betting on 5th favourite is",expected_value)

print()





"""
#testing stuff - seeing how close the maths for expected prob of 2nd place was to the
#proportion of simulations in which the horse ran second
#it was very close
probs = []
lamb = 0
for i in range(9):
    lamb+=reciprocals[i]
for j in range(9):
    prob = 0
    for k in range(9):
        if k!=j:
            prob+= reciprocals[k]/(lamb-reciprocals[k])
    prob = (reciprocals[j]/lamb)*prob
    probs.append(prob)


for i in range(9):
    counter = 0
    for x in race_simulations.keys():
        if x[1]==str(i):
            counter += race_simulations[x]
    print(str(counter/1000000), probs[i])
"""
