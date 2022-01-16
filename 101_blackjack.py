import random
import sys


cards = [
    { 'name' : 'As', 'value': 1},
    { 'name' : '2', 'value': 2 },
    { 'name' : '3', 'value': 3 },
    { 'name' : '4', 'value': 4 },
    { 'name' : '5', 'value': 5 },
    { 'name' : '6', 'value': 6 },
    { 'name' : '7', 'value': 7 },
    { 'name' : '8', 'value': 8 },
    { 'name' : '9', 'value': 9 },
    { 'name' : 'King', 'value':10 },
    { 'name' : 'queen', 'value':10 },
    { 'name' : 'A', 'value': 10 },
]

def get_card():
    random_card = random.randint(0, len(cards) - 1)
    return random_card



def start_play():
    selected_cards = []
    for card in range(0, 2):
        random_cards = get_card()
        cards_player1 = cards[random_cards]
        selected_cards.append(cards_player1)
    return selected_cards

def sum_cards(cards):
    total = 0
    for card in cards:
        total += card["value"]
    return total




def blackjack():
    goal = 21

    player1 = start_play()
    player2 = start_play()


    if sum_cards(player1) < 13:
        total = sum_cards(player1)
        print(f"PLAYER 1 TAKE CARD: You have {total}")
    if sum_cards(player2) < 13:
        total2 = sum_cards(player2)
        print(f"PLAYER 2 TAKE A CARD: You have {total2}")



blackjack()

