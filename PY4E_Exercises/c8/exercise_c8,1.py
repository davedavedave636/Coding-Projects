def chop(x):    
    del x[len(x)-1]
    del x[0]

def middle(x):
    return x[1:len(x)-1]

x = [612812839123,7,8,8,5,6,5,6,5,6,5,6,5,6,6969696969]

print(chop(x))

