x = None
y = []
try:
    while x != 'done':
        x = input('Enter a number: ')
        if x == 'done':
            print('Maximum:', max(y), 'Minimum:', min(y))
            break
        y.append(int(x))
except: 
    print('bad input')


