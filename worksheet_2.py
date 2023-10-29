from enum import Enum
import random


#Problem 1

#got those wrong. trailing underscore more than 2 prevents name mangling
#you canc create new attributes for instances of a class

class Suit(Enum):
    SPADES = 4
    HEARTS = 3
    DIAMONDS = 2
    CLUBS = 1
class PlayingCard:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    def get_rank(self):
        return self._rank
    def get_suit(self):
        return self._suit

class Player:
    def __init__(self,name):
        self._name = name
        self._hand = []
    def get_name(self):
        return self._name
    def get_hand(self):
        return self._hand
    def set_hand(hand):
        # each hand is expected to be PlayingCard class instance
        self._hand.append(hand)
        if len(self._hand)>2:
            raise ValueError('hands more than 2')
        return print('the hand is now', self._hand)
    def strongest_hand(self):
        relative_rank = []
        relative_suit = []
        cards = []
        for card in self.get_hand():
            cards.append(card)
            relative_rank.append(card.get_rank())
            relative_suit.append(card.get_suit())
        if relative_rank[0]>relative_rank[1]:
            return cards[0]
        elif relative_rank[0]<relative_rank[1]:
            return cards[1]
        elif relative_rank[0]==relative_rank[1]:
            if relative_suit[0]>relative_suit[1]:
                return cards[0]
            elif relative[0]<relative_suit[1]:
                return cards[1]
            else:
                raise ValueError('ERROR. something is wrong.')
class Deck:
    def __init__(self):
        self._cards = []
        for i in range(13):
            self._cards.append(PlayingCard(i+2,Suit.SPADES))
            self._cards.append(PlayingCard(i+2,Suit.DIAMONDS))
            self._cards.append(PlayingCard(i+2,Suit.HEARTS))
            self._cards.append(PlayingCard(i+2,Suit.CLUBS))
    def get_cards(self):
        return self._cards
    def shuffle(self):
        current_cards = self.get_cards()
        current_cards_indices = [i for i in range(0,len(current_cards))]
        random.shuffle(current_cards_indices)
        shuffled_deck = [current_cards[index] for index in current_cards_indices]
        return shuffled_deck

    
#problem 5