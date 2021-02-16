x = input('Enter a file input: ')
mbox = open(x)
sum = 0
count = 0
for line in mbox:
    if not 'X-DSPAM-Confidence:' in line:
        continue
    else: 
        spam = line.strip('X-DSPAM-Confidence: ')
        num = float(spam)
        count += 1
        sum += num
print('Average spam confidence:', sum/count)