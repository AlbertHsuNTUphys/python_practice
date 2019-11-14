# -*- coding: utf-8 -*-
"""
    hw1.linefig
    ~~~~~~~~~~~

    This file defines functions to transform figure files into an 2D array describing the contour 
    of the picture. The method used here is actually very crude (calculating linumance and interpret
    pixels that have luminance below average to be black and otherwise white ) but can be improved.

"""

from PIL import Image # module to read pictures
import numpy as np # use numpy array to process pictures
import math
import matplotlib.pyplot as plt # enable this line to test by plotting directly
# I didn't use the cv2 module because I want to try doing it by myself

def readImage( filePath ):
    """
    read image and transform it into a 3D ( height * width * RGB values ) numpy array. 
    """
    
    image = Image.open( filePath )
    imArray = np.array( image )
    return imArray

def brightness_of_elements( imageArrayElement ):
    """
    formula to calculate luminance
    """
    # return imageArrayElement[0]*0.2126 + imageArrayElement[1]*0.7152 + imageArrayElement[2]*0.0722 
    return imageArrayElement[0]*0.3 + imageArrayElement[1]*0.59 + imageArrayElement[2]*0.11 

def brightness( imageArray ):
    """
    calculating the normalized brightness
    """
    raw_brightness = np.apply_along_axis( brightness_of_elements, 2, imageArray )
    std = np.std( raw_brightness )
    # avg = np.average( raw_brightness )
    # raw_brightness -= avg
    # raw_brightness /= std * 6
    return raw_brightness

def linify( imageArray ) :
    """
    if the pixels around a pixel are all black, make it white to find the contour of the picture.
    """
    height, width = imageArray.shape
    processedArray = np.zeros( shape = imageArray.shape )
    for i in range( 1, height-1 ):
        for j in range(1, width-1 ):
            # if ( imageArray[i+1,j] and imageArray[i,j+1] and imageArray[i-1,j] and imageArray[i,j-1] ) :
                # processedArray[i,j] = 0
            gx = - imageArray[i+1,j-1] - imageArray[i,j-1] - imageArray[i-1,j-1] + imageArray[i+1,j+1] + imageArray[i,j+1] + imageArray[i-1,j+1]
            gy = - imageArray[i-1,j+1] - imageArray[i-1,j] - imageArray[i-1,j-1] + imageArray[i+1,j+1] + imageArray[i+1,j] + imageArray[i+1,j-1]
            processedArray[i,j] = math.sqrt( gx**2 + gy**2 )
        # print( i , height, sep='/')
    avg = np.average( processedArray )
    std = np.std( processedArray )
    processedArray = (processedArray-avg) / std
    strength = 1.5
    # newArray = ( processedArray > 0 ).astype(int)
    for i in range( 1, height-1 ):
        for j in range(1, width-1 ):
            if processedArray[i,j] > ( strength):
                processedArray[i,j] = 1
            else:
                processedArray[i,j] = 0
    return processedArray
    # return newArray

    
def getLineFig( filePath ) :
    """
    packing all the functions above
    """
    imageArray = readImage( filePath )
    # bnwfig = ( brightness( imageArray ) > 0 ).astype( int ) 
    bnwfig = brightness( imageArray ) 
    return linify( bnwfig )
    # return bnwfig



"""
to test the functions in this file, uncomment the scripts below and import matplotlib ( line 14 )
"""
if __name__ == "__main__":
    # print( bnwfig )
    # print( bnwfig.shape )
    # plt.matshow( bnwfig.astype( int ) ) 
    # plt.matshow( bnwfig ) 
    # plt.show()
    
    plt.matshow( getLineFig( "./test3.jpg") , cmap = plt.cm.cool, vmin=0, vmax=1)
    plt.show() 
    # plt.matshow(bnwfig, cmap = plt.cm.cool, vmin=0, vmax=1)
    # plt.show() 


