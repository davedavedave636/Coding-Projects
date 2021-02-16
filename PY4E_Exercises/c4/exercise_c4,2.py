try:
    scr = float(input('Enter score: '))
    def computegrade(scr):
        if 0 <= scr <= 1:
            if scr >= 0.9:
                return 'A'
            elif scr >= 0.8:
                return 'B'
            elif scr >= 0.7: 
                return 'C'
            elif scr >= 0.6: 
                return 'D'
            else: 
                return 'F'
        else:
            return 'bad score'
    print(computegrade(scr))
except: 
    print('bad score')