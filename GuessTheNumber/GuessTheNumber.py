# This is a guess the number game
import random


### FUNCTIONS ###
def takeAGuess():
    global guess
    for guessesTaken in range(1,7):
        print("Take a guess.");

        guess=int(input())

        if guess<secretNumber:
            print("Your guess is too low.")
        elif guess>secretNumber:
            print("Your guess is too high.")
        else:
            break #break out of the for loop. No more guesses required.
    return guessesTaken

def checkGuess(numGuesses):
    if guess==secretNumber:
        print("Good job! You guesses my secret number in " +str(numGuesses) + " guesses!")
    else:
        print("Nope. The number I was thinking of was " + str(secretNumber) + ".")

### MAIN ###
secretNumber = random.randint(1,20)

print("I am thinking of a number between 1 and 20")

numGuesses=takeAGuess()

checkGuess(numGuesses)
