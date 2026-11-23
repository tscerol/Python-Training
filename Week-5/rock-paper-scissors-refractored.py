from random import choice

def is_winner(player1,player2):
    
    if player1 == 'scissors':
        if player2 == 'paper':
            print(f'You chose {player1} and player 2 chose {player2}. You win!')
        elif player2 == 'rock':
            print(f'You chose {player1} and player 2 chose {player2}. You lose!')
        else:
            print(f'You chose {player1} and player 2 chose {player2}. It\'s a tie!')
    if player1 == 'rock':
        if player2 == 'paper':
            print(f'You chose {player1} and player 2 chose {player2}. You lose!')
        elif player2 == 'scissors':
            print(f'You chose {player1} and player 2 chose {player2}. You win!')
        else:
            print(f'You chose {player1} and player 2 chose {player2}. It\'s a tie!')
       
    if player1 == 'paper':
        if player2 == 'scissors':
            print(f'You chose {player1} and player 2 chose {player2}. You lose!')
        elif player2 == 'rock':
            print(f'You chose {player1} and player 2 chose {player2}. You win!')
        else:
            print(f'You chose {player1} and player 2 chose {player2}. It\'s a tie!')
    




print('Welcome to the rock, paper, scissors game.')
rps = [ 'scissors', 'paper', 'rock' ]
p1 = input('Rock, paper, or scissors?').lower()
p2 = choice(rps)
is_winner(p1,p2)
