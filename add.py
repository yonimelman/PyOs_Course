def addition(x,y):
    '''
    addition(x,y) takes two numbers, adds them and returns their sum.
    input: 
        x - number (type int/float)
        y - number (type int/float)
    output:
        the sum of x+y; number (type int/float)
    '''

    if type(x)!=int and type(x)!=float:
        raise TypeError('Wrong input type: Use int or float only')
    if type(y)!=int and type(y)!=float:
        raise TypeError('Wrong input type: Use int or float only')
    
    return x+y



