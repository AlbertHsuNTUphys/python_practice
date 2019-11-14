import math

def is_prime( n ):
    if n == 1:
        return False
    lim = round( math.sqrt( n ) ) + 3
    for d in range( 2, lim ):
        if not n % d :
            return False
    return True

# if __name__ == "__main__":
    # print( is_prime( int( input() ) ) )
