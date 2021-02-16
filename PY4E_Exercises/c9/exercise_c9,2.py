fhand = open('mbox-short.txt', 'r')
day = dict()
for line in fhand:
    if line.startswith('From'):
        x = line.split()
        if len(x) > 4:
            y = x[2]
            z = x[4]
            day[y] = z
        else: 
            continue     
print(day)