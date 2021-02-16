x = open('words.txt', 'r')
wordsdict = dict()
for line in x:  
    w = line.split()
for y in w:
    wordsdict[y] = y
words = input('Enter a word: ')
if words in wordsdict:
    print('There is an instance of the word', words, "in the file.")
