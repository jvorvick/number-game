'''
Number Guessing Game

Either the player or the computer will try to guess a number between 1 and 100, chosen by the opponent.
'''

import random

def choose_guesser():
    return input('Would you like to guess the number? Enter "y" for yourself or "n" for the computer: ').upper()

# player guesses, computer picks
def player_guesses():      
    # get random number from computer
    computer = random.randint(1, 100)
    
    # loop until player guesses correctly
    correct = False
    while not correct:
        player = int(input('Choose a number between 1 and 100: '))

        # compare guess to computer and print out appropriate message
        if player < computer:
            message = 'Guess was too low. Try again.'
        elif player > computer:
            message = 'Guess was too high. Try again.'
        else:
            message = 'You guessed the secret!'
            correct = True
        
        print(f"computer: {computer}, player: {player}, {message}") 

# computer guesses, player picks
def computer_guesses():   
    # get number from player
    player = int(input('Enter a number between 1 and 100: '))
    
    # set lowest and highest value for computer to guess
    lowest = 1
    highest = 100
    
    # loop until computer guesses correctly
    computer = random.randint(lowest, highest)

    correct = False
    while not correct:

        # compare guess to player. if incorrect, adjust range of guess
        if computer < player:
            message = 'Guess was too low. Try again.'
            lowest = computer + 1
        elif computer > player:
            message = 'Guess was too high. Try again.'
            highest = computer - 1
        else:
            message = 'You guessed the secret!'
            correct = True

        print(f'player: {player}, computer: {computer}, {message}')
        print(f'guess range: {lowest, highest}')

        # place computer's next guess in the middle of the new range
        computer = int((highest + lowest) / 2)

def play_again():
    return input('Would you like to play again? Enter "y" or "n": ').upper()

# loop until player chooses not to play anymore
while True:

    # choose guesser
    guesser = choose_guesser()

    if guesser == 'Y':
        player_guesses()
    else:
        computer_guesses()

    again = play_again()

    if again != 'Y':
        print('Goodbye!')
        break