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
def straightCheckSP(sevenCards): 
    cards = "A23456789TJQKA"
    suits = ["S", "H", "C", "D"]
    out = straightCheck(sevenCards)[::-1]
    #print(out)
    suitsy = ""
    for finalCard in out:
        pos = 0
        for realCard in sevenCards:
            if finalCard == realCard:
                #print(pos+1)
                #print(len(sevenCards))
                if (pos+1)<len(sevenCards):
                    suitsy += sevenCards[pos + 1]
            pos = pos + 1
    y = ""
    #print(suitsy)
    for x in range(0,len(out)):
        y += out[x] + suitsy[x]
    return y
            
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
def flushCheckSP(sevenCards): 
    cards = "A23456789TJQKA"
    suits = ["S", "H", "C", "D"]
    out = flushCheck(sevenCards)
    #print(out)
    suitsy = ""
    for finalCard in out:
        pos = 0
        for realCard in sevenCards:
            if finalCard == realCard:
                #print(pos+1)
                #print(len(sevenCards))
                if (pos+1)<len(sevenCards):
                    suitsy += sevenCards[pos + 1]
            pos = pos + 1
    y = ""
    #print(suitsy)
    for x in range(0,len(out)):
        y += out[x] + suitsy[x]
    return y
            
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
        #print([cards5one, n]) cards5one comes up as empty string error 04/03/2021, should be length 10 and cards
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
def getFinalHand(sevenCards): # this function will help me further determine a winner
    winOrder = ["high card", "pair", "two pair", "three of a kind", "straight", "flush",
                    "full house", "four of a kind", "straight flush"]
    kind = handCategory(sevenCards)
    out = ""
    if kind==winOrder[0]:
        out = firstFiveSP(sevenCards, "")
    if kind==winOrder[1]:
        x = relevantCardsPair(sevenCards)
        #print(x)
        out = firstFiveSP(sevenCards, x[0])
    if kind==winOrder[2]:
        x = relevantCardsTwoPair(sevenCards)
        #print(x)
        out = firstFiveSP(sevenCards, x[0] + x[2])
    if kind==winOrder[3]:
        x = relevantCardsThreeOfAKind(sevenCards)
        #print(x)
        out = firstFiveSP(sevenCards, x[0])
    if kind==winOrder[4]:
        out = straightCheckSP(sevenCards)
        #print(x)
    if kind==winOrder[5]:
        out = flushCheckSP(sevenCards)
    if kind==winOrder[6]:
        x = relevantCardsPair(sevenCards)
        y = relevantCardsThreeOfAKind(sevenCards)
        out = firstFiveSP(sevenCards, x[0] + y[0])
    if kind==winOrder[7]:
        x = relevantCardsFourOfAKind(sevenCards)
        out = firstFiveSP(sevenCards, x[0])
    if kind==winOrder[8]:
        suit = flushSuit(sevenCards)
        out = straightCheckSP(sevenCards)
        #print(x)
    return out
    # note after this (not here) we need just to remove the suits from the list after using this function
    # and then to compare them using higher()

# gets the five relevant cards from the seven provided
def firstFiveSP(cardsString, precludeCards): # SP = suit preservation
    cards = "AKQJT98765432"
    found = ""
    count = 0
    for y in precludeCards:
        idx = -1
        for x in cardsString:
            idx = idx + 1
            if x==y:
                #print(found)
                found += x + cardsString[idx+1]
                count += 1
                if count==5:
                    return found
    for x in precludeCards: # remove preclude cards from what is about to be added
        cards = cards.replace(x, "")
    for x in cards:
        idx = -1
        for y in cardsString:
            idx = idx + 1
            if x==y:
                found += x + cardsString[idx+1]
                count = count + 1
                if count==5:
                    return found
    #print(cardsString)
    return found
def handCategory(hand7):
    flush = len(flushCheck(hand7))==5
    straight = len(straightCheck(hand7))==5
    four = len(sames(hand7, 4))==1
    three = len(sames(hand7, 3))>0 # used for full house too...
    twop = len(sames(hand7, 2))>1
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
def sfCheckSP(sevenCards):
    suit = flushSuit(sevenCards)
    count = 0
    cards = ""
    for a in sevenCards:
        if a==suit:
            cards += sevenCards[count-1] + suit
        count += 1
    #print(cards)
    x = straightCheckSP(cards)
    return x

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
    
def makeList(cards):
    suits = ["S", "H", "C", "D"]
    suitsFound = ""
    cardsValsFound = ""
    for c in cards:
        for s in suits:
            if c==s:
                suitsFound += c
    for c in cards:
        count ==0
        for s in suits:
            if c!=s:
                count += 1
            if count==4:
                cardsValsFound += s
    out = []
    c = 0
    while c<0:
        out.append(cardsValsFound[c] + suitsFound[c])
    return out
def listsEquivalent(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        matchFound = ""
        for c in list1:
            for c2 in list2:
                if c==c2:
                    matchFound += "F"
                    break
        matchFoundR = ""
        for c2 in list2:
            for c1 in list1:
                if c1==c2:
                    matchFound += "M"
                    break
        return matchFound=="F"*len(list1) + "M"*len(list2)
# straightCheck and flushCheck already do this so not needed here
def game(startingHand, opponents, timesToRun):
    wins = 0
    draws = 0

    while timesToRun > 0:
        timesToRun = timesToRun - 1
        cards = []
        card = "NONE"
        while len(cards)<(opponents*2 + 5):
            card = getCard()
            if cards.count(card)!=0:
                continue
            else:
                # it's a new card
                cards.append(card)
        print([cards[0:opponents*2],"".join(cards)[-10:]])
        final(cards[0:opponents*2],"".join(cards)[-10:])
def getCard():
    cards = "23456789TJQKA"
    suits = "DCHS"
    return random.choice(cards) + random.choice(suits)
def final(hands, tableCs):
    winOrder = ["high card", "pair", "two pair", "three of a kind", "straight", "flush",
                    "full house", "four of a kind", "straight flush"]
    sevens = []
    for h in hands:
        sevens.append(h + "".join(tableCs))
    categs = []
    #print(sevens)
    for s in sevens:
        categs.append(handCategory(s))
    #print(categs)
    # we now have the name of the result each player gets
    # so we need to only focus on the top kind because they win
    # but remember that could be everyone
    z = ""
    for x in winOrder: # because of the order of winOrder, this loop will select the winning category
        for y in categs:
            if x==y:
                z=x
    # we now need to see which players get that result
    idx = 0
    potentials = []
    for x in categs:
        if x==z:
            potentials.append(idx)
        idx += 1
        
    potentialsCards = []
    for x in potentials:
        potentialsCards.append(sevens[x])
    count = len(potentials)
    # 
    idx = 0
    print(categs)
    for x in potentialsCards:
        potentialsCards[idx] = getFinalHand(x)
        #print(potentialsCards)
        idx += 1
    print(potentialsCards)
    while count != 0 and idx != None:
        #print(potentialsCards)
        idx = loser(potentialsCards)
        #print(idx)
        if idx != 'none' and idx != None:
            potentialsCards.pop(idx)
            potentials.pop(idx)
            #print(potentialsCards)
        count = count -1
    #rint("List of winning hands: " + str(potentialsCards))
    return potentials
        
# find a hand that loses 
def loser(potentials):
    if len(potentials)==1:
        return None
    for x in range(0,len(potentials)):
        for y in range(0,len(potentials)):
            if x==y:
                continue
            else:
                z = [potentials[x],potentials[y]] # error here 04/03/2021, two empty strings
                #print(z)
                z = higher(z[0],z[1])
                if z==1:
                    loser = x
                    return loser
                elif z==0:
                    loser = y
                    return loser
                elif z=='same':
                    loser = 'none'
    # then output the ones left over
def draw(cardsList):
    a = len(potentialsCards)
    countEquiv = 0
    for x in range(0,a):
        for y in range(0,a):
            if x<=y:
                continue
            else:
                X = potentialsCards[x]
                Y = potentialsCards[y]
                X = makeList[X]
                Y = makeList[Y]
                same = listsEquivalent[X,Y]
                countEquiv+=1
def make(numOpps, startingHand):
    addRobot(startingHand)
    while numOpps >0:
        addRobot("GENERATE")
        numOpps-=1
    deal()
    deal()
    deal()
    hands = []
    for n in table:
        hands.append(n.showCards())
    #print(hands)
    #print(dealt)
    res = final(hands, "".join(dealt))
    
    return res.count(0)
