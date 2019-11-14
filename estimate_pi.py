import random

def calculate_pi( n ) :
    random.seed( 777 )

    count = 0

    for i in range( n ):
        x = random.random()
        y = random.random()
        if ( x**2 + y**2 < 1 ) :
            count += 1

    estimated_pi = round( (count / n * 4) , 3 )

    return estimated_pi 
