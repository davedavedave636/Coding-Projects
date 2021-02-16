fhand = input('Enter a file name: ')
f = open(fhand, 'r')
emailOccurence = dict()
for line in f:
    if line.startswith('From'):
        x = line.split()
        address = x[1]
        count = 0
        for letter in address:
            index = 0
            if letter == '@':
                index = count + 1
                break
            count += 1
    domain = address[index: ]
    emailOccurence[domain] = emailOccurence.get(domain, 0) + 1
print(emailOccurence)