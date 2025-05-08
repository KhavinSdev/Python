#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import time

def deal_cards(new_cards1, new_cards2, size_of_deck = 52, no_of_players = 2 ):
    '''
    Passing in the lists representing the players' hands first as arguments
    followed by size of deck(default = 52) and number of players(default = 2)
    '''
    for i in range(int(size_of_deck/no_of_players)):
        new_cards1.append(selected_deck.deal_card())
        new_cards2.append(selected_deck.deal_card())


# In[2]:


suits = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[3]:


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"



# In[4]:


class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    
    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop(0)


# In[5]:


class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)

        else:  
            self.hand.append(new_cards)

    def remove_card(self):
        return self.hand.pop(0)

    def __str__(self):
        return f'The Player {self.name} has {len(self.hand)} card/cards'


    


# In[6]:


Player1 = Player(input('What is your name? '))
Player2 = (Player('COMPUTER(Irene)'), Player('COMPUTER(Anbil Magesh)'))

Game_On = True

sel = int(input(f'Select your opponent from 1 to {len(Player2)}'))
selected_player = Player2[sel - 1]
print(f"You have selected {selected_player.name} to be your adversary in this WAR!")
    

print('Selecting a new deck....')

time.sleep(5)
selected_deck = Deck()
print('The deck has been chosen')

print('Shuffling the deck.....')

time.sleep(5)
selected_deck.shuffle_deck()
print('The deck has been shuffled!')
           
time.sleep(1)
print()
print('Preparing to start game!')

print()
print()
print()
print("=======================================================")
print()
print('Welcome to W.A.R!!')
print('The game where WRATH leads to ANGER and then RAGE!!!!')
print()
print("=======================================================")
print()
print('Have fun :)')
time.sleep(5)

print('Dealing cards to all players......')

time.sleep(8)
deal_cards(Player1.hand, selected_player.hand)
                                                                    
print('Cards have been distributed!!')


# #debug0.01 - To check whether cards distributed

# for i in Player1.hand:
#     print(i)

# for i in selected_player.hand:
#     print(i)


p1_warpil = []
p2_warpil = []

while Game_On:

    
    if len(selected_player.hand) == 0  or len(Player1.hand) == 0:
        #print(selected_player.hand)
        #print(Player1.hand)
        if len(selected_player.hand) > len(Player1.hand):
            print(f' {selected_player.name} wins the Game!')
        else:
            print(f' {Player1.name} wins the Game! :) e')
        Game_On = False
        break
        
        
    
    p1_card = Player1.remove_card()
    p2_card = selected_player.remove_card()

    print()
    print()

    
    
    print(f'It is {p1_card} VS {p2_card}!')
    
    #time.sleep(4)

    print()
    print()
    
    if p1_card.value < p2_card.value:
        print(f'{selected_player.name} wins!')
        selected_player.add_card(p1_card)
        selected_player.add_card(p2_card)
        selected_player.add_card(p1_warpil)
        selected_player.add_card(p2_warpil)
        p1_warpil = []
        p2_warpil = []
        
    elif p1_card.value > p2_card.value:
        print(f'{Player1.name} wins!')
        Player1.add_card(p1_card)
        Player1.add_card(p2_card)
        Player1.add_card(p1_warpil)
        Player1.add_card(p2_warpil)
        p1_warpil = []
        p2_warpil = []

    if len(selected_player.hand) == 0  or len(Player1.hand) == 0:
        print(selected_player.hand)
        print(Player1.hand)
        if len(selected_player.hand) > len(Player1.hand):
            print(f' {selected_player.name} wins the Game!')
        else:
            print(f' {Player1.name} wins the Game! :) e')
        Game_On = False
        break
    
    elif p1_card.value == p2_card.value:
        print("War has been declared!!!!!")
        time.sleep(2)
        for i in range(3):
            p1_warpil.append(Player1.remove_card())
            p2_warpil.append(selected_player.remove_card())
    
        print('The War Pile is:')
    
        print(Player1.name)
        for i in p1_warpil:
            print(i)
    
        print()
        print()
    
        print(selected_player.name)
        for i in p2_warpil:
            print(i)



print()

print()
print("Thanks for Playing... even though you didn't reall do anything :)")
time.sleep(10)

 

 
    


# In[ ]:




