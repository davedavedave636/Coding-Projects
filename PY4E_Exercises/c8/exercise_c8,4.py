f = input('enter a file: ') 
x = open(f, 'r')
y = []
for line in x:
    z = line.split()
    y = y + z
y.sort()
print(y)