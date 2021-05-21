#########
# Ellisa Booker Project 1 - Engineering Computation
#########

import random

class card:
    
    def __init__(self,value=0,suit=""):
        #Define the boundaries of suit and value. Assign them as object variables. Add special OR case for Joker
        if ((suit in ["D","H","C","S"]) and (value>=1) and (value<=13)) or (suit=="J"):
            self.suit = suit
            self.value = value
        #Print error if suit or value is defined incorrectly
        else: print("Error: Enter valid suit/value")

    def display(self):
        #Initialize the string to be displayed
        myStr = ""
        
        #Values 2-10 are normal cards. Assign value as such
        if (self.value>=2) and (self.value<=10):
            myStr += str(self.value)
            
        #The following values are special cards. Assign value as such    
        elif (self.value==1):   myStr += "Ace"
        elif (self.value==11):  myStr += "Jack"
        elif (self.value==12):  myStr += "Queen"
        elif (self.value==13):  myStr += "King"

        myStr += " of "
        
        #Assign suits
        if (self.suit=="D"):    myStr += "diamonds"
        elif (self.suit=="S"):  myStr += "spades"
        elif (self.suit=="C"):  myStr += "clubs"
        elif (self.suit=="H"):  myStr += "hearts"
        
        #Display suit and value. Joker is special case
        if(self.suit == "J" ):
            print("Joker")
        else:
            print(myStr)

class deck:
    
    def __init__(self, n=0, joker = False):
        #Initialize how many cards this deck will have, and if it has a joker. False by default
        self.hasJoker = joker
        self.numberOfCards = n
        #Initialize an array of cards that will act like the deck and a counter variable to compare to numOfCards
        self.cards = []
        counter = 0
        #Create a deck of n cards
        for s in ["D","S","H","C"]:
            for v in range(1,13+1):
                #This if statement ensures that the deck only creates the specified number of cards
                if(counter < self.numberOfCards):
                    self.add_card_to_deck(v,s)
                    counter += 1
                
        
        if(self.hasJoker == bool(True)):
            #Add joker to deck if requested 
            self.add_card_to_deck(suit="J")
    
    def add_card_to_deck(self,value=0,suit=""):
        #Append a card of the given value into the cards array/deck
        self.cards.append(card(value,suit))

    def show_status(self):
        #Display all the cards in this deck as well as the number of cards left
        print("The " + str(len(self.cards)) + " cards left in this deck are: \n")
        for object in self.cards: 
            object.display()
        

    def shuffle(self):
        #Randomize cards in deck
        random.shuffle(self.cards)
        
    def deal(self):
        #Display card then remove from deck.
        self.cards[0].display()
        self.cards = self.cards[1:]
        

class hand:
    
    def __init__(self, n=5):
        #Initialize a hand by dealing n cards to it from the deck (5 default) and display the hand
        self.numOfCardsInHand = n
        self.cardsInHand = []
        
    def deal_to_me(self, d=deck(n=52)):
        #Deal n random cards from the deck (5 by default)
        cardsToPick = random.sample(range(d.numberOfCards), self.numOfCardsInHand)
        
        for i in range(0, self.numOfCardsInHand):
            self.cardsInHand.append(d.cards[cardsToPick[i]])
        
    def display(self):
        #Display all the cards in this hand as well as the number of cards
        print("The " + str(self.numOfCardsInHand) + " cards in this hand are: \n")
        for object in self.cardsInHand: 
            object.display()

def main():

    myDeck = deck(26, joker = True)  # the number can be any value between 1 and 52 (or 53 if joker is True); the joker flag can be True or False. 
    myDeck.shuffle()

    myHand = hand()
    myHand.deal_to_me( myDeck )
    
    myDeck.show_status()
    myHand.display()

if __name__ == "__main__":
    main()