record = {}
def debug(func):
    global record
    
    def printArgs(arg):
        result = ''
        size = len(arg)
        for i in range(size):
            result += str(arg[i])
            if i != size-1:
                result += ', '
        return result

    def printKwargs(kwargs):
        result = ''
        size = len(kwargs)
        i = 0
        for key in kwargs:
            result += ( str(key) + '=' + str(kwargs[key]) )
            if i != size-1:
                result += ', '
            i += 1
        return result

    def printAllArgs(arg, kwargs):
        if len(arg) and len(kwargs):
            return printArgs(arg) + ', ' + printKwargs(kwargs)
        elif len(arg)==0 and len(kwargs)!=0:
            return printKwargs(kwargs)
        elif len(arg)!=0 and len(kwargs)==0:
            return printArgs(arg)
        else:
            return ''

    def wrapper(*arg, **kwargs):
        global record
        record[func.__name__] = record.get(func.__name__, 0) + 1
        print('Call ', func.__name__, ' ', record[func.__name__],
                '-th times', sep='')
        print('Calling ', func.__name__, '(', printAllArgs(arg, kwargs),
                ')', sep='')
        returnValue = func(*arg, **kwargs)
        print(func.__name__, ' returned ', returnValue, sep='')
        return returnValue
        

    return wrapper

# @debug
# def hey(a):
    # return a+1

# @debug
# def gcd(m, n):
    # if n == 0:
        # return m
    # else:
        # return gcd(n, m % n)
 

# if __name__ == "__main__":
    # for i in range(2):
        # hey(a=2)
    # gcd(15,12) 
    
