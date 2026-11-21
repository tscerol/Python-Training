from random import choice

print('Welcome to the rock, paper, scissors game.')
rps = [ 'scissors', 'paper', 'rock' ]
p1 = input('Rock, paper, or scissors?').lower()
p2 = choice(rps)

if p1 == 'scissors':
    if p2 == 'paper':
        print(f'You chose {p1} and player 2 chose {p2}. You win!')
    elif p2 == 'rock':
        print(f'You chose {p1} and player 2 chose {p2}. You lose!')
    else:
        print(f'You chose {p1} and player 2 chose {p2}. It\'s a tie!')
if p1 == 'rock':
    if p2 == 'paper':
        print(f'You chose {p1} and player 2 chose {p2}. You lose!')
    elif p2 == 'scissors':
        print(f'You chose {p1} and player 2 chose {p2}. You win!')
    else:
        print(f'You chose {p1} and player 2 chose {p2}. It\'s a tie!')
       
if p1 == 'paper':
    if p2 == 'scissors':
        print(f'You chose {p1} and player 2 chose {p2}. You lose!')
    elif p2 == 'rock':
        print(f'You chose {p1} and player 2 chose {p2}. You win!')
    else:
        print(f'You chose {p1} and player 2 chose {p2}. It\'s a tie!')
    
