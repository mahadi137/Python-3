# This is a guess the number game
# udemy course: Automate the boring stuff with python programming

import random
print('Hey! What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 to 20.')
secretNumber = random.randint(1, 20)

for guessedNumber in range (1, 5):
    print('Take a guess: ')
    guess = float(input()) 
    if guess < secretNumber:
        print('I guessed a higher number than yours.')
    elif guess > secretNumber:
        print('I guessed a lower number than yours.')
    else:
        break # This condition is for the correct number.

if guess == secretNumber:
    print('Good job! ' + name + ' ,You guessed the correct number.')
    print('You took ' + str(guessedNumber) + ' guesses.')
else:
    print('Nope. The number I guessed is, ' + str(secretNumber) + '.')
    
