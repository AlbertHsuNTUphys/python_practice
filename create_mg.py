def creating_mg(n):
    mg = [[0 for j in range(n)] for i in range(n)]
    cursor = [0, int((n-1)/2)]
    for k in range(n**2):
        mg[cursor[0]][cursor[1]] = k+1
        if (mg[ (cursor[0]-1) % n ][ (cursor[1]+1) % n ] == 0):
            cursor[0] = (cursor[0]-1) % n
            cursor[1] = (cursor[1]+1) % n
        else:
            cursor[0] = (cursor[0]+1) % n
    return mg

if __name__ == "__main__":
    mg = creating_mg(5)
    for l in mg:
        print( l )

# if __name__ == "__main__":
    # size = 3
    # mg = creating_mg(size)
    # s = (size**2)*((size**2)+1)/2/size
    # for l in mg:
        # if not sum(l) == s:
            # raise("fuck")
    # for l in mg:
        # print(l)
    # mg2 = list(map(list, zip(*mg))) 
    # for l in mg2:
        # print(l)
    # for l in mg2:
        # if not sum(l) == s:
            # raise("fuck")

