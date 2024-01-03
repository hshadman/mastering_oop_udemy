from enum import Enum
import random
import numpy as np
#from functools import total_ordering

#classes already created
class Suit(Enum):
    SPADES = 4
    HEARTS = 3
    DIAMONDS = 2
    CLUBS = 1    

#problem 1 modification 
class PlayingCard:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit
    def __eq__(self, other):
        return self.get_rank() == other.get_rank() and self.get_suit() == other.get_suit()
    def __gt__(self, other):
        if self.get_rank()!=other.get_rank():
            return self.get_rank() > other.get_rank() 
        else:
            return self.get_suit() > other.get_suit()
    def __lt__(self, other):
        if self.get_rank()!=other.get_rank():
            return self.get_rank() < other.get_rank() 
        else:
            return self.get_suit() < other.get_suit()    
    def __str__(self):
        return f"({self.get_rank()},{str(self.get_suit()).split('.')[1]})"

#problem 3
card = PlayingCard(9, Suit.SPADES)
print(card)

#problem 2 modification
class Player:
    def __init__(self,name):
        self._name = name
        self._hand = []
    def get_name(self):
        return self._name
    def get_hand(self):
        return self._hand
    def set_hand(self, hand):
        # each hand is expected to be PlayingCard class instance
        self._hand = hand
        if len(self._hand)>2:
            raise ValueError('hands more than 2')
        return print('the hand is now', self._hand)
    def strongest_hand(self):
        if self.get_hand()[0] > self.get_hand()[1]:
            return self.get_hand()[0]
        elif self.get_hand()[1] > self.get_hand()[0]:
            return self.get_hand()[1]
        else:
            return print('there is a problem')

