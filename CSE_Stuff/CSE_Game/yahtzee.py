import math
import sys
import random
def roll():
    x = random.randint(1,6)
    return x 
rollone = roll()
rolltwo = roll()
rollthree = roll()
rollfour = roll()
rollfive = roll()
print('Welcome to Yahtzee!')
inp = input('Hit "ENTER" to roll. ')
rolltotal = 0
scr = 0
if inp == '':
    print(rollone, rolltwo, rollthree, rollfour, rollfive)
else: 
    print('bad input, try again')
reroll = (input('Which die would you like to reroll? (none, one, two, three, four, or five)')
if reroll == 'none':
elif reroll == 'one':
    rollone = roll()
    print(rollone, rolltwo, rollthree, rollfour, rollfive)

