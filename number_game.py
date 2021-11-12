'''
Number Guessing Game

User will try to guess a number between 1 and 100, chosen by the computer.
'''

import random
 
computer = random.randint(1, 100)
# correct = False

while True:
    player = int(input('Choose a number between 1 and 100: '))

    if player < computer:
        message = f'Guess was too low. Try again.'
    elif player > computer:
        message = f'Guess was too high. Try again.'
    else:
        message = f'You guessed the secret!'
        break
        # correct = True
    

    print(f"computer: {computer}, player: {player}, {message}")