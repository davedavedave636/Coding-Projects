import random
import sys
import math
scr = 0
ai = 0
def playermove():
    x = random.randint(1,6)
    return x
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