hrs = int(input('Enter Hours: '))
rt = int(input('Enter rate: '))
def computepay(hrs, rt):
    try:
        paynorm = hrs * rt
        if hrs < 40: 
            return paynorm
        else: 
            return (hrs - 40) * rt * 0.5 + paynorm
    except: 
        print('Please enter an integer input')
print('Pay:', computepay(hrs, rt))