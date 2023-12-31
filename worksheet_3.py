from enum import Enum
import random
import numpy as np

#Problem 1
#explain the differences between the attributes firstname, lastname and job. 
#What values can they have for different instances of the class?
class Hanks:
    lastname = "Hanks"
    job = "software engineer"
    def __init__(self, firstname, job = None):
        self.firsname = firstname
        if job is not None:
            self.job = job
#Answer: lastname is a class attribute, it will be the same value for all instances of the class
#unless we change it 
#firstname and job are both instance attribute and we will manually set the value of these
#for every instance

#Problem 2

#classes already created
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
    def set_hand(self, hand):
        # each hand is expected to be PlayingCard class instance
        self._hand = hand
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
        self._cards = shuffled_deck
        return shuffled_deck
    def draw(self,n):
        current_cards = self.get_cards()
        if len(current_cards)<n:
            return print('None')
        else:
            j=1
            drawn_cards = []
            for card_iter in range(n):
                drawn_cards.append(current_cards[(-1)*j])
                j += 1    
            updated_deck = [card for card in current_cards if card not in drawn_cards]
            self._cards = updated_deck
            return drawn_cards


class Game:
    
    
    def __init__(self, players, deck):
        #assuming 3 players
        self._players = players #list of players in the game
        self._scores = {}
        self._deck = deck
        # initialize the scores to zeros
        for p in players:
            self._score[p.get_name()] = 0

    def show_score(self):
        print("Score:")
        print("-----")
        for k, v in self._score.items():
            print(f'{k}: {v}')
        print('\n')
        
    
    def play_round(self):
        winning_card = None
        winning_player = None
        for p in self._players:
            hand = self._deck.draw(2)
            p.set_hand(hand)
            print(f'player {p.get_name()} is dealt [{hand[0]},
                  {hand[1]}]')
            if winning_card is None or (
                p.strongest_card().get_rank() > winning_card.get_rank()
            ) or (
                (p.strongest_card().get_rank() == winning_card.get_rank())
                and (p.strongest_card().get_suit().value > winning_card.get_suit().value)
            ):
                winning_card = p.strongest_card()
                winning_player = p
        print(f'PLAYER {winning_player.get_name()} WINS THIS ROUND\n')
        self._score[winning_player.get_name()] += 1
        self.show_score()


        

        


