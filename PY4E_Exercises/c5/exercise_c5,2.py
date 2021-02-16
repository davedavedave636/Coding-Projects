num = None
count = 0
largest = None
smallest = None
while num != 'done':
    try:
        num = input('Enter a number: ')
        if num != 'done':
            if largest is None:
                largest = num
            elif int(num) > int(largest):
                largest = num
            if smallest is None:
                smallest = num
            elif int(num) < int(smallest):
                smallest = num
            count += 1
        elif num == 'done':
            break
    except: 
        print('bad input')
print('largest is', largest, ', smallest is', smallest, ', and count is', count)