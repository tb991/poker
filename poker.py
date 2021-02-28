import random
import linecache # to select a name from a file
# strings from which to generate the 52 card deck
cards = "23456789TJQKA"
suits = "DCHS"

deck = []
#pack.append("FAKE CARD 1")
#pack.append("FAKE CARD 2")
'''
strength = random.choice(cards)
suite = random.choice(suits)

card = strength + " of " + suite
'''
def getName():
    particular_line = linecache.getline('names.txt', random.randint(1, 18238)) 
    particular_line = particular_line.replace("\n", "")
    particular_line = particular_line.replace(" ", "")
    return particular_line
#print(pack)
#print("FAKE" in pack)
# object for iterating
class Pointer:
    limit = 0
    value = 0
    changer = 0
    startVal = 0
    def __init__(self, limit, changer, defaultValue):
        self.limit - limit
        self.value = defaultValue
        self.startVal = defaultValue
        self.changer = changer
    def reset(self):
        self.value = self.startVal
    def change(self):
        self.value = self.value + self.changer
# generating ordered deck
cardsPtr = Pointer(0,-1,12)
suitsPtr = Pointer(0,-1, 3)

        
while cardsPtr.value != -1:
    card = cards[cardsPtr.value] + "" + suits[suitsPtr.value] # selected a card
    deck.append(card)
    suitsPtr.change() # changed the pointer
    if suitsPtr.value == suitsPtr.limit - 1: # if the suit pointer is exhausted then change the card pointer
        cardsPtr.change()
        suitsPtr.reset() # and reset the suit pointer
print(deck)

# instead of shuffling you can just generate a random number from 0 to 51 and select from the ordered deck
# you can then use a mutable ordered deck and take out each choice
mutableOrderedDeck = deck.copy()
def detectWinCategory():
    ["high card", "pair", "two pair", "three of a kind", "straight", 
     "flush", "full house", "four of a kind", "straight flush"]
    # high card condition: no pairs, no straights nor flushes
    # note you only need to search for those three categories above mostly
def pair(sevenCards): # if three/four of a kind this does NOT return the pair
    cards = "23456789TJQKA"
    found = [0]*len(cards)
    pairCount = 0
    cardsIndex = 0
    output = ""
    for c in cards:
        pairCount = 0
        for s in sevenCards: # suits can be ignored implicitly
            if s==c:
                found[cardsIndex] = found[cardsIndex] + 1
        cardsIndex = cardsIndex + 1
    count = 0
    for f in found:
        if f==2:
            output = output + cards[count]
            count = count + 1
    if len(output) > 1:
        return output[-1] + output[-2]
    elif len(output) == 1:
        return output
    else:
        return ""
class Robot:
    cards = "NONE" # empty
    name = ""
    def __init__(self, cardOne, cardTwo):
        self.cards = cardOne + "" + cardTwo
        self.name = getName()
    def dealTo(self, cardOne, cardTwo):
        self.cards = cardOne + "" + cardTwo
    def showCards(self):
        print(self.cards, end=" ")
        return self.cards
def newCardFromDeck():
    choice = random.randint(0,len(mutableOrderedDeck) - 1)
    newCard = mutableOrderedDeck.pop(choice)
    return newCard

class Player:
    cards = "NONE"
    name = ""
    def __init__(self, cardOne, cardTwo):
        self.cards = cardOne + "" + cardTwo
        self.name = getName()
    def dealTo(self, cardOne, cardTwo):
        self.cards = cardOne + "" + cardTwo
    def showCards(self):
        print(self.cards, end=" ")
        return self.cards

def cardVal(cardSymbol):
    global cards
    return cards.index(cardSymbol)
def newDeck():
    mutableOrderedDeck = deck
robotPlayers = 0

table = [] # no human or robot by default
humanPlayers = 0
def addRobot(hisCards):
    global robotPlayers 
    global table
    if robotPlayers == 8:
        print("max players reached")
    else:
        robotPlayers = robotPlayers + 1
        if hisCards=="GENERATE":
            robot = Robot(newCardFromDeck(), newCardFromDeck())
        elif hisCards!="GENERATE":
            robot = Robot(hisCards[0] + hisCards[1], hisCards[2] + hisCards[3])
        table.append(robot)
        
dealt = []
 
def deal():
    global dealt
    if len(dealt)==0:
        # flop
        dealt.append(newCardFromDeck())
        dealt.append(newCardFromDeck())
        dealt.append(newCardFromDeck())
        print(dealt)
    elif len(dealt)==3:
        # turn
        dealt.append(newCardFromDeck())
        print(dealt)
    elif len(dealt)==4:
        # river
        dealt.append(newCardFromDeck())
        print(dealt)
    elif len(dealt)==5:
        # reset
        dealt = []

def whoWon(): # this assumes betting is over, so 5 cards needed on dealt
    global dealt
    out = []
    while len(dealt) != 5:
        deal()
    #print(dealt)
    out.append(dealt)
    for a in table:
        #print(a.showCards())
        out.append(a.showCards)
        

# i'm going to create a function for every "victory category" *pair, two pair, flush etc"
# that returns a value indicating whether it has been detected
# then i will need to give each card a value and see who wins when categories are equal

# returns the value of the highest pair

# ---game simulation---
gameState = "empty"
while True:
    print("There are " + str(len(table)) + " players and the game is in state: " + gameState)
    for p in table:
        print(p.name, end = " ")
    print("")
    for p in table:
        p.showCards()
    a = input("\nEnter command: ")
    if a=="add":
        a = input("human (h) or robot (r)?")
        if a=="h":
            humanPlayers = humanPlayers + 1
            human = Player(newCardFromDeck(), newCardFromDeck())
            table.append(human)
        elif a=="r":
            addRobot("GENERATE")
        elif a=="c": # custom, must be no prior humans or robots because i need to select cards
            a = input("Enter cards (AHKC == ace of hearts, king of clubs): ")
            # no error detection for input as it is cumbersome. must be uppcase and format in here
            addRobot(a)
            mutableOrderedDeck.remove(a[0] + a[1])
            mutableOrderedDeck.remove(a[2] + a[3])
    elif a=="rem": #(remove)
        a = input("enter their table position: (up to " + str(len(table)))
        a = input("")
    elif a=="dea": # deal
        deal()
    elif a=="dec": # deck (show it)
        print(mutableOrderedDeck)
        print(deck)
    elif a=="res": # restart
        print(mutableOrderedDeck)
    elif a=="win": # apply win detections
        for p in table:
            x = p.cards
            y = ""
            y = y.join(dealt)
            if len(pair(x + y))==1:
                print(p.name + " has one pair")
            elif len(pair(x + y))>1:
                print(p.name + " has a two pair")
