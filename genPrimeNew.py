import sys
# def is_prime( n ):
    # return True

def generating_prime(a,b): 
    prime_list = []
    not_prime_dict = []
    for n in range( a, b+1 ) :
        if not n % 2 :
            continue
        if n == 1 :
            continue
        if not n in not_prime_dict :
            p = False
            for i in range( 2, int(n**0.5)+1 ) :
                if not n % i :
                    p = True
                    break
            if p :
                continue
            prime_list.append( n )
            not_prime_dict.extend( range( 2*n, b, n) )
        else:
            not_prime_dict.remove( n )
    return prime_list


# if __name__ == "__main__":
    # print( generating_prime( 1, 101 ) )
