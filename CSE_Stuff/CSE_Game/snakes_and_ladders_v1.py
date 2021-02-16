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
if ai >= 100:
    print('Computer wins!')
elif scr >= 100:
    print('You win!')


