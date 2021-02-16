import sys
import os
import math
import random
from random import sample
play_again = "yes"
ladders = {
    3: 37,
    6: 16,
    14: 32,
    27: 56,
    41: 85,
    69: 87,
    79: 98,
    89: 91
}
snakes = {
    15: 9,
    42: 17,
    49: 12,
    58: 45,
    61: 22,
    75: 47,
    88: 36,
    94: 64,
    97: 65
}
def rockpaperscissors():
    os.system('cls')
    print('Welcome to Rock Paper Scissors! To play the game, type "rock" , "paper", or "scissors" when prompted to. Then, you will see what the computer chose and whether or not you won!')
    replay = "yes"
    while replay.lower() == "yes":
        bot_choice = random.randint(1,3)
        choice = input("\nDo you pick rock (r), paper (p), or scissors (s)? ")
        if choice == "r":
            if bot_choice == 1:
                print("\nBot chose rock, you tied!")
            elif bot_choice == 2:
                print("\nBot chose paper, you lost!")
            else:
                print("\nBot chose scissors, you won!")
        elif choice == "s":
            if bot_choice == 1:
                print("\nBot chose rock, you lost!")
            elif bot_choice == 2:
                print("\nBot chose paper, you won!")
            else:
                print("\nBot chose scissors, you tied!")
        elif choice == "p":
            if bot_choice == 1:
                print("\nBot chose rock, you won!")
            elif bot_choice == 2:
                print("\nBot chose paper, you tied!")
            else:
                print("\nBot chose scissors, you lost!")
        else:
            print("bad input, make sure everything is lowercase")
        replay = input("Would you like to play this game again? (type 'yes' if you want to play again, or press 'ENTER' to exit.) ")
def guessing():
    os.system('cls')
    print('Welcome to the Guessing Game! Players will guess a number from 1 to 1000. After guessing, the player will be told whether or not their choice was too high or low. Players also have 10 guesses to choose the random number.')
    replay = "yes"
    guesses = 10
    while replay.lower() == "yes":
        number = random.randint(1,1000)
        while guesses > 0:
            guess = int(input("\nGuess a number from 1 to 1000: "))
            if guess == number:
                print("\nYou guessed correctly, you won!")
                break
            elif guess > number:
                guesses -= 1
                print("\nYou guessed too high! You have", guesses, "guesses left.")
            else:
                guesses -= 1
                print("\nYou guessed too low! You have", guesses,"guesses left.")
        if guesses == 0:
            print("\nYou lost! The number was", number)
        replay = input("\nWould you like to play this game again? (type 'yes' if you want to play again, or press 'ENTER' to exit.) ")
def playermove():
    x = random.randint(1,6)
    return x
def snakesandladders():
    os.system('cls')
    print('Welcome to Snakes and Ladders! You will be playing against a computer. To continue, hit the "enter" key, and you will roll a die see what square you land on. If you hit a ladder, you will go to a higher square. If you hit a snake, you will go to a lower square.  The first player to reach square 100 wins!')
    replay = "yes"
    while replay.lower() == "yes":
        scr = 0
        ai = 0
        while scr < 100 and ai < 100:
            rollprompt = input('\nHit "ENTER" to roll the dice. ')
            if rollprompt == "":
                roll = playermove()
                scr += roll
                print('\nYou are at square', scr)
                roll = playermove()
                ai += roll
                print('Computer is at square', ai)
            else: 
                print('bad input, try again')
            if scr in snakes:
                print("\nYou caught a snake from square", scr,"to square", snakes.get(scr))
                scr = snakes.get(scr)
            elif scr in ladders:
                print("\nYou got a ladder from square", scr,"to sqaure", ladders.get(scr))
                scr = ladders.get(scr)
            if ai in snakes:
                print("\nComputer caught a snake from square", ai," to square", snakes.get(ai))
                ai = snakes.get(ai)
            elif ai in ladders:
                print("\nComputer got a ladder from square", ai,"to square", ladders.get(ai))
                ai = ladders.get(ai)
        if scr >= 100:
            print('\nYou win!')
        elif ai >= 100:
            print('\nComputer wins! Better luck next time!')
        replay = input("\nWould you like to play this game again? (type 'yes' if you want to play again, or press 'ENTER' to exit.) ")
while play_again.lower() == "yes":
    os.system('cls')
    print("Welcome to the main menu! We have three games to choose from!")
    game = input("Would you like to play rock-paper-scissors, a guessing game, or snakes and ladders? Enter rock, guess, or snake. ")
    if game == "rock":
        rockpaperscissors()
    elif game == "guess":
        guessing()
    elif game == "snake":
        snakesandladders()
    else:
        os.system('cls')
        continue
    play_again = input("Would you like to play another game? Type yes or no. ")
    
