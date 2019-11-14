import os
import shutil

def spread_message(): 
    return "Hope Is A Good Thing " 

def findFile(s):
    names = []
    for path, dirnames, filenames in os.walk("./Kingdom/Kingdom/Cave/") :
        if len(filenames) > 0 and filenames[0] == s :
            names.append( path[-2:] )
    print( names )
    return names

def findGuard():
    names = findFile( "cross" )
    for path, dirnames, filenames in os.walk("./Kingdom/Kingdom/Castle/"):
        for d in dirnames:
            if ( d[0:2].lower() in names ) and ( d[2:4].lower() in names) :
                targetDir = path + d

    for fileName in os.listdir(targetDir):
        if fileName.isdigit():
            if checkprime(int( fileName )):
                prime = int( fileName )
    return prime


def checkprime( n ):
    for d in range( 2, n ):
        if not (n%d):
            return False
    return True

def aimHigher():
    n = findGuard()
    path = "./Kingdom/Kingdom/Forest/" + ("branch/"*(n%100))
    nameList = []
    for name in os.listdir( path )  :
        # print( name )
        if name[-4:] == ".txt":
            shutil.copy( path+name, "./Kingdom/Kingdom/Sea/"+name )
    for name in os.listdir( "./Kingdom/Kingdom/Sea/" )  :
        if name[-4:] == ".txt":
            nameList.append( name.strip(".txt") )
    nameList.sort()
    print( nameList )
    message = ""
    for name in nameList:
        message += name[5]
    print( message )


# if __name__ == "__main__":
    # aimHigher()
    # findFile("cross")
    
