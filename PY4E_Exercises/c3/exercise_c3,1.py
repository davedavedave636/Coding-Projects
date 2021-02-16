try:
    hrs = int(input('Enter Hours: '))
    rt = int(input('Enter rate: '))
    paynorm = hrs * rt
    if hrs < 40: 
        print('Pay:', paynorm)
    else: 
        print('Pay:', (hrs - 40) * rt * 0.5 + paynorm)
except: 
    print('Please enter an integer input')