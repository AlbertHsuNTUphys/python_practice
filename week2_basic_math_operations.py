import math

def basic_math( input_list ) :
    summation , maximum , minimum , _sqsum = 0, input_list[0] , input_list[0] , 0
    for item in input_list :
        summation += item
        _sqsum += item ** 2
        if maximum < item :
            maximum = item
        if minimum > item :
            minimum = item
    average = summation / len(input_list)
    _std = math.sqrt( ( _sqsum / len( input_list ) ) - average ** 2 )
    average = round( average, 2 )
    _std = round( _std, 2 )
    return [ maximum, minimum, summation, average, _std ]

if __name__ == "__main__":
    print( basic_math( [ 1, 2, 3, 4, 5 ] ) )

