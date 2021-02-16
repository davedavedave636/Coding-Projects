try:
    fhand = input('Enter a file name: ')
    f = open(fhand, 'r')
except: 
    print('File does not exist due to typo')
    exit()
msgs = dict()
for line in f:
    if line.startswith('From'):
        split = line.split()
        email = split[1]
        msgs[email] = msgs.get(email, 0) + 1
print(msgs)