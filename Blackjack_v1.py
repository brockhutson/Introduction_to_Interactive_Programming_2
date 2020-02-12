# -*- coding: utf-8 -*-
"""

@author: Brock
python 2.7

http://www.codeskulptor.org/#user46_JukKpPKZiD_45.py

This is an a game of Blackjack created using Codeskulptor.
"""

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
cards = ""
deck_card = ""


# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, 
                          card_loc, 
                          CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0],  
                           pos[1] + CARD_CENTER[1]], 
                           CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.card_field = []

    def __str__(self):
        cards = ""
        if len(self.card_field) > 0:
            for i in range(len(self.card_field)):
                cards += str(self.card_field[i]) + " "
            return "Hand contains " + str(cards)
        else:
            return "Hand contains"
        
    def add_card(self, card):
        self.card_field.append(card)

    def get_value(self):
        total = 0
        ace = False
        if len(self.card_field) == 0:
            return total
        for self in self.card_field:
            total += VALUES[self.rank]
            if self.rank == 'A':
                ace = True
        if ace and total <= 11:
            return total + 10
        else:
            return total  
        return total
    
    def busted(self):
        if self.get_value() > 21:
            return True
        else:
            return False
   
    def draw(self, canvas, pos):
        idx = 0
        for card in self.card_field:
#            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0],  pos[1] + CARD_CENTER[1]], CARD_SIZE)
            card.draw(canvas, [pos[0] + idx * 100, pos[1]])    
            idx += 1

        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_field = []
        for suit in SUITS:
            for rank in RANKS:
                deck_card = Card(suit, rank)
                self.deck_field.append(deck_card)
            
    def shuffle(self):
        random.shuffle(self.deck_field)

    def deal_card(self):
        dealt_cards = []
        card = self.deck_field.pop(0)
        dealt_cards.append(card)
        return card

    def __str__(self):
        deck = ""
        if len(self.deck_field) > 0:
            for i in range(len(self.deck_field)):
                deck += str(self.deck_field[i]) + " "
            return "Deck contains " + str(deck)
        else:
            return "Deck contains"

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, casino_deck, score
    in_play = True

    casino_deck = Deck()
    casino_deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(casino_deck.deal_card())
    
    dealer_hand = Hand()
    dealer_hand.add_card(casino_deck.deal_card())
    
    player_hand.add_card(casino_deck.deal_card())
    
    if player_hand.get_value() == 21:
        dealer_hand.add_card(casino_deck.deal_card())
        if dealer_hand.get_value() == 21:
            outcome = "Player and Dealer both have Blackjack"
            in_play = False
        else:
            outcome = "Player has Blackjack, Player wins!"
            score += 1
            in_play = False
        


def hit():
    global in_play, player_hand, casino_deck, score, outcome
 
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(casino_deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            in_play = False
            outcome = "Player busts: " + str(player_hand.get_value())
            score -= 1
           
       
def stand():
    global player_hand, dealer_hand, score, outcome, in_play

    if in_play:
        dealer_hand.add_card(casino_deck.deal_card())
        if dealer_hand.get_value() == 21:
            outcome = "Dealer has Blackjack, Dealer wins!"
            score -= 1
            in_play = False
            
        else:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(casino_deck.deal_card())
            
            if player_hand.busted():
                outcome = "Player busts, " + str(player_hand.get_value()) + ", Dealer wins."
                score -= 1
            else:
                if dealer_hand.busted():
                    outcome = "Dealer busts, " + str(dealer_hand.get_value()) + ", Player wins!"
                    score += 1
                elif dealer_hand.get_value() < player_hand.get_value():
                    outcome = str(player_hand.get_value()) + ", Player wins!"
                    score += 1
                else:
                    outcome = str(dealer_hand.get_value()) + ", Dealer wins"
                    score -= 1
        in_play = False

# draw handler    
def draw(canvas):
    global win, loss, player_hand, dealer_hand
    player_hand.draw(canvas,[50,400])
    dealer_hand.draw(canvas,[50,250])
    canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,[50+36.5,90+49] , CARD_BACK_SIZE)

    canvas.draw_text("Blackjack", [50, 50], 36, "RED")
    canvas.draw_text("Dealer", [50, 240], 28, "Black")
    canvas.draw_text("Player", [50, 390], 28, "Black")
    canvas.draw_text("Score: " + str(score), [450, 50], 28, "Black")

    if in_play == False:
        canvas.draw_text("New Deal?", [200, 125], 28, "Black")
        canvas.draw_text(outcome, [200, 100], 28, "Black")


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)

frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
