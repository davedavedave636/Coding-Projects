import sys
import math
import random
def rockpaperscissors():
    replay = "yes"
    while replay == "yes":
        bot_choice = random.randint(1,3)
        choice = input("Do you pick rock, paper, or scissors? ")
        if choice == "rock":
            if bot_choice == 1:
                print("Bot chose rock, you tied!")
            elif bot_choice == 2:
                print("Bot chose paper, you lost!")
            else:
                print("Bot chose scissors, you won!")
        elif choice == "scissors":
            if bot_choice == 1:
                print("Bot chose rock, you lost!")
            elif bot_choice == 2:
                print("Bot chose paper, you won!")
            else:
                print("Bot chose scissors, you tied!")
        elif choice == "paper":
            if bot_choice == 1:
                print("Bot chose rock, you won!")
            elif bot_choice == 2:
                print("Bot chose paper, you tied!")
            else:
                print("Bot chose scissors, you lost!")
        else:
            print("bad")
        replay = input("Would you like to play this game again? ")
def guessing():
    replay = "yes"
    guesses = 10
    while replay == "yes":
        number = random.randint(1,1000)
        while guesses > 0:
            guess = int(input("What number do you guess? "))
            if guess == number:
                print("You guessed correctly, you won!")
                break
            elif guess > number:
                guesses -= 1
                print("You guessed too high! You have " + str(guesses) + " guesses left.")
            else:
                guesses -= 1
                print("You guessed too low! You have " + str(guesses) + " guesses left.")
        if guesses == 0:
            print("You lost! The number was " + str(number))
        replay = input("Would you like to play this game again?")
def playermove():
    x = random.randint(1,6)
    return x
def snakesandladders():
    scr = 0
    ai = 0
    print('Welcome to snakes and ladders!')
    while scr < 100 and ai < 100:
        rollprompt = input('Hit "ENTER" to roll the dice. ')
        if rollprompt == "":
            roll = playermove()
            scr += roll
            print('You are at square', scr)
            roll = playermove()
            ai += roll
            print('Computer is at square', ai)
        else: 
            print('bad input, try again')
        if scr == 3:
            scr = 37
            print('You got a ladder to square 37!')
        elif scr == 6: 
            scr = 16
            print('You got a ladder to square 16!')
        elif scr == 14: 
            scr = 32
            print('You got a ladder to square 32!')
        elif scr == 15:
            scr = 9
            print('You caught a snake back to square 9.')
        elif scr == 27: 
            scr = 56
            print('You got a ladder to square 56!')
        elif scr == 41:
            scr = 85 
            print('You got a ladder to square 85!')
        elif scr == 42:
            scr = 17
            print('You caught a snake back to square 17.')
        elif scr == 49:
            scr = 12
            print('You caught a snake back to square 12.')
        elif scr == 58:
            scr = 45
            print('You caught a snake back to square 45.')
        elif scr == 61:
            scr = 22
            print('You caught a snake back to square 22.')
        elif scr == 69:
            scr = 87
            print('You got a ladder to square 87!')
        elif scr == 75:
            scr = 47
            print('You caught a snake back to square 47.')
        elif scr == 79:
            scr = 98
            print('You got a ladder to square 98!')
        elif scr == 88:
            scr = 36
            print('You caught a snake back to square 36.')
        elif scr == 89:
            scr = 91
            print('You caught a ladder to square 91!')
        elif scr == 94:
            scr = 64
            print('You caught a snake back to square 64.')
        elif scr == 97:
            scr = 65
            print('You caught a snake back to square 65.')
        if ai == 3:
            ai = 37
            print('Computer got a ladder to square 37!')
        elif ai == 6: 
            ai = 16
            print('omputer got a ladder to square 16!')
        elif ai == 14: 
            ai = 32
            print('Computer got a ladder to square 32!')
        elif ai == 15:
            ai = 9
            print('Computer caught a snake back to square 9.')
        elif ai == 27: 
            ai = 56
            print('Computer got a ladder to square 56!')
        elif ai == 41:
            ai = 85 
            print('Computer got a ladder to square 85!')
        elif ai == 42:
            ai = 17
            print('Computer caught a snake back to square 17.')
        elif ai == 49:
            ai = 12
            print('Computer caught a snake back to square 12.')
        elif ai == 58:
            ai = 45
            print('Computer caught a snake back to square 45.')
        elif ai == 61:
            ai = 22
            print('Computer caught a snake back to square 22.')
        elif ai == 69:
            ai = 87
            print('Computer got a ladder to square 87!')
        elif ai == 75:
            ai = 47
            print('Computer caught a snake back to square 47.')
        elif ai == 79:
            ai = 98
            print('Computer got a ladder to square 98!')
        elif ai == 88:
            ai = 36
            print('Computer caught a snake back to square 36.')
        elif ai == 89:
            ai = 91
            print('Computer caught a ladder to square 91!')
        elif ai == 94:
            ai = 64
            print('Computer caught a snake back to square 64.')
        elif ai == 97:
            ai = 65
            print('Computer caught a snake back to square 65.')
    if scr >= 100:
        print('You win!')
    elif ai >= 100:
        print('Computer wins! Better luck next time!')
rockpaperscissors()