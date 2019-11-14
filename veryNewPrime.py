def generating_prime( a, b ):
    # 134 15183
    # 21344 66666
    # 5 1245122 
    # 3 310831
    # 1 1
    # prime_list = []
    # not_prime_list = []
    # if a % 2 :
        # a += 1
    # for num in range( a, b+1, 2 ) :
        # if num in not_prime_list :
            # continue
        # not_prime = True
        # for d in range( 3, int( a**0.5 ) + 1, 2 ) :
            # if d in not_prime_list :
                # continue
            # if not num % d :
                # not_prime = True
                # break
        # if not_prime:
            # continue

    prime_list = [] 
     save = True
    start = 0
    next_num = 3
    all_possibilities = set( range( a, b+1 ) ) 
    if b < 2:
        return []
    
    while next_num <= b :
        is_prime = True
        for d in prime_list :
            if d > next_num*0.5:
                break
            if next_num % d == 0 :
                is_prime = False
                break
        if is_prime :
            prime_list.append( next_num )
        # print( next_num )
        if save and prime_list[-1] >= a :
            start = prime_list.index( next_num )
            save = False
        next_num += 2
    if a <= 2:
        prime_list.insert(0, 2 )

    return prime_list[ (start) : ]

   save = True
    start = 0
    next_num = 3
    all_possibilities = set( range( a, b+1 ) ) 
    if b < 2:
        return []
    
    while next_num <= b :
        is_prime = True
        for d in prime_list :
            if d > next_num*0.5:
                break
            if next_num % d == 0 :
                is_prime = False
                break
        if is_prime :
            prime_list.append( next_num )
        # print( next_num )
        if save and prime_list[-1] >= a :
            start = prime_list.index( next_num )
            save = False
        next_num += 2
    if a <= 2:
        prime_list.insert(0, 2 )

    return prime_list[ (start) : ]

# if __name__ == "__main__":
    # print( generating_prime( 5, 1240 ) )
    # generating_prime( 5, 1245122 ) 



