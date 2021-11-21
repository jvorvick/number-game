'''
Number Guessing Game

User will try to guess a number between 1 and 100, chosen by the computer.
'''

import random

# loop until player chooses not to play anymore
while True:

    # choose guesser
    guesser = input('Would you like to guess the number? Enter "y" for yourself or "n" for the computer: ').upper()

    # player guesses, computer picks
    if guesser == 'Y':
        # get random number from computer
        computer = random.randint(1, 100)
        correct = False

    # loop until player guesses correctly
        while not correct:
            player = int(input('Choose a number between 1 and 100: '))

            # compare guess to computer and print out appropriate message
            if player < computer:
                message = f'Guess was too low. Try again.'
            elif player > computer:
                message = f'Guess was too high. Try again.'
            else:
                message = f'You guessed the secret!'
                
                correct = True
            
            print(f"computer: {computer}, player: {player}, {message}")
        
        play_again = input('Would you like to play again? Enter "y" or "n": ').upper()

        if play_again != 'Y':
            break

    # computer guesses, player piccks    
    else:
        # get number from player
        player = input('Enter a number between 1 and 100: ')
        

        break