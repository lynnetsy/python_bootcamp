from os import name
import random


dict = [
    {
        'name': 'cristiano ronaldo',
        'followers': 3560
    },
    {
        'name': 'kylie jenner',
        'followers': 2764
    },
    {
        'name': 'lionel messi',
        'followers':2750
    },
    {
        'name': 'dwayne johnson',
        'followers':2745
    },
    {
        'name': 'ariana grande',
        'followers':2719
    }
]

def question():
    yes = ('si', 'yes', 'y', 's')
    response = input('Deseas jugar Otra vez?\n').lower()
    if response in yes:
        return True
    else:
        return False

def get_index():
    random_index = random.randint(0, len(dict) - 1)
    return random_index

def generate_people():
    random_people = get_index()
    people = dict[random_people]
    return people

def choice(p1,p2):
    choice=input(f"Quien crees que tenga mas followers: \n{p1['name']} o {p2['name']}\n\n").lower()
    return choice

def compare_followers(p1, p2, choice):
    winner = None
    if p1['followers'] > p2['followers']:
        winner = p1
    elif p1['followers'] < p2['followers']:
        winner = p2
    
    return winner is not None and winner['name'] == choice
    
 
def game():
    print('HIGHER OR LOWER!\n\n')
    p1=generate_people()
    p2=generate_people()
    user_bid=choice(p1, p2)
    win=compare_followers(p1,p2,user_bid)
    if win:
        print('Acertaste!')
    else:
        print('Mas suerte para la proxima')
    other_game = question()
    if other_game == True:
        game()
    else:
        return

game()
