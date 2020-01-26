def thodeOpen(d, i):
    if d == 0:
        return(12 <= i < 22)
    elif d == 5:
        return(8 <= i < 17)
    elif d == 6:
        return(10 <= i < 17)
    else:
        return(8 <= i < 22)

def getOpenTime(dow):
    if dow == 0:
        return "12:00"       
    elif dow == 6:
        return "10:30"
    else:
        return "8:00"