import os
import sys
import subprocess

def getSum( targetDir, extension ): # ( Directory to be walked ( e.g. ~/ ) , file extensions ( e.g. ".py" )

    # get absolute full path to get 'os.walk' to work 
    fullDir = os.path.expanduser( targetDir )
    if not os.path.isabs( fullDir ):
        fullDir = os.path.abspath( fullDir )  

    fileDict = dict()

    # walk path
    for path, dirnames, filenames in os.walk( fullDir ) :
        for name in filenames :
            a_file_path = path + '/' + name # full path for each files walked
            if ( a_file_path[ -len( extension ) : ] == extension ):
                md5sum = ( subprocess.check_output( [ "md5sum", a_file_path ], universal_newlines=True ) ) [ : 32 ]
                list_to_add = fileDict.get( md5sum, [] )
                list_to_add.append( a_file_path )
                fileDict[ md5sum ] = list_to_add
    return fileDict

if __name__ == "__main__":
    sums = getSum( "~/Documents", ".py" )
    for key in sums:
        if len( sums[key] ) > 1 :
            print( "duplicate files:" )
            for path in sums[key]:
                print( path )
