from enum import Enum
from itertools import product
class Person:
    def __init__(self, name="Messi"):
        self.name = name

#problem 1
p = Person()
print(p.name)

#problem 2
p = Person()
p.name = "CR7"
print(p.name)

#problem 3
p = Person("CR7")
print(Person().name)

#Problem 4
print('starting problem 4')
p1 = Person()
p2 = Person()
print(p1 is p2) #probably not True
p1 = Person("CR7")
p2 = Person("CR7")
print(id(p1) != id(p2)) #probably True
print(id(Person) == id(Person())) # probably not true

#Problem 5

#brainstorming objects for the MaxHandWind capstone project
#an object that maintains the remaining deck of cards
#an object that identifies winner of a selected round
#an object that randomly picks 3 cards from the deck for the three players
#an object that keeps score of the players and eventually decides winner of the game

#Problem 6

class suits(Enum):
      SPADES   = 3
      HEARTS   = 2
      DIAMONDS = 1
      CLUBS    = 0

class PlayingCard:
    def __init__(self,rank,suit):
        if rank in [i for i in range(2,15)]:
            self.rank = rank
        elif rank == 'Jack':
	        self.rank = 11
        elif rank == 'Queen':
	        self.rank = 12
        elif rank == 'King':
    	    self.rank=13
        elif rank == 'Ace':
	        self.rank=14
        else:
            raise ValueError('ERROR. Ranks can range from 2 to 14 inclusive or be one of these choices: Jack, Queen, King or Ace')
            
        if suit == 'SPADES':
            self.suit = suits.SPADES.value
        elif suit == 'HEARTS':
            self.suit = suits.HEARTS.value
        elif suit == 'DIAMONDS':
            self.suit = suits.DIAMONDS.value            
        elif suit == 'CLUBS':
            self.suit = suits.CLUBS.value            
        else:
            raise ValueError('ERROR. Suits can only be SPADES, HEARTS, DIAMONDS or CLUBS') 


#Problem 7
class Player:
    def __init__(self,name,hand):        
        self.name = name
        list_of_cards=[]
        list_of_cards.append(hand)
        self.hand = list_of_cards
    def add_card(self,list_of_cards,card):
         list_of_cards.append(card)
         self.hand = list_of_cards

class Deck:
    def __init__(self):
        ranks = range(2,15)
        suits = ['SPADES','HEARTS','DIAMONDS','CLUBS']
        card_combinations = list(product(ranks,suits))
        self.cards = []
        for card in card_combinations:
            self.cards.append(PlayingCard(card[0],card[1]))     
        

p1 = Deck()

print(len(p1.cards))