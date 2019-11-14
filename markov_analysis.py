import string
import random

WORDREF = 2
LENGTH = 100

def get_wordlist( filename ):
	global WORDREF
	fin = open( filename )
	nope = "#$%&\()*+-/:;<=>?@[]^_`{|}~"  + string.whitespace + "1234567890"
	wordlist = dict()
	word = ""
	count = 0
	successive_words = []
	for i in range( WORDREF + 1 ) :
		successive_words.append( "" )
	
	for line in fin :
		for char in line :
			if not ( char in nope ) :
				word += char.lower()
			elif not len( word ) == 0 :
				for i in range( WORDREF ) :
					successive_words[i] = successive_words[ i+1 ]
				successive_words[ WORDREF ] = word
				count += 1
				if count > WORDREF - 1 :
					list_to_be_added = wordlist.get( tuple( successive_words[ : WORDREF ] ) , [] )
					list_to_be_added.append( word )
					wordlist[ tuple( successive_words[ : WORDREF] ) ] = list_to_be_added
				word = ""
	return wordlist

def get_random_sentence( wordlist_in_dict , number_of_words = 60):
	if number_of_words < WORDREF:
		print( "The number of words assigned for length is smaller than the number of words referencing. Exiting." )
		return
	number_of_keys = 0
	for keys in wordlist_in_dict:
		number_of_keys += 1
	random_start = random.randint( 1, number_of_keys )
	count = 0
	for keys in wordlist_in_dict:
		start = keys
		count += 1
		if count == random_start:
			break
	sentence_l = []
	for item in start:
		sentence_l.append( item )
		sentence_l.append( " " )
	sentence_l.pop()
	last_word = start
	for i in range( number_of_words - WORDREF ) :
		next_word = random.choice( wordlist_in_dict[ last_word ] )
		sentence_l.append( " " )
		sentence_l.append( next_word )
		last_word = list( last_word[1:] )
		last_word.append( next_word )
		last_word = tuple( last_word )
	sentence_s = "".join( sentence_l )
	print( sentence_s )
	
	
	

if __name__ == "__main__":
	wordlist_in_dict = get_wordlist( "../../Downloads/book.txt" )
	# for wordtuples in wordlist_in_dict:
		# if len( wordlist_in_dict[ wordtuples ] ) > 2 :
			# print( wordtuples, wordlist_in_dict[ wordtuples ] )
	get_random_sentence( wordlist_in_dict, LENGTH )

