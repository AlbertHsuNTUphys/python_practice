import math

def dist( p, q ):
    return math.sqrt( ( p.x - q.x )**2 + ( p.y + q.y )**2 )

class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__( self ):
        return "({x},{y})".format( x=self.x , y=self.y ) 


class Circle:

    def __init__( self, c = Point( 0, 0 ), r = 0 ):
        if r < 0 :
            print( "Invalid radius entered. Radius set to 0." )
            r = 0
        self.center = c
        self.radius = r

    def __str__( self ) :
        return "Circle with radius {r} and center at {c}.".format( r = self.radius, c = self.center )

    def inCircle( self, p ) :
        if dist( self.center, p ) > self.radius :
            return False
        else: 
            return True

class Rect:
    def __init__( self, llcorner = Point(0,0), width = 0, height = 0 ) :
        if width < 0 :
            print( "Invalid width entered and is reset to 0." )
            width = 0
        if height < 0 :
            print( "Invalid height entered and is reset to 0." )
            height = 0

        self.llcorner = llcorner
        self.width = width
        self.height = height
    def __str__( self ) :
        return "Rectangle with width {w}, height {h} and lower-left corner at point {p}.".format( w = self.width, h = self.height, p = self.llcorner )

if __name__ == "__main__":
    a = Point( 150, 100 )
    print( a )
    o = Circle( a, 75 )
    print( o )
    r = Rect( a, 10, 15 )
    print( r.llcorner )



