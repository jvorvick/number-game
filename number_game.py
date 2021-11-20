'''
Number Guessing Game

User will try to guess a number between 1 and 100, chosen by the computer.
'''

import random

# loop until player chooses not to play anymore
while True:

    computer = random.randint(1, 100)
    correct = False

# loop until player guesses correctly
    while not correct:
        player = int(input('Choose a number between 1 and 100: '))

        if player < computer:
            message = f'Guess was too low. Try again.'
        elif player > computer:
            message = f'Guess was too high. Try again.'
        else:
            message = f'You guessed the secret!'
            
            correct = True
        
        print(f"computer: {computer}, player: {player}, {message}")

    play_again = input('Would you like to play again? Enter "y" or "n": ')

    if play_again != 'y':
        break