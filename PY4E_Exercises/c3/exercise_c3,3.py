try:
    scr = float(input('Enter score: '))
    if 0 <= scr <= 1:
        if scr >= 0.9:
            print('A')
        elif scr >= 0.8:
            print('B')
        elif scr >= 0.7: 
            print('C')
        elif scr >= 0.6: 
            print('D')
        else: 
            print('F')
    else:
        print('Bad score')
except: 
    print('Bad score')