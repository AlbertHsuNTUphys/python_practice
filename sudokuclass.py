import copy

# The class name and function define here cannot be changed.
class Sudoku:
    def __init__(self,board):
        self.board = board
    def complete_sudoku(self):
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
        self.board = fill(self.board)

    def get_board(self):
        return self.board
 
if __name__ == "__main__":
    input1 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    input2 = [
        [4, 0, 3, 0, 2, 0, 0, 7, 1],
        [2, 6, 0, 0, 5, 0, 0, 4, 9],
        [9, 0, 8, 4, 0, 0, 0, 5, 6],
        [0, 4, 2, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 9, 1, 5],
        [1, 0, 9, 5, 0, 0, 0, 0, 7],
        [3, 8, 0, 2, 0, 9, 7, 0, 0],
        [0, 2, 1, 0, 3, 0, 5, 0, 8],
        [7, 9, 0, 0, 0, 0, 0, 0, 0]]
    output1= [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    output2 = [
        [4, 5, 3, 9, 2, 6, 8, 7, 1],
        [2, 6, 7, 8, 5, 1, 3, 4, 9],
        [9, 1, 8, 4, 7, 3, 2, 5, 6],
        [5, 4, 2, 1, 9, 7, 6, 8, 3],
        [8, 7, 6, 3, 4, 2, 9, 1, 5],
        [1, 3, 9, 5, 6, 8, 4, 2, 7],
        [3, 8, 5, 2, 1, 9, 7, 6, 4],
        [6, 2, 1, 7, 3, 4, 5, 9, 8],
        [7, 9, 4, 6, 8, 5, 1, 3, 2]]
    ex_sodoku1 = Sudoku(input1)
    ex_sodoku2 = Sudoku(input2)
    ex_sodoku1.complete_sudoku()
    ex_sodoku2.complete_sudoku()
    # If ex_sodoku1.get_board() and output1 mismatch, an AssertionError will be
    # raise,
    # this is a common way to test your code.
    assert ex_sodoku1.get_board() == output1, "Wrong Answer"
    assert ex_sodoku2.get_board() == output2, "Wrong Answer" 
