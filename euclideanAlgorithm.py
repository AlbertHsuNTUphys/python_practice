def gcd( a, b ):
    if not ( a and b ):
        return max( a, b )
    while a % b :
        old_a, old_b = a, b
        a, b = b, (old_a % old_b)
    return b


