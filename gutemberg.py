start = False
import string

def get_wordlist( filename ):
	global start
	fin = open( filename )
	wordlist = dict()
	word = ""
	nope = string.punctuation + string.whitespace + "1234567890"
	for line in fin:
		for char in line:
			if word == "preface":
				start = True
			if not ( char in nope ):
				word += char.lower()
			elif not len(word) == 0:
				if start:
					wordlist[ word ] = wordlist.get( word , 0 ) + 1
				word = ""
	return wordlist

def get_dict( filename ):
	fin = open( filename )
	wordlist = dict()
	for line in fin:
		word = line.strip()
		wordlist[ word ] = None
	return wordlist

if __name__ == "__main__":
	book_dict = get_wordlist( "../../Downloads/book.txt" )

	# print( "length: ", len(book_dict) )

	# FREQ SORT 

	# freq_list = []
	# for word in book_dict:
		# if not book_dict[ word ] in freq_list:
			# freq_list.append( book_dict[ word ] )
	# count = 0
	# for freq in reversed( sorted( freq_list ) ) :
		# for word in book_dict:
			# if book_dict[ word ] == freq:
				# print( word, book_dict[ word ] )
				# count += 1
				# if count > 30 :
					# exit()
	dictionary = get_dict( "../../Downloads/words.txt" )
	# for i in range( 50 ):
		# print( wordlist[i] )
	
	for word in book_dict:
		if not ( word in dictionary ):
			print( word )

