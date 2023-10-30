from enum import Enum
import random

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
    def __init__(self, players):
        #assuming 3 players
        self.players = players #list of players in the game
        self.scores = [0,0,0]
    
    def deck(self):
        #supposed to be an instance of the Deck class
        self.deck = Deck()
    def score(n1,n2,n3):
        #has to be in order of players
        self.scores[0] = self.scores[0] + n1
        self.scores[1] = self.scores[1] + n2
        self.scores[2] = self.scores[2] + n3
    
    def show_score(self):
        for player in self.players:
            print(f'Player {player} has score {self.scores[self.players.index(player)]}')
        return            
    
    def play_round(self):
        start_deck = deck(Deck)
