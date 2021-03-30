# This is a guess the number game
import random

name = input ('Hello, what is your name? ')
print ('well, {}, I`m thinking of a number between 1 and 20.'.format(name))
secretnumber  = random.randint(1, 20)

for guesstaken in range(1,7):
    guess = int(input('Take a guess: '))

    if guess < secretnumber:
        print ('Your guess is too low.')
    elif guess > secretnumber:
        print ('Your guess is too high.')
    else:
        break # This condition is for the correct guess
if guess == secretnumber:
    print ('Good job ' + name + '! You guessesd my number in '+ str(guesstaken) + ' guesses.')
else:
    print ('Nope. The number I was thinking of was ' + str(secretnumber))


print ('You took ' + str(guesstaken) + ' guesses.')