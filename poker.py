import random
# note there may be an error when there's a straight and a flush
# in that the straight will be identified yet the flush will be shown for its cards...

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
'''
def getName():
    particular_line = linecache.getline('names.txt', random.randint(1, 18238)) 
    particular_line = particular_line.replace("\n", "")
    particular_line = particular_line.replace(" ", "")
    return particular_line
'''
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
#print(deck)

# instead of shuffling you can just generate a random number from 0 to 51 and select from the ordered deck
# you can then use a mutable ordered deck and take out each choice
mutableOrderedDeck = deck.copy()
# sames() just returns the number of occurences of each card from 2 to Ace
# it can be used to find pairs, 3oaK, 4oaK and full house
def sames(sevenCards, ofAKindNum): 
    cards = "23456789TJQKA"
    found = [0]*len(cards)
    cardsIndex = 0
    output = ""
    # making an array of found counts for what cards appear for player
    for c in cards:
        for s in sevenCards: # suits can be ignored implicitly
            if s==c:
                found[cardsIndex] = found[cardsIndex] + 1
        cardsIndex = cardsIndex + 1
    count = 0
    for f in found:
        if f==ofAKindNum:
            output = output + cards[count]
        count = count + 1
    return output[::-1]
def straightCheck(sevenCards): 
    cards = "A23456789TJQKA"
    found = [0]*len(cards)
    linked = 0
    cardsIndex = 0
    output = ""
    finalCardIndex = -1
    for c in cards:
        for s in sevenCards: # suits can be ignored implicitly
            if s==c:
                found[cardsIndex] = found[cardsIndex] + 1
        cardsIndex = cardsIndex + 1
    for f in range(0,len(found)):
        if cards[f]=="J":
            break # because this is exceeding the highgest straight
        linked = 0
        for c in range(0,5):
            if found[f + c]>0:
                linked = linked + 1
                if linked == 5:
                    finalCardIndex = f + c
                    #print("KABOOM")
    #print(found)
    output = ""
    if finalCardIndex != -1:
        output = cards[finalCardIndex-4:finalCardIndex+1]
    #print(output)
    return output[::-1]
def flushCheck(sevenCards): # if three/four of a kind this does NOT return the pair
    cards = "23456789TJQKA"
    suits = "DCHS"
    suitCount = [0]*len(suits)
    for c in sevenCards:
        for s in range(0,len(suits)):
            if c==suits[s]:
                suitCount[s] = suitCount[s] + 1
    flushFound = False
    flushSuit = ""
    #print(suitCount)
    for a in suitCount:
        if a > 4:
            flushFound = True
            flushSuit = suits[suitCount.index(a)]
    #print(flushSuit)
    # find the highest of flush suit
    captured = "" # cards that are suited in flush
    for c in range(0,len(sevenCards)):
        if sevenCards[c]==flushSuit:
            captured = captured + sevenCards[c-1]
    #print(captured)
    ordCapt = "" # ordered version of flush cards
    for a in reversed(cards):
        for b in captured:
            if a==b:
                ordCapt = ordCapt + a
    return ordCapt[:5]
class Robot:
    cards = "NONE" # empty
    def __init__(self, cardOne, cardTwo):
        self.cards = cardOne + "" + cardTwo
    def dealTo(self, cardOne, cardTwo):
        self.cards = cardOne + "" + cardTwo
    def showCards(self):
        #print(self.cards, end=" ")
        return self.cards
def newCardFromDeck():
    choice = random.randint(0,len(mutableOrderedDeck) - 1)
    newCard = mutableOrderedDeck.pop(choice)
    return newCard
''' # not really needed. just need custom or robot
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
'''
def cardVal(cardSymbol):
    global cards
    return cards.index(cardSymbol)
def newDeck():
    mutableOrderedDeck = deck

table = [] # no human or robot by default
def addRobot(hisCards):
    global table
    if hisCards=="GENERATE":
        robot = Robot(newCardFromDeck(), newCardFromDeck())
        #print("ROBOT ADDED WITH GENERATED CARDS")
        table.append(robot)
    elif hisCards!="GENERATE":
        robot = Robot(hisCards[0] + hisCards[1], hisCards[2] + hisCards[3])
        mutableOrderedDeck.remove(hisCards[0] + hisCards[1])
        mutableOrderedDeck.remove(hisCards[2] + hisCards[3])
        table.append(robot)
        #print("ROBOT ADDED WITH CUSTOM CARDS")
        #robot.showCards()
dealt = []
 
def deal():
    global dealt
    if len(dealt)==0:
        # flop
        dealt.append(newCardFromDeck())
        dealt.append(newCardFromDeck())
        dealt.append(newCardFromDeck())
        #print(dealt)
    elif len(dealt)==3:
        # turn
        dealt.append(newCardFromDeck())
        #print(dealt)
    elif len(dealt)==4:
        # river
        dealt.append(newCardFromDeck())
        #print(dealt)

# i'm going to create a function for every "victory category" *pair, two pair, flush etc"
# that returns a value indicating whether it has been detected
# then i will need to give each card a value and see who wins when categories are equal

# returns the value of the highest pair

# ---game simulation---
# returns the score for each hand for how good it is according to high cards standard
def handRanks(allHands5):
    betterCount = [0]*len(allHands5)
    n = 0
    for h in allHands5:
        for h2 in allHands5:
            if h==h2:
                continue
            betterCount[n] += higher(h2, h)
        n += 1
    #print(betterCount)
def higher(cards5one, cards5two):
    x = ""
    y = ""
    for n in range(1,6):
        x = x + highest(cards5one, n)
        y = y + highest(cards5two, n)
    if x==y:
        return "same"
    Ato2 = "AKQJT98765432"
    for n in range(0,len(cards5one)):
        a = x[n]
        b = y[n]
        if Ato2.index(a) < Ato2.index(b):
            return 0
        elif Ato2.index(a) > Ato2.index(b):
            return 1
        elif Ato2.index(a) == Ato2.index(b):
            continue   
# get the highgest or nth high number from a string of unordered cards
# very useful method
def highest(cardsString, n):
    cards = "AKQJT98765432"
    found = ""
    for x in cards:
        for y in cardsString:
            if x==y:
                found += x
    #print(cardsString)
    return found[n-1]
    
def handCategory(hand7):
    flush = len(flushCheck(hand7))==5
    straight = len(straightCheck(hand7))==5
    four = len(sames(hand7, 4))==1
    three = len(sames(hand7, 3))>0 # used for full house too...
    twop = len(sames(hand7, 2))==2
    two = len(sames(hand7, 2))==1
    # note straight flush has awkward conditions
    out = "high card"
    if two:
        out = "pair"
    elif twop:
        out = "two pair"
    if three and (two or twop):
        out = "full house"
    elif three and not (two or twop):
        out = "three of a kind"
    elif four:
        out = "four of a kind"
    if straight:
        out = "straight"
    elif flush:
        out = "flush"
    if sfCheck(hand7):
        out = "straight flush"
    return out
def show():
    for x in table:
        print(x.showCards(), end=" ")
    print()
def flushSuit(sevenCards):
    # there must be mostly this suit, so that reduces the problem massively
    suits = ["S","H","C","D"]
    countS = [0]*len(suits)
    idx = 0
    for suit in suits:
        for cardElement in sevenCards:
            if suit==cardElement:
                countS[idx] += 1
        idx += 1
    fSuit = -1
    for a in range(0,len(suits)):
        if countS[a] == 5:
            fSuit = a
    if fSuit == -1:
        return ""
    else:
        return suits[fSuit]
def sfCheck(sevenCards):
    suit = flushSuit(sevenCards)
    usedCardVals = straightCheck(sevenCards)
    outCount = 0
    idx = 0
    for cardElement in sevenCards:
        for cardVal in usedCardVals:
            if cardVal == cardElement:
                # the suit will be to its right
                if sevenCards[idx + 1] == suit:
                    outCount = outCount + 1
        idx += 1
    return outCount == 5       
# these are for strength evaluation between matching results, to prevent false draws being decided   
# it works with highest() 
def relevantCardsHC(cards, numToTake):
    x = ""
    for i in range(1,numToTake+1):
        x = x + highest(cards, i)
    return x
def relevantCardsPair(sevenCards):
    pairC = sames(sevenCards, 2)
    x = sevenCards.replace(pairC, "")
    x = relevantCardsHC(x,3)
    return pairC + pairC + x
def relevantCardsTwoPair(sevenCards):
    pairC = sames(sevenCards, 2)
    x = sevenCards.replace(pairC[0], "")
    x = x.replace(pairC[1], "")
    x = relevantCardsHC(x,1)
    return pairC[0]*2 + pairC[1]*2 + x
def relevantCardsThreeOfAKind(sevenCards): # breaks easy but works for good input
    thr = sames(sevenCards, 3)
    x = sevenCards.replace(thr[0], "")
    x = relevantCardsHC(x,2)
    return thr[0]*3 + x
def relevantCardsFullHouse(sevenCards):
    pairC = sames(sevenCards, 2)
    thr = sames(sevenCards, 3)
    x = sevenCards.replace(pairC[0], "")
    x = x.replace(thr, "")
    return thr*3 + pairC[0]*2
def relevantCardsFourOfAKind(sevenCards): # breaks easy but works for good input
    fou = sames(sevenCards, 4)
    x = sevenCards.replace(fou, "")
    x = relevantCardsHC(x,1)
    return fou*4 + x
# straightCheck and flushCheck already do this so not needed here

# what i really need is two lists the same size as the number of players
# and for the first list to contain the name of the result each gets with cards on table
# and the next list to give a integer for its rank and result number

def final(hands, tableCs):
    winOrder = ["high card", "pair", "two pair", "three of a kind", "straight", "flush",
                    "full house", "four of a kind", "straight flush"]
    sevens = []
    for h in hands:
        sevens.append(h + "".join(tableCs))
    categs = []
    print(sevens)
    for s in sevens:
        categs.append(handCategory(s))
    print(categs)
    # we now have the name of the result each player gets
    # so we need to only focus on the top kind because they win
    # but remember that could be everyone
    strongest = ""
    for kind in winOrder:
        for result in categs:
            if kind==result:
                strongest = kind
    winKind = strongest
    winners = []
    count = 0
    for w in categs:
        if w==winKind:
            winners.append(categs[count])
        count = count + 1
    # now compare them all    
    print("winners: " + str(winners))
    winCount = [0]*len(winners)
    for w in range(0,len(winners)-1):
        for x in range(0,len(winners)-1):
            if x<=w:
                continue
            else:
                winCount[w] += higher(winners[x], winners[w])         
    w = max(winCount)
    idx = 0
    finalWinners = [] # will contain indexes of winners
    for a in winCount:
        if a==w:
            finalWinners.append(a)
        idx = idx+1
    return finalWinners
def make():
    addRobot("GENERATE")
    addRobot("GENERATE")
    addRobot("GENERATE")
    deal()
    deal()
    deal()
    show()
    print(dealt)
    final([table[0].showCards(), table[1].showCards(), table[2].showCards()], dealt)
