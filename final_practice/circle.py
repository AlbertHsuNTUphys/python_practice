class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle( (self.x+other.x)/2,  (self.y+other.y)/2,  (self.r+other.r))
        else:
            return Circle(self.x, self.y, self.r + other)
