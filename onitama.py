import random

#Initialising the cards
cards_moves = {"tiger":["f2","b1"],"dragon":["f1l2","f1r2","b1l1","b1r1"],"frog":["f1l1","l2","b1r1"],"rabbit":["f1r1","r2","b1l1"],
"crab":["f1","l2","r2"],"elephant":["f1l1","f1r1","l1","r1"],"goose":["f1l1","l1","r1","r1b1"],"rooster":["f1r1","l1","r1","b1l1"],
"monkey":["f1l1","f1r1","b1l1","b1r1"],"mantis":["f1l1","f1r1","b1"],"horse":["f1","l1","b1"],"ox":["f1","r1","b1"],
"crane":["f1","b1l1","b1r1"],"boar":["f1","l1","r1"],"eel":["f1l1","r1","b1l1"],"cobra":["f1r1","l1","b1r1"]
}
cards = ["tiger","dragon","frog","rabbit","crab","elephant","goose","rooster","monkey","mantis","horse","ox","crane","boar","eel","cobra"]
game_grid=[1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,4,3,3] #blue is 1,2 red is 3,4, squares with 0 have nobody on them
whose_turn = random.randint(0,1) #blue is 0, red is 1
game_over = 0

#Randomly distributing the cards
blue_cards=[]
red_cards=[]
middle_card=[]

for i in range(5):
    add = cards[random.randint(0,15-i)]
    if i==0 or i==1:
        blue_cards.append(add)
    elif i==2:
        middle_card.append(add)
    else:
        red_cards.append(add)
    cards.remove(add)
print(blue_cards)
print(middle_card)
print(red_cards)


def play_card(player,card):
    if player == 0:
        for i in middle_card:
            blue_cards.append(i)
        blue_cards.remove(card)
    if player == 1:
        for i in middle_card:
            red_cards.append(i)
        red_cards.remove(card)
    middle_card.append(card)
    return True

def where_to(player):
    p = None
    if player==0:
        p = "Blue"
    if player==1:
        p = "Red"
        print(p+" player's turn: where would you like to go?\n"
        "First enter the card you would like to use, then the move coordinates.\m"
        "Please leave your answer in the form AABB, where AA are the coordinates of the square you are"
        " moving from, and BB are the coordinates of the square you are moving to.\n")
    boo = True
    while boo:
        card = input()
        movement = input()

def coordinate_conversion(str):
    if len(str)!=4:
        



def move( player, fro, to, card ):
    if player==0:
        if card not in blue_cards:
            print("Invalid move: you don't have that card.")
            return False
        if game_grid[fro]!="b" and game_grid[fro]!="B":
            print("Invalid move: you don't have a piece on that square.")
        #if game_grid[to]
        return

def turn(player, ):
    print
    turn( (player-1)*(player-1),  )
