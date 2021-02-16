w = input('Enter a file name: ')
x = open(w, 'r')
y= []
count = 0
for line in x:
    if line.startswith('From'):
        z = line.split()
        print(z[1])
        count += 1
print('There were', count, 'lines in the file as from as the first word')
        
