import random

class Card :
    suit_names = [ "Clubs", "Diamonds", "Hearts", "Spades" ]
    rank_names = [ None, "Ace", '2', '3', '4', '5', '6', '7', '8', '9', "10", "Jack", "Queen", "King" ]
    def __init__( self, s = 0, r = 2):
        self.suit = s
        self.rank = r

    def __str__( self ) :
        return "{rank} of {suit}".format( rank = Card.rank_names[ self.rank ], suit = Card.suit_names[ self.suit ] )

    def __lt__( self, other ):
        return (self.suit , self.rank) < (other.suit , other.rank)
    
    def __eq__( self, other ):
        return (self.suit , self.rank) == (other.suit , other.rank)

    def __gt__( self, other ):
        me = self.suit, self.rank
        you = other.suit, other.rank
        return me > you and ( not me == you )

    def __le__( self, other ):
        return not self > other 

    def __ge__( self, other ):
        return (self > other) or (self == other)

class Deck :
    def __init__( self ):
        self.cards = []
        for suit in range( 4 ) :
            for rank in range( 1, 14 ) :
                self.cards.append( Card( suit, rank ) )
    
    def __str__( self ):
        tmp_arr = []
        for card in self.cards :
            tmp_arr.append( str( card ) )
        return '\n'.join( tmp_arr )
    
    def shuffle( self ):
        random.shuffle( self.cards )

    def sort( self ) :
        self.cards.sort()

    def pop( self ) :
        return self.cards.pop()

    def add( self , card ) :
        self.cards.append( card )

class Hand( Deck ) :
    def __init__( self, label = '') :
        self.cards = []
        self.label = label

    def move_cards( self, hand, num ) :
        for i in range( num) :
            hand.add( self.pop_card() )



class PokerHand( Hand ) :
    def suit_hist( self ) :
        self.suits = {}
        print( type( self.suits ) )
        for card in self.cards :
            self.suits[ card.suit ] = self.suits.get( card.suit, 0 ) + 1

    def has_flush( self ) :
        for val in self.suits.values :
            if val >= 5 :
                return True
        return False

    def has_staight_flush( self ) :
        return any( all( ( Card( c.suit, c.rank + i ) in self.cards ) for i in range(5) ) for c in self.cards )


if __name__ == "__main__":
    myhand = PokerHand()
    myhand.add( Card( 2, 5 ) )
    myhand.add( Card( 2, 6 ) )
    myhand.add( Card( 2, 7 ) )
    myhand.add( Card( 2, 8 ) )
    myhand.add( Card( 2, 9 ) )
    print( myhand.has_staight_flush() )

