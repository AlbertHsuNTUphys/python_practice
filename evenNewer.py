def generating_prime( a, b ):
    if b < 2 :
        return []
    all_possibilities = list(reversed(range( 2, b+1 )))
    # print( all_possibilities )
    cursor = len( all_possibilities ) - 1
    # print( all_possibilities[cursor] )
    
    while cursor >= 0 :
        next_d = all_possibilities[cursor]
        # print( "nextd" , next_d )
        small_cursor = cursor - next_d
        # print( "smc", all_possibilities[small_cursor] )
        # print( small_cursor )
        while small_cursor >= 0 :
            # print( all_possibilities[small_cursor] )
            all_possibilities[small_cursor] = 0
            small_cursor -= next_d
        cursor -= 1
        while all_possibilities[cursor] == 0:
            cursor -= 1
    ans = []
    for i in reversed(all_possibilities):
        if i < a :
            continue
        if i != 0 :
            ans.append(i)
    return ans


# if __name__ == "__main__":
    # print( generating_prime( 5, 31 ) )
    # generating_prime( 3, 310831 )
    # 5 1245122 
    # 3 310831
     

 


