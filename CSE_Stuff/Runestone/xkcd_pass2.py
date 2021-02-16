import random
import sys
my_password = 'abcd'
guess_num = 0
done = False
while not done:
    guessed_pw = ""
    for _ in range(4):
        letters = 'qwertyuiopasdfghjklzxcvbnm'
        x = letters[random.randint(0,25)]
        guessed_pw += x 
    print(guessed_pw)
    if guessed_pw == my_password:
        print("found it after ", guess_num, " tries")
        done = True 
        break