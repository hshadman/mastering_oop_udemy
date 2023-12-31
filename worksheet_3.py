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
    def score(self, index, score):
        #has to be in order of players
        self.scores[index] = self.scores[index] + score

    def show_score(self):
        for player in self.players:
            print(f'Player {player} has score {self.scores[self.players.index(player)]}')
        return            
    
    def play_round(self):
        #assuming 3 players in this game
        if len(self.players!=3):
            raise ValueError('expected 3 players in game')
        #each element or 'player' in the self.players list is an instance of Player() class
        all_strongest=[]
        for player in self.players:
            player.set_hand(deck.draw(2))
            all_strongest.append(player.strongest_hand())
            deck.shuffle()
        #now to find the strongest overall
        relative_rank = []
        relative_suit = []
        cards = []
        for card in all_strongest:
            cards.append(card)
            relative_rank.append(card.get_rank())
            relative_suit.append(card.get_suit())

        relative_rank = np.array(relative_rank)            
        relative_suit = np.array(relative_suit)            
        if np.unique(relative_rank).shape[0]==relative_rank.shape[0]:
            winning_card = np.where(relative_rank == max(relative_rank))[0][0]
            Game.score(winning_card,1)
            return 
        elif np.unique(relative_rank).shape[0]<relative_rank.shape[0] and np.unique(relative_rank).shape[0]>1:
            u1,c1 = np.unique(relative_rank,return_counts=True)
            non_uniq1 = u1[c1>1]
            uniq1 = u1[c1==1]
            if len(non_uniq)!=1:
                raise ValueError('something is wrong')
            if uniq1[0]>non_uniq1[0]:
                winning_card = uniq1[0]
                Game.score(winning_card,1)
                return
            elif uniq1[0]<non_uniq1[0]:
                non_uniq1_suits = relative_suit[np.where(relative_rank == non_uniq1[0])]
                winning_card = np.where(relative_suit == max(non_uniq1_suits))[0][0]
                Game.score(winning_card,1)
                return
        elif np.unique(relative_rank).shape[0] == 1:
            winning_card = np.where(relative_suit == max(relative_suit))[0][0]
            Game.score(winning_card,1)
            return 
        else:
            raise ValueError('ERROR. something is wrong.')        


        


