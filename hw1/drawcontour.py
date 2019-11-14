# -*- coding: utf-8 -*-
"""
    hw1.drawcontour
    ~~~~~~~~~~~~~~~

    The goal of this script is to read a figure file (*.bmp and *.jpg are tested and should work 
    properly) and draw the contour of it with the turtle module.  

"""

# Enter the location of the figure file here
FIGURE_PATH = "./flower.bmp"
# Parameter to adjust the strength of the filter. Higer value will make the filter to discard the edges that are not so abvious and speed up the print. The default value is 0, can be either positive, zero or negative.
FILTER_STRENGTH = 1.5
# if you want to print the "edge of the edge" to reduce the printing time, enable fast mode. Note that this sometimes result in wierd contour. Increase the speed by more than 10 times.
FAST_MODE = True
# resize the image to reduce the resolution and increase the speed. 
# New size = old size / RESIZE_RATIO
# Increase the speed by a factor of (approximately) RESIZE_RATIO ^2
RESIZE_RATIO = 10

from PIL import Image # module to read pictures
import numpy as np # use numpy array to process pictures
import math
import sys
# import matplotlib.pyplot as plt # enable this line to test by plotting directly
# I didn't use the cv2 module to find the contour because I want to try doing it by myself
import turtle


# ---------------------------------- Just want to try some exeptions :) --------------------------------------------------

class InvalidResizeRatio( Exception ): # Written for fun :) raised if the ratio to resize is smaller than 1
    def __init__( self ) :
        super().__init__( "The ratio to resize must be larger than one." )

# ---------------------------------- image methods --------------------------------------------------
def readImage( filePath, resize = 1 ):  # read image and transform it into a 3D ( height * width * RGB values ) numpy array. 
    
    image = Image.open( filePath )
    width, height = image.size
    if resize < 1 :
        raise InvalidResizeRatio
    if resize > 1 :
        image = image.resize( ( int( width/resize ), int( height/resize ) ) )
    imArray = np.array( image )
    return imArray

def brightness_of_elements( imageArrayElement ):  # formula to calculate luminance

    # alternative formula to compute luminance :
    # return imageArrayElement[0]*0.2126 + imageArrayElement[1]*0.7152 + imageArrayElement[2]*0.0722 

    return imageArrayElement[0]*0.3 + imageArrayElement[1]*0.59 + imageArrayElement[2]*0.11 

def brightness( imageArray ): # calculating the brightness

    raw_brightness = np.apply_along_axis( brightness_of_elements, 2, imageArray )
    return raw_brightness

def linify( imageArray, filterStrength, fastMode = False ) : # use the Prewitt filter to find the edge

    height, width = imageArray.shape
    processedArray = np.zeros( shape = (height, width) )
    for i in range( 1, height-1 ):
        for j in range(1, width-1 ):
            gx = - imageArray[i+1,j-1] - imageArray[i,j-1] - imageArray[i-1,j-1] + imageArray[i+1,j+1] + imageArray[i,j+1] + imageArray[i-1,j+1]
            gy = - imageArray[i-1,j+1] - imageArray[i-1,j] - imageArray[i-1,j-1] + imageArray[i+1,j+1] + imageArray[i+1,j] + imageArray[i+1,j-1]
            processedArray[i,j] = math.sqrt( gx**2 + gy**2 )
    avg = np.average( processedArray )
    std = np.std( processedArray )
    processedArray = ( processedArray - avg ) / std
    for i in range( 1, height-1 ):
        for j in range(1, width-1 ):
            if processedArray[i,j] > filterStrength:
                processedArray[i,j] = 1
            else:
                processedArray[i,j] = 0
    finalArray = np.copy( processedArray )
    if fastMode :
        for i in range( 1, height-1 ):
            for j in range(1, width-1 ):
                if ( processedArray[i+1,j] and processedArray[i-1,j] and processedArray[i,j+1] and processedArray[i,j-1] ) :
                    finalArray[i,j] = 0
    return finalArray

    
def getLineFig( filePath, filterStrength, fastMode, resize=1 ) : # encapsulation for functions processing the figure array 
    imageArray = readImage( filePath, resize )
    bnwfig = brightness( imageArray ) 
    return linify( bnwfig, filterStrength, fastMode )

# ---------------------------------- turtle methods --------------------------------------------------

def goto( t, x, y ): # move the turtle without drawing anything
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw( figurePath, filterStrength = 1.5, fastMode = False, resize=1, wait = True ) : # encapsulation for drawing methods
    t = turtle.Turtle()
    img = getLineFig( figurePath, filterStrength, fastMode, resize ) # function written in  linefig.py
    height, width = img.shape
    turtle.screensize( width, height )
    turtle.setworldcoordinates( 0, height, width, 0 )
    t.hideturtle() # to improve speed
    t.speed(0)
    print('\n')
    for x in range( 1, width-1 ):
        # for each pixel that is black, draw line line to any pixels
        # that is around it and is also black
        for y in range( 1, height-1 ):
            if img[ y, x ] :
                goto( t, x, y )
                if img[y,x+1]:
                    t.goto(x+1,y)
                    goto( t, x, y )
                if img[y+1,x]:
                    t.goto(x,y+1)
                    goto( t, x, y )
                if img[y+1,x+1]:
                    t.goto(x+1,y+1)
                    goto( t, x, y )
                if img[y+1,x-1]:
                    t.goto(x-1,y+1)
        # remove the last line. MIGHT NOT WORK ON EVERY MACHINE. Tested on Ubuntu 19.04 with Python 3.7.3
            sys.stdout.write("\033[F") #back to previous line
            sys.stdout.write("\033[K") #clear line 
            print( "Progress: {:.1%}".format(( (x-1)*(height-2) + y )/( (width-2) * (height-2) )) ) # printing the progress
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line 
    print( "done" )
    if wait:
        turtle.mainloop()
    
if __name__ == "__main__":
    # to test the functions in this file, uncomment the scripts below and import matplotlib ( line 14 )

    # plt.matshow( getLineFig( FIGURE_PATH ) , cmap = plt.cm.cool, vmin=0, vmax=1)
    # plt.show() 

    draw( FIGURE_PATH, FILTER_STRENGTH , FAST_MODE, RESIZE_RATIO)
