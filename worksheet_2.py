from enum import Enum
from itertools import product

#Problem 1

#got those wrong. trailing underscore more than 2 prevents name mangling
#you canc create new attributes for instances of a class

#Problem 2
class suits(Enum):
      SPADES   = 3
      HEARTS   = 2
      DIAMONDS = 1
      CLUBS    = 0

class PlayingCard:
    def __init__(self,rank,suit):
        if rank in [i for i in range(2,15)]:
            self._rank = rank
        elif rank == 'Jack':
	        self._rank = 11
        elif rank == 'Queen':
	        self._rank = 12
        elif rank == 'King':
    	    self._rank=13
        elif rank == 'Ace':
	        self._rank=14
        else:
            raise ValueError('ERROR. Ranks can range from 2 to 14 inclusive or be one of these choices: Jack, Queen, King or Ace')
            
        if suit == 'SPADES':
            self._suit = suits.SPADES.value
        elif suit == 'HEARTS':
            self._suit = suits.HEARTS.value
        elif suit == 'DIAMONDS':
            self._suit = suits.DIAMONDS.value            
        elif suit == 'CLUBS':
            self._suit = suits.CLUBS.value            
        else:
            raise ValueError('ERROR. Suits can only be SPADES, HEARTS, DIAMONDS or CLUBS') 
    def get_rank(self):
         return self._rank
    def get_suit(self):
         return self._suit


class Player:
    def __init__(self,name,hand):        
        self._name = name
        self._hand = []
    def set_hand(self, hand):
        if (self._hand)>2:
            raise ValueError('ERROR, more than 2 hands')
        else:
            return self._hand.append(hand)
    def get_name(self):
        return self._name
    def get_hand(self):
        return self._hand
    def strongest_hand():
        
class Deck:
    def __init__(self):
        ranks = range(2,15)
        suits = ['SPADES','HEARTS','DIAMONDS','CLUBS']
        card_combinations = list(product(ranks,suits))
        self._cards = []
        for card in card_combinations:
            self._cards.append(PlayingCard(card[0],card[1]))
    def get_cards(self):
         return self._cards

#Problem 3