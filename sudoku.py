# import copy
def complete_sudoku(lol): 
    exist_easy_choices = True
    while exist_easy_choices:
        exist_easy_choices = False
        for r in range(9):
            for c in range(9):
                if lol[r][c]:
                    continue
                choice = choices(lol, r, c)
                if len(choice) == 1:
                    lol[r][c] = choice.pop()
                    exist_easy_choices = True

    # if exist0(lol):
    return lol
    # else:
        # return lol

# def guess(lol, n_of_guess):
    # exist_easy_choices = True
    # while exist_easy_choices:
        # for r in range(9):
            # for c in range(9):
                # if lol[r][c]:
                    # continue
                # choice = choices(lol, r, c)
                # if len(choice) == 0:
                    # return None
                # elif len(choice) == 1:
                    # lol[r][c] = choice.pop()
                # else:
                    # lol[r][c] = -len(choice)
    # return lol



# def count0(lol):
    # n = 0
    # for r in range(9):
        # for c in range(9):
            # if lol[r][c] == 0:
                # n += 1
    # print(n)

# def exist0(lol):
    # s = set()
    # for l in lol:
        # s.update(l)
    # no = set([0,-1,-2,-3,-4,-5,-6,-7,-8,-9])
    # if len(s.union(no)):
        # return True
    # else:
        # return False



def choices(lol, r, c):
    options = set([1,2,3,4,5,6,7,8,9])
    ran = set(lol[r])
    for row in lol:
        ran.add(row[c])
    for i in range((r//3)*3,(r//3)*3+3):
        for j in range((c//3)*3,(c//3)*3+3):
            ran.add(lol[i][j])
    return options - ran


# if __name__ == "__main__":
    # input1 = [
            # [5, 3, 0, 0, 7, 0, 0, 0, 0],
            # [6, 0, 0, 1, 9, 5, 0, 0, 0],
            # [0, 9, 8, 0, 0, 0, 0, 6, 0],
            # [8, 0, 0, 0, 6, 0, 0, 0, 3],
            # [4, 0, 0, 8, 0, 3, 0, 0, 1],
            # [7, 0, 0, 0, 2, 0, 0, 0, 6],
            # [0, 6, 0, 0, 0, 0, 2, 8, 0],
            # [0, 0, 0, 4, 1, 9, 0, 0, 5],
            # [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    # difficult = [
            # [0, 0, 0, 0, 3, 0, 9, 0, 0],
            # [0, 0, 0, 0, 0, 9, 4, 1, 0],
            # [0, 0, 0, 1, 0, 8, 6, 0, 0],
            # [0, 3, 0, 9, 4, 0, 0, 8, 2],
            # [4, 0, 0, 0, 0, 0, 0, 0, 6],
            # [6, 9, 0, 0, 5, 1, 0, 4, 0],
            # [0, 0, 5, 3, 0, 7, 0, 0, 0],
            # [0, 6, 7, 8, 0, 0, 0, 0, 0],
            # [0, 0, 4, 0, 1, 0, 0, 0, 0]]
     
    # p = complete_sudoku(input1)
    # for l in p:
        # print(l)
    
    # complete_sudoku(input1)=
            # [
            # [5, 3, 4, 6, 7, 8, 9, 1, 2],
            # [6, 7, 2, 1, 9, 5, 3, 4, 8],
            # [1, 9, 8, 3, 4, 2, 5, 6, 7],
            # [8, 5, 9, 7, 6, 1, 4, 2, 3],
            # [4, 2, 6, 8, 5, 3, 7, 9, 1],
            # [7, 1, 3, 9, 2, 4, 8, 5, 6],
            # [9, 6, 1, 5, 3, 7, 2, 8, 4],
            # [2, 8, 7, 4, 1, 9, 6, 3, 5],
            # [3, 4, 5, 2, 8, 6, 1, 7, 9]] 
    # complete_sudoku(input1)
