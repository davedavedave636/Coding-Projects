x = input('Enter a file input: ')
mbox = open(x)
for line in mbox:
    line = line.rstrip()
    print(line.upper())