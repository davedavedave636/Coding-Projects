x = input('Enter a file input: ')
count = 0
if x == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()
try:
    mbox = open(x)
    for line in mbox:
        count += 1
except: 
    print('File cannot be opened:', x)
    quit()
print('There were', count, 'subject lines in', x)