'''
Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess. If the user guesses wrong
then the prompt appears again until the guess is correct, on successful
guess, user will get a "Well guessed!" message, and the program will
Exit.
Hints: User random.randint() to generate a random number
See the
'''

import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')