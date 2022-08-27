# importing colors module
# importing random module
from random import randint
from colors import *

# welcome screen
print(YELLOW, '****** Welcome to ChanceGame **********')
user_input = int(input(WHITE + '1. Start Game \n'
                               '2. About chance Game\n'
                               '3. Exit application \n\n'
                               'choose an option above :'
                       ))
# determine user_input
if user_input == 1:
    user_input = int(input(WHITE + 'Choose Game Level\n'
                                   '1.Lazy(1-100)\n'
                                   '2.Intermediate option(1-500)\n'
                                   '3.Genius(1-1000)\n\n'
                                   'provide level please:'))
    guess_range = 0
    if user_input == 1:
        guess_range = 100
    elif user_input == 2:
        guess_range = 500
    elif user_input == 3:
        guess_range = 1000

#       generate random number base on the guess range
    generated_number = randint(1, guess_range)
# attempts available to a user
    user_chance = 3
    for chance in range(3):
        user_guess = int(input(WHITE + 'Provide Your Guess Number :'))
    #               Determine/Validate User Guess
        if user_guess == generated_number:
            print(GREEN, f'Congrats User, You are good')
            break
        elif user_guess > generated_number:
            print(YELLOW, f'{user_guess} Too High, Try Again !!!!')
            user_chance -= 1
        elif user_guess < generated_number:
            print(YELLOW, f'{user_guess} Too low , Try Again !!!!!')
            user_chance -= 1
    if user_chance < 1:
        print(RED, 'Failed\n'
              f'The correct Guess Number is {generated_number}')

elif user_input == 2:
        print(YELLOW, 'A game to check how good you are at guesses, just try your luck. Its fun with numbers')
elif user_input == 3:
        print(WHITE, 'Hope to see you Loser')
        exit(1)
else:
    print(RED, 'Invalid Option,try again !!!!!')
