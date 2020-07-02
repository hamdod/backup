# YOUR CODE HERE
import sys

#countycountmccountface (this will be useful later) (trust me)
def count(stringy):
	listylist = []
	for i in range(1,7):
		counter=0
		for j in range(len(stringy)):
			if stringy[j]==str(i):
				counter+=1
		listylist.append(counter)
	return listylist

#checking a solution
def checksol(sol):
	for x in range(6):
		if sol[x]==sol[x+6] or sol[x]==sol[x+12] or sol[x]==sol[x+18] or sol[x]==sol[x+24] or sol[x]==sol[x+30]\
		or sol[x+6]==sol[x+12] or sol[x+6]==sol[x+18] or sol[x+6]==sol[x+24] or sol[x+6]==sol[x+30]\
		or sol[x+12]==sol[x+18] or sol[x+12]==sol[x+24] or sol[x+12]==sol[x+30]\
		or sol[x+18]==sol[x+24] or sol[x+18]==sol[x+30]\
		or sol[x+24]==sol[x+30]:
			return False
		if sol[6*x]==sol[6*x+1] or sol[6*x]==sol[6*x+2] or sol[6*x]==sol[6*x+3] or sol[6*x]==sol[6*x+4] or sol[6*x]==sol[6*x+5]\
		or sol[6*x+1]==sol[6*x+2] or sol[6*x+1]==sol[6*x+3] or sol[6*x+1]==sol[6*x+4] or sol[6*x+1]==sol[6*x+5]\
		or sol[6*x+2]==sol[6*x+3] or sol[6*x+2]==sol[6*x+4] or sol[6*x+2]==sol[6*x+5]\
		or sol[6*x+3]==sol[6*x+4] or sol[6*x+3]==sol[6*x+5]\
		or sol[6*x+4]==sol[6*x+5]:
			return False
	return True


grid = []
for i in range(6):
	for x in input().split(" "):
		grid.append(int(x))

operators = []
for x in input().split(" "):
	operators.append(x)

results = []
for i in range(len(operators)):
	x = operators[i]
	if x[len(x)-1]=="*" or x[len(x)-1]=="/" or x[len(x)-1]=="+" or x[len(x)-1]=="-":
		string = x[0:len(x)-1]
		results.append(int(string))
		operators[i] = x[len(x)-1]
	else:
		results.append(int(x))
		operators[i] = None

#list of lists of coords of each square
listofcoords = []
for i in range(len(operators)):
	coords = []
	for j in range(36):
		if grid[j]==i:
			coords.append(str(int(j%6))+str( int( (j-j%6)/6 ) ) )
	listofcoords.append(coords)
#for i in range(len(operators)):
	#print(i, listofcoords[i])

#list of lists of solutions
listofsols = []
for i in range(len(operators)):
	sols = []
	if operators[i]==None:
		sols.append(str(results[i]))
	if operators[i]=="/":
		if results[i]==1:
			sols.append("11")
			sols.append("22")
			sols.append("33")
			sols.append("44")
			sols.append("55")
			sols.append("66")
		if results[i]==2:
			sols.append("12")
			sols.append("21")
			sols.append("24")
			sols.append("42")
			sols.append("36")
			sols.append("63")
		if results[i]==3:
			sols.append("13")
			sols.append("31")
			sols.append("26")
			sols.append("62")
	if operators[i]=="-":
		for a in range(1,7):
			for b in range(1,7):
				if abs(a-b)==results[i]:
					string = str(a)+str(b)
					sols.append(string)
	if operators[i]=="+":
		counter = 0
		for j in range(len(grid)):
			if grid[j]==i:
				counter+=1
		if counter == 2:
			for a in range(1,7):
				for b in range(1,7):
					if a+b==results[i]:
						string = str(a)+str(b)
						sols.append(string)
		if counter == 3:
			for a in range(1,7):
				for b in range(1,7):
					for c in range(1,7):
						if a+b+c==results[i]:
							string = str(a)+str(b)+str(c)
							sols.append(string)
		if counter == 4:
			for a in range(1,7):
				for b in range(1,7):
					for c in range(1,7):
						for d in range(1,7):
							if a+b+c+d==results[i]:
								string = str(a)+str(b)+str(c)+str(d)
								sols.append(string)
		if counter == 5:
			for a in range(1,7):
				for b in range(1,7):
					for c in range(1,7):
						for d in range(1,7):
							for e in range(1,7):
								if a+b+c+d+e==results[i]:
									string = str(a)+str(b)+str(c)+str(d)+str(e)
									sols.append(string)
		if counter == 6:
			for a in range(1,7):
				for b in range(1,7):
					for c in range(1,7):
						for d in range(1,7):
							for e in range(1,7):
								for f in range(1,7):
									if a+b+c+d+e+f==results[i]:
										string = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
										sols.append(string)
	if operators[i]=="*":
		counter = 0
		for j in range(len(grid)):
			if grid[j]==i:
				counter+=1
		if counter == 2:
			for a in range(1,7):
				for b in range(1,7):
					if a*b==results[i]:
						string = str(a)+str(b)
						sols.append(string)
		if counter == 3:
			for a in range(1,7):
				for b in range(1,7):
					for c in range(1,7):
						if a*b*c==results[i]:
							string = str(a)+str(b)+str(c)
							sols.append(string)
		if counter == 4:
			for a in range(1,7):
				for b in range(1,7):
					for c in range(1,7):
						for d in range(1,7):
							if a*b*c*d==results[i]:
								string = str(a)+str(b)+str(c)+str(d)
								sols.append(string)
		if counter == 5:
			for a in range(1,7):
				for b in range(1,7):
					for c in range(1,7):
						for d in range(1,7):
							for e in range(1,7):
								if a*b*c*d*e==results[i]:
									string = str(a)+str(b)+str(c)+str(d)+str(e)
									sols.append(string)
		if counter == 6:
			for a in range(1,7):
				for b in range(1,7):
					for c in range(1,7):
						for d in range(1,7):
							for e in range(1,7):
								for f in range(1,7):
									if a*b*c*d*e*f==results[i]:
										string = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
										sols.append(string)
	listofsols.append(sols)


"""
#test,check
#print(listofsols)
number=1
for i in range(len(listofsols)):
	number = number * len(listofsols[i])
print(number)
"""

#preliminaryswoop
listtoremove = []
for i in range(len(operators)):
	#REMOVING SOLUTIONS WHERE NUMBER IS IN SAME ROW OR COLUMN AS SAME NUMBER IN SINGLE BOX
	if operators[i]==None:
		for j in range(len(listofsols)):
			if j!=i:
				#print(listofsols[j])
				for a in range(len(listofsols[j])):
					for k in range(len(listofsols[j][0])):
						if listofcoords[i][0][0]==listofcoords[j][k][0] or listofcoords[i][0][1]==listofcoords[j][k][1]:
							#print(j, a  , k)
							if listofsols[j][a][k] == listofsols[i][0][0]:
								#print(j, listofsols[j][a])
								stringy = str(j)
								stringy = stringy + " " + str(listofsols[j][a])
								listtoremove.append(stringy)
	#REMOVING SOLUTIONS WHERE SAME NUMBER OCCURS MULTIPLE TIMES IN SAME BOX IN SAME ROW OR COLUMN
	else:
		for a in range(len(listofcoords[i])):
			for b in range(len(listofcoords[i])):
				if a!=b:
					if listofcoords[i][a][0]==listofcoords[i][b][0] or listofcoords[i][a][1]==listofcoords[i][b][1]:
						for j in range(len(listofsols[i])):
							if listofsols[i][j][a]==listofsols[i][j][b]:
								stringy = str(i)
								stringy = stringy + " " + str(listofsols[i][j])
								listtoremove.append(stringy)

#print(listtoremove)
for i in range(len(listtoremove)):
	x,y = listtoremove[i].split(" ")
	try:
		listofsols[int(x)].remove(y)
	except:
		pass

"""
#test,check
print(listofsols)
number=1
for i in range(len(listofsols)):
	number = number * len(listofsols[i])
print(number)
"""


#SWOOOOOOOP
swoop=0
while swoop<10:
	listtoremove = []
	for i in range(len(operators)):


		#REMOVING SOLUTIONS IN SAME ROW OR COLUMN AS BOX WHICH MUST HAVE 2 OR 3 SAME VALUES IN A ROW
		if len(listofsols[i])>1:
			jasmine = True
			for j in range(1, len(listofsols[i])):
				if count(listofsols[i][j])!=count(listofsols[i][j-1]):
					jasmine=False
			if jasmine==True:
				#2 or more in a row
				jasrow=True
				for j in range(1,len(listofcoords[i])):
					if listofcoords[i][j][0]!=listofcoords[i][j-1][0]:
						jasrow=False
				if jasrow==True:
					#print(i, listofsols[i])
					for k in range(len(listofcoords)):
						if k!=i:
							for l in range(len(listofcoords[k])):
								if listofcoords[k][l][0]==listofcoords[i][0][0]:
									for n in range(len(listofsols[k])):
										for p in range(len(listofsols[i][0])):
											if listofsols[k][n][l]==listofsols[i][0][p]:
												stringy = str(k)
												stringy = stringy + " " + str(listofsols[k][n])
												listtoremove.append(stringy)
				#2 or more in a column
				jascol=True
				for j in range(1,len(listofcoords[i])):
					if listofcoords[i][j][1]!=listofcoords[i][j-1][1]:
						jascol=False
				if jascol==True:
					#print(i, listofsols[i])
					for k in range(len(listofcoords)):
						if k!=i:
							for l in range(len(listofcoords[k])):
								if listofcoords[k][l][1]==listofcoords[i][0][1]:
									for n in range(len(listofsols[k])):
										for p in range(len(listofsols[i][0])):
											if listofsols[k][n][l]==listofsols[i][0][p]:
												stringy = str(k)
												stringy = stringy + " " + str(listofsols[k][n])
												listtoremove.append(stringy)


		#REMOVING SOLUTIONS WHERE NUMBER OCCURS IN SAME ROW OR COLUMN AS BOX WHERE THAT NUMBER IS THE ONLY POSSIBILITY
		if len(listofsols[i])==1 and operators[i]!=None:
			for a in range(len(listofsols[i][0])):
				x = listofcoords[i][a][0]
				y = listofcoords[i][a][1]
				for b in range(len(listofcoords)):
					for c in range(len(listofcoords[b])):
						if b!=i:
							if listofcoords[b][c][0]==x or listofcoords[b][c][1]==y:
								for j in range(len(listofsols[b])):
									if listofsols[b][j][c] == listofsols[i][0][a]:
										stringy = str(b)
										stringy = stringy + " " + str(listofsols[b][j])
										listtoremove.append(stringy)
	for i in range(len(listtoremove)):
		x,y = listtoremove[i].split(" ")
		try:
			listofsols[int(x)].remove(y)
		except:
			pass
	for i in range(len(listofsols)):
		if len(listofsols[i])==0:
			print("No solution.")
			sys.exit()

	"""
	#test,check
	number=1
	for i in range(len(listofsols)):
		number = number * len(listofsols[i])
	print(number)
	"""


	swoop+=1
	brekkie=True
	for i in range(len(listofsols)):
		if len(listofsols[i])>1:
			brekkie=False
	if brekkie==True:
		break


#checking all possible solutions
solution = [0]*36
def createsol(sol,counter,limit):
	if counter<limit:
		#yourcodehere
		for i in range(len(listofsols[counter])):
			additin = True
			for j in range(len(listofcoords[counter])):
				x = int(listofcoords[counter][j][0])
				y = int(listofcoords[counter][j][1])
				for k in range(len(sol)):
					if k%6 == x or int(k/6) == y:
						if sol[k] == int(listofsols[counter][i][j]):
							additin=False
				sol[x+6*y] = listofsols[counter][i][j]
			counter+=1
			if additin==True:
				createsol(sol,counter,limit)
			counter-=1
	else:
		if checksol(sol)==True:
			for a in range(6):
				for b in range(5):
					print(solution[a*6+b],end=" ")
				print(solution[a*6+5])
			sys.exit()
	return
createsol(solution,0,len(operators))

print("No solution.")




	
