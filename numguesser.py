import os
import time
import random
numoftries = 0
def game():
    numoftries = 0
    
    print("I am thinking of a number between 1, 100")
    computenum = random.randint(1,100)
    print("Take a Guess!")

    while numoftries < 100:
        guess = input()
        guess = int(guess)
    

        numoftries = numoftries + 1

        if guess > computenum:
            print("Too High!")
        if guess < computenum:
            print("Too Low!")
        if guess == computenum:
            break
    if guess == computenum:
        numoftires = str(numoftries)
        print("Congrats you guessed the number, and it took you " + str(numoftries) + " Tries!")
        again = input("Would you like to play again? Y,N:")
        if input == "y":
            game()
        if input == "n":
            exit()
game()
