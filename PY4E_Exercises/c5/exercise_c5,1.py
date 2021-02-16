num = None
count = 0
sum = 0
while num != 'done':
    try:
        if num != 'done': 
            num = (input('Enter a number: '))
            sum = sum + int(num)
            count += 1
        elif num == 'done':
            break
    except: 
        print('bad input')  
try:
    print('sum is', sum, ', count is', count, ', and average is', sum / count)
except: 
    print('please enter a number') 