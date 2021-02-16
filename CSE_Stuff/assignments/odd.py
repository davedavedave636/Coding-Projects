try:
    num = input('enter a number: ')
    if int(num) % 2 == 0: 
        print('even')
    else: 
        print('odd')
except:
    print('error, make sure your input is an integer')