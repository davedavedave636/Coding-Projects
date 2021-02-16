string = 'X-DSPAM-Confidence: 0.8475 '
spos = string.find(' ')
secondpos = string.find (' ', spos + 1)
decimal = string[spos + 1:secondpos]
print(float(decimal))
