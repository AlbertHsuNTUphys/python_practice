import copy
def fill(lol):

    exist_easy_choices = True
    while exist_easy_choices:
        exist_easy_choices = False
        for r in range(9):
            for c in range(9):
                if lol[r][c] > 0:
                    continue
                choice = choices(lol, r, c)
                if len(choice) == 0:
                    # print('Dead')
                    return None
                elif len(choice) == 1:
                    exist_easy_choices = True
                    lol[r][c] = choice.pop()
                else:
                    lol[r][c] = len(choice) - 10
    return lol

def make_set(lol):
    s = set()
    for l in lol:
        s.update(l)
    return s

def complete_sudoku(lol):
    # print('#####', count0(lol))
    # print('##### Depth:', depth)
    # print(lol)
    lol = fill(lol)
    if lol == None:
        # print('passing None')
        return None
    # print('successfully filled!')
    # if depth == 8:
        # pretty_print(lol)
    if incompleted(lol):
        _range = make_set(lol)
        target = min(_range)
        found = False
        for r in range(9):
            if found:
                break
            for c in range(9):
                if found:
                    break
                if lol[r][c] == target:
                    found = True
                    index = (r,c)
        choice = choices(lol, index[0], index[1])
        # print('choices: ', choice)
        for c in choice:
            # print('trying ', c)
            test = copy.deepcopy(lol)
            test[index[0]][index[1]] = c
            test = complete_sudoku(test)
            if not incompleted(test):
                # print('passing completed!')
                return test
    else:
        return lol


def pretty_print(lol):
    for l in lol:
        print(l)

# def count0(lol):
    # n = 0
    # for r in range(9):
        # for c in range(9):
            # if lol[r][c] <= 0:
                # n += 1
    # return n

def incompleted(lol):
    if lol == None:
        return True
    s = set()
    for l in lol:
        s.update(l)
    no = set([0,-1,-2,-3,-4,-5,-6,-7,-8,-9])
    if len(s.intersection(no)):
        # print(s.intersection(no))
        return True
    else:
        return False



def choices(lol, r, c):
    options = set([1,2,3,4,5,6,7,8,9])
    ran = set(lol[r])
    for row in lol:
        ran.add(row[c])
    for i in range((r//3)*3,(r//3)*3+3):
        for j in range((c//3)*3,(c//3)*3+3):
            ran.add(lol[i][j])
    return options - ran


if __name__ == "__main__":
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
     
    very_difficult = [
            [0, 0, 0, 0, 7, 0, 4, 0, 0],
            [6, 7, 3, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, 9, 0, 5, 0, 0],
            [3, 0, 2, 0, 0, 0, 0, 0, 8],
            [0, 0, 7, 0, 1, 0, 0, 0, 9],
            [0, 0, 0, 5, 0, 2, 0, 0, 0],
            [0, 0, 0, 2, 5, 8, 0, 3, 0],
            [0, 0, 0, 0, 0, 7, 0, 4, 0],
            [8, 6, 0, 0, 0, 0, 0, 0, 0]]
    
    pretty_print( complete_sudoku(very_difficult) )
