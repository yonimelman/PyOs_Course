def addition(x,y):
    if type(x)!=int and type(x)!=float:
        raise ValueError
    if type(y)!=int and type(y)!=float:
        raise ValueError
    return x+y
