import sys
def sed( pattern, replace, source, target ):

    try:
        fin = open( source )
    except Exception as e:
        print( "Error occurred while attempting to open source file." , file = sys.stderr) 
        exit()


    try:
        fout = open( target, 'w' )
    except Exception as e:
        print( "Error occurred while attempting to open target file.", file = sys.stderr )
        exit()

    for line in fin:
        newline = ""
        findstr = line.find( pattern )
        cursor = 0
        while findstr >= 0 :
            newline += line[ cursor: findstr ]
            newline += replace 
            cursor = findstr + len( pattern )
            findstr = line[ cursor : ].find( pattern )
        newline += line[ cursor : ] 
        fout.write( newline )



if __name__ == "__main__":
    sed( "duck", "fuck", "./test.txt", "./testout.txt" )
