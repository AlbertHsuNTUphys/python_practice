def gcd( a, b ):
    while a % b :
        old_a = a
        old_b = b

        a = old_b
        b = old_a % old_b
    return b

class Fraction :
    def __init__( self , top, bottom ):
        if not (( type(top) is int ) or ( type(bottom) is int )):
            raise TypeError( "Both top and bottom must be integers." )
        if bottom < 0:
            top , bottom = -top, -bottom
        common = gcd( top, bottom )
        self.num = top // common
        self.den = bottom // common

    def show( self ):
        print( self.num, "/", self.den )

    def __str__( self ) :
        return "/".join( (str(self.num), str(self.den))  )

    def __add__( self, otherfraction ):
        if not ( type(otherfraction) is Fraction ):
            otherfraction = Fraction( otherfraction, 1 )
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction( newnum , newden ) 

    def __iadd__( self, otherfraction ):
        self = self + otherfraction
        return self

    def __radd__( self, otherfraction ):
        return self + otherfraction 

    def __eq__( self, otherfraction ):
        return ( self.den * otherfraction.num ) == ( self.num * otherfraction.den )

    def __sub__( self, otherfraction) :
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction( newnum , newden ) 

    def __mul__( self, otherfraction) :
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction( newnum , newden ) 

    def __truediv__( self, otherfraction) :
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        return Fraction( newnum , newden ) 

    def __gt__( self, otherfraction ):
        return ( self - otherfraction ).num > 0 

    def __ge__( self, otherfraction ):
        return ( self - otherfraction ).num >= 0 

    def __lt__( self, otherfraction ):
        return not self >= otherfraction

    def __le__( self, otherfraction ):
        return not self > otherfraction

    def __ne__( self, otherfraction ):
        return not self == otherfraction

    def getnum( self ):
        return self.num
        
    def getden( self ):
        return self.den

    def __repr__( self ):
        return "Fraction(" + str(self.num) + "," + str(self.den) + ")"

if __name__ == "__main__":
    f = Fraction( 1, 3 )
    print( f == eval(repr( f )) )
