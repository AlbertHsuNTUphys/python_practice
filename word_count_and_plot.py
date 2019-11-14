import string
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats

def get_wordlist( filename ):
    global start
    fin = open( filename )
    wordlist = dict()
    word = ""
    nope = string.punctuation + string.whitespace + "1234567890"
    for line in fin:
        for char in line:
            if not ( char in nope ):
                word += char.lower()
            elif not len(word) == 0:
                wordlist[ word ] = wordlist.get( word , 0 ) + 1
                word = ""
    return wordlist

if __name__ == "__main__":
    book_dict = get_wordlist( "../../Downloads/book.txt" )
    # print( book_dict )
    max_freq = 0
    for keys in book_dict:
        max_freq = max( max_freq, book_dict[ keys ] )
    # print( max_freq )
    sorted_list = []
    for freq in reversed( range( 1, max_freq+1 ) ):
        for key in book_dict:
            if book_dict[ key ] == freq :
                sorted_list.append( book_dict[ key ] )
    # print( sorted_list )
    x = range( 1, len( sorted_list )+1 )
    for i in range( len( sorted_list ) ) :
        sorted_list[i] = math.log( sorted_list[i] )

    log_list = []
    for i in x:
        log_list.append( math.log( i ) )
    slope, intercept, r_value, p_value, std_err = stats.linregress( log_list, sorted_list) 
    line = []
    for i in log_list:
        line.append( i * slope + intercept )
    plt.plot( log_list, sorted_list,'o', log_list, line) 
    print( slope, intercept, r_value, p_value, std_err)  
    plt.plot( log_list , sorted_list )
    plt.ylabel("freq")
    plt.xlabel("rank")
    # plt.xscale( "log" )
    plt.show()
    


