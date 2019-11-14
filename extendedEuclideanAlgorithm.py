# import random
# import euclideanAlgorithm 

def extended_gcd(a, b):
    if a == 0 and b == 0 :
        return 0, 0
    if a == 0 or b == 0 :
        return 1, 0

    b, a = sorted( ( a, b ) )
    # switched = False
    # if a < b :
        # switched = True
        # a, b = b, a
    r = [a,b]
    q = []
    q_next, r_next = divmod(a, b)
    while r_next != 0 :
        r.append( r_next )
        q.append( q_next )
        q_next, r_next = divmod(r[-2], r[-1])
    s = [ 1, 0 ]
    t = [ 0, 1 ]
    for i in range(2, len(r)):
        s.append( s[-2] - q[i-2]*s[-1] )
        t.append( t[-2] - q[i-2]*t[-1] )
    return s[-1], t[-1]
    
# if __name__ == "__main__":

    # for i in range(100, 10000) :
        # x = random.randint( 0, 100000000000)
        # y = random.randint( 0, 100000000000)
        # a, b = extended_gcd( x, y )
        # if a*x + b*y != euclideanAlgorithm.gcd( x, y ) :
            # print( i, x, y )
    # print( extended_gcd( 0, 0 ) )
    # print( extended_gcd( 5, 5 ) )


