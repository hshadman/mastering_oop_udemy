from enum import Enum
import random
import numpy as np

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
        return f"({self.get_rank()},{str(self.get_suit().name)})"
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

#cheater class is an inheritance of player class
#cheater class only changing the strongest hand
class Cheater(Player):
    def strongest_hand(self):
        if random.randint(1,10)<=2:
            return PlayingCard(14,Suit.SPADES)
        else:
            return super().strongest_card()
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

#problem 1
#problem 2        
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
        
    
    def __play_round(self):
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
    def play(self):
        #method doesn't return anything



        

