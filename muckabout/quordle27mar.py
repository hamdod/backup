solutions = []

with open("words.txt") as myfi:
    listo = myfi.readlines()
    for word in listo:
        if len(word)==6 and word[1]=='a' and word[3]=='u' and word[4]=='e':
            """
            countera = 0
            counterl = 0
            countervowel = 0
            for letter in word:
                if letter == "a":
                    countera+=1
                if letter == "l":
                    counterl+=1
                if letter == "e" or letter == "o" or letter == 'u' or letter == 'p' or letter == 's' or letter == 'r' or letter == 't' or letter == 'd' or letter == 'c' or letter == 'w':
                    countervowel+=1
            if countera >= 1 and counterl >= 1 and countervowel==0:
                solutions.append(word)
            countera=0
            counterl=0
            countervowel=0
            """
            solutions.append(word)

for word in solutions:
    print(word)
    print(len(word))
