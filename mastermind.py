import sys
import random
import datetime

k=True
while k==True:

	with open("colourlist.txt","r") as file:
		list_of_colours=file.read().split("\n")
	with open("colourlist.txt","r") as file:
		list_of_colour_names=file.read().split("\n")
	for i in range(len(list_of_colours)):
		try:
			list_of_colours[i]=str(list_of_colours[i])[0]
		except:
			list_of_colours.remove(list_of_colours[i])


	def whatsya():
		name=input()
		i=0
		while i<len(name):
			if name[i]=="_":
				print("\nSorry, bud, I don't permit underscores.\n")
				return whatsya()
			i+=1
		if len(name)>30:
			print("\nTitf pick a shorter name.\n")
			return whatsya()
		elif len(name)<4 or "," in name or "\t" in name:
			print("\nOh, is that right, is it? You're name is '{}'?\n"
			"I wasn't born yesterday, you know. Try again.\n".format(name))
			return whatsya()
		else:
			return name

	def choose_colours():
		try:
			number_of_colours=int(input("Number of colours: "))
		except:
			print("\nWhoopsee. Looks like you didn't input a valid number. Try again.\n")
			return choose_colours()
		if number_of_colours>26 or number_of_colours<4:
			print("\nWhoopse. Looks like you chose a bad number.\n"
			"Easy there, cowboy! Pick a different number.\n")
			return choose_colours()
		return number_of_colours


	def choose_code():
		try:
			code=int(input("Length of code: "))
		except:
			print("\nYou numskull! That's not a suitable number!\n"
			"Try again, buddy.\n")
			return choose_code()
		if code<1 or code>26:
			print("\nYou numbskull! That's not a suitable number!\n"
			"Try again, buddy.\n")
			return choose_code()
		return code

	def choose_difficulty():
		dif=input("Choose a difficulty (Enter a letter): ")
		return dif

	print("\n\n\n\n\n\nWelcome to Mastermind. It is time to guess the code!\n"
	"\nBut first, let's get to know each other... what's ya name?\n")
	name=whatsya()

	print("\n\nCool name! Now, please choose a difficulty:"
	"\nE = Easy"
	"\nM = Medium (same as board game)"
	"\nH = Hard"
	"\nI = Insane"
	"\n\nAlternatively, you may choose a specific code length and number of colours by typing 'choose'.\n")

	i=False
	while i==False:
		dif=choose_difficulty()
		if dif=="E":
			code_length=4
			colours=4
			i=True
		elif dif=="M":
			code_length=4
			colours=8
			i=True
		elif dif=="H":
			code_length=6
			colours=10
			i=True
		elif dif=="I":
			code_length=10
			colours=15
			i=True
		elif dif=="choose":
			print("\n\nThis man don't play by no rules! I like that..."
			"\nNow, please choose how many colours you would like to choose from.\n")
			colours=choose_colours()

			print("\n\nFantastic! I knew you could do it.\n"
			"Now, it's time to pick how long you want the code to be.\n"
			"Remember: the longer it is, the harder it will be to crack!\n")
			code_length=choose_code()
			i=True
		else:
			print("\n\nInvalid difficulty. Please read the instructions carefully.\n")



	code_to_guess=[]
	list1=list_of_colours[0:colours]
	list_of_colours=list1


	for i in range(code_length):
		code_to_guess.append(list_of_colours[random.randint(0,len(list_of_colours)-1)])


	def input_guess():
		code=[]
		a=input()
		if a=="q" or a=="Q":
			return a
		try:
			code=a.split(" ")
			if code_length!=len(code):
				print("\nCode length incorrect.\n"
				"Can you count? You stupid, dumb, big baby.\n")
				return input_guess()
			for i in range(len(code)):
				if code[i] not in list_of_colours:
					print("\nERROR: {} is not a valid colour.\n"
					"You fucking idiot. I literally gave you a list of colours.\n".format(code[i]))
					return input_guess()
		except:
			print("\nInvalid code.\n")
			return input_guess()

		return code

	def guess_response():
		guess=input_guess()
		if guess=="q" or guess=="Q":
			return guess
		white=0
		black=0
		guess_dict={}
		code_dict={}
		i=0
		while i<code_length:
			try:
				code_dict[code_to_guess[i]]+=1
			except:
				code_dict[code_to_guess[i]]=1
			try:
				guess_dict[guess[i]]+=1
			except:
				guess_dict[guess[i]]=1
			i+=1
		for item in guess_dict:
			if item in code_dict:
				if code_dict[item]>=guess_dict[item]:
					white+=guess_dict[item]
				else:
					white+=code_dict[item]
		for i in range(code_length):
			if guess[i]==code_to_guess[i]:
				black+=1
		white=white-black
		return (white,black)


	print("\n\nGreat! Now it is time to guess the code!\n"
	"Please enter {} letters, SEPERATED BY SPACES, corresponding to your guess\n"
	"Two numbers will be returned:\n"
	"1. The number of correct colours which AREN'T in the right spot.\n"
	"2. The number of correct colours which ARE in the right spot.\n"
	"Remember: you can give up any time you like, by simply writing 'q' or 'Q'\n"
	"but I'll think you're a big baby idiot.\n"
	"\nChoice of colours:".format(code_length))
	for i in range(len(list_of_colours)):
		print("{}: {}".format(list_of_colours[i],list_of_colour_names[i]))
	print("")

	turn_counter=0
	while True:
		a=guess_response()
		if a=="Q" or a=="q":
			print("\n\nHAHAHAHAHAHAHAHA\n"
			"You fucking idiot. God, you're such a fucking waste of space.\n"
			"You couldn't even figure out a simple code. Your mother is disappointed in you\n"
			"\nThe correct code was:")
			for i in range(code_length):
				print(code_to_guess[i],end=" ")
			print("\n\nooft that's embarrassing.\n\n\n")
			break
		elif a==(0,code_length):
			print("\n\nCongratulations! You have guessed the code!\n\n"
			"Number of colours: {}\n"
			"Length of code: {}\n"
			"Number of guesses taken: {}\n\n\n".format(colours, code_length,turn_counter+1))

			#LEADERBOARD
			print("Current Leaderboard:\n")
			class Entry:
			    def __init__(self,name,colours,length,guesses,date):
			        self.name=name
			        self.colours=int(colours)
			        self.length=int(length)
			        self.guesses=int(guesses)
			        self.date=date


			n=name
			c=colours
			l=code_length
			g=turn_counter+1
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
			list_of_hawks=sorted(list_of_hawks, key=lambda x: x.guesses)


			#TABLEOS
			longest_name=4
			def printos(thing):
			    print(" "*(5-len(str(thing)))+str(thing),end="")

			for entry in list_of_hawks:
			    if len(entry.name)>longest_name:
			        longest_name=len(entry.name)

			print("Name"+" "*(longest_name-4)+" Gues  Col  Len  Date")
			i=0
			counter=0
			printed_hawks=[]
			while i<len(list_of_hawks):
				entry=list_of_hawks[i]
				if str(entry.length)==str(code_length) and str(entry.colours)==str(colours) and counter<20 and entry.name not in printed_hawks:
					print(entry.name+" "*(longest_name-len(entry.name)),end="")
					printos(entry.guesses)
					printos(entry.colours)
					printos(entry.length)
					print("  "+entry.date)
					printed_hawks.append(entry.name)
					counter+=1
				i+=1
			print("\n\n\n")




			break
		print(a)
		turn_counter+=1

	def play_again():
		j=input("Play again? (y/n)")
		if j=="y" or j=="Y":
			pass
		elif j=="n" or j=="N":
			sys.exit()
		else:
			print("uhh what?")
			return play_again()
	play_again()
