# CSE Variety Game App
# By David Huang and Jason Zhang
# Note: repl sometimes has problems aligning the text so some of the text might get cut off. If it happens, we recommend running the code on the Visual Studio Code app instead.

import sys           # import these for a randomizer and other things 
import os
import math
import random
from random import sample

def clearscreen():    # create a function to make the screen jump 20 lines so it's easier to read 
   for _ in range(20):
       print("\n")

play_again = "yes"
ladders = {          # these two dictionaries are for the snakes and ladders game, and the third is for the trivia game.
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
Problems = {
    "What year did humans first step foot on the moon? (your answer is an integer)": "1969",
    "What is the capital of the state of Washington?": "Olympia",
    "How many elements are there on the periodic table? (your answer is an integer)": "118",
    "What year did WW2 end? (your answer is an integer)": "1945",
    "How many sides does a nonagon have? (your answer is an integer)": "9",
    "How many years was the longest time someone was a US president? (your answer is an integer)": "12",
    "How many centimeters are in a kilometer? (your answer is an integer)": "100000",
    "What year did the US gain independence? (your answer is an integer)": "1776",
    "About how many million miles is between the Earth and the Sun? (your answer is an integer)": "93",
    "How many degrees are in a right angle? (your answer is an integer)": "90",
    "Who was the 13th president? Only put last name.": "Fillmore",
    "How many votes are the US electoral college? (your answer is an integer)": "538",
    "What country was Beethoven born in?": "Germany",
    "What is the smallest country?": "Vatican City",
    "About how many bones are humans born with? (your answer is an integer)": "300"
}
key = list(Problems)

def trivia():              # define a function for the trivia game, the trivia game picks five random questions from a pool of 15 total questions
    clearscreen()
    print('Welcome to the Trivia Game! You will be given five random questions, and try to answer them to the best of your knowledge! Correct answers are worth one point and incorrect answers are worth none. (also be sure to spell everything correctly and put an integer answer when asked to do so.) \n')
    replay = "yes"                # while loop for replayability  
    score = 0             
    while replay.lower() == "yes": 
      s = sample(key, 5)
      for i in s:
          print(i)
          answer = input("What is your answer? ")
          if answer.lower() == Problems.get(i).lower():
              print("\nThat is correct!\n")
              score += 1
          else:
              print("\nSorry, that was incorrect.\n")
      print("You got {}/5 questions correct!".format(score))
      replay = input("Would you like to play this game again? (type 'yes' if you want to play again, or press 'ENTER' to exit.) ")
      clearscreen()

def rockpaperscissors():    # define a function for the rock paper scissors game
    clearscreen()        # the computer picks a random selection and the player will be asked to input their selection
    print('Welcome to Rock Paper Scissors! To play the game, type "rock" , "paper", or "scissors" when prompted to. Then, you will see what the computer chose and whether or not you won!')
    replay = "yes"
    while replay.lower() == "yes":     # while loop for replayability
        bot_choice = random.randint(1,3)    #computer picks a random number which is rock, paper, or scissors
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
        clearscreen()

def guessing():         # guessing game picks a random integer from 1 to 1000 and players have 10 tries to guess the number
    clearscreen()
    print('Welcome to the Guessing Game! Players will guess a number from 1 to 1000. After guessing, the player will be told whether or not their choice was too high or low. Players also have 10 guesses to choose the random number.')
    replay = "yes"
    while replay.lower() == "yes":              # while loop for replayability
        number = random.randint(1,1000)
        guesses = 10
        while guesses > 0:
            try:    
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
            except:
                print('Bad input, make sure you write an integer.')
        if guesses == 0:
            print("\nYou lost! The number was", number)
        replay = input("\nWould you like to play this game again? (type 'yes' if you want to play again, or press 'ENTER' to exit.) ")
        clearscreen()

def playermove():           # the playermove function is a function that rolls the dice for the snakes and ladders game
    x = random.randint(1,6)
    return x
def snakesandladders():     # the dictionaries from earlier are used as snakes and ladders. when a player rolls onto a square with a snake or ladder, they will move squares.
    clearscreen()
    print('Welcome to Snakes and Ladders! You will be playing against a computer. To continue, hit the "enter" key, and you will roll a die see what square you land on. If you hit a ladder, you will go to a higher square. If you hit a snake, you will go to a lower square.  The first player to reach square 100 wins!')
    replay = "yes"
    while replay.lower() == "yes":            # while loop for replayability
        scr = 0
        ai = 0
        while scr < 100 and ai < 100:     # make a while loop for the player until they reach square 100 or more
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
            if scr in snakes:           # dictionaries are used for the snakes and ladders here
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
        clearscreen()

while play_again.lower() == "yes":          #this is the main menu screen where you can choose to play a game
    clearscreen()
    print("Welcome to the main menu! We have four games to choose from!")
    game = input("Would you like to play rock-paper-scissors, a guessing game, snakes and ladders, or a trivia game? Enter rock, guess, snake, or trivia. ")
    if game == "rock":        # make an if statement to determine which game the player wants to play
        rockpaperscissors()
    elif game == "guess":
        guessing()
    elif game == "snake":
        snakesandladders()
    elif game == "trivia":
        trivia()
    else:
        clearscreen()
        continue
    play_again = input("Would you like to play another game? Type yes or no. ")



