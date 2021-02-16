def count():
    word = input('enter a word: ')
    let = input('enter a letter: ')
    countnum = 0
    for letter in word:
        if letter == let:
            countnum += 1
    print('There is/are', countnum, let + "'s")
count()



