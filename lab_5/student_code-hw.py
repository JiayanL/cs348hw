import common

#helpful, but not needed
class variables:
	counter=0

def sudoku_backtracking(sudoku):
    variables.counter = 0
    #put your code here
    _backtracking(sudoku)
    return variables.counter

def sudoku_forwardchecking(sudoku):
    variables.counter = 0
    # initialize domain to match board
    domain = _init_domain(sudoku)
    _forwardchecking(sudoku, domain)
    return variables.counter

# ---------------------------------------------------------------------------- #
#                               Helper Functions                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------- General --------------------------------- #

# check for empty domains
def _domain_empty(sudoku, domain):
    for y in range(9):
        for x in range(9):
            if len(domain[y][x]) == 0 and sudoku[y][x] == 0:
                return False
    return True

# initialize domain
def _init_domain(sudoku):
    # initialize domain
    domain = [[[] for i in range(9)] for j in range(9)]
    
    for y in range(9):
        for x in range(9):
            # check that entry is empty
            if sudoku[y][x] == 0:
                # look for values
                for value in range(1, 10):
                    # check that its a valid entry
                    if common.can_yx_be_z(sudoku, y, x, value):
                        domain[y][x].append(value)
    return domain

# checks that board is complete
def _check_complete(sudoku):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                return False
    return True

# -------------------------------- Algorithms -------------------------------- #
def _backtracking(sudoku):
    variables.counter += 1
    # print(variables.counter)
    
    # check for completeness
    if _check_complete(sudoku):
        return True
    # backtrack
    # loop through all ys and xs that are empty
    for y in range(9):
        for x in range(9):
            # check that its empty
            if sudoku[y][x] == 0:
                # loop through values 1 - 9
                for value in range(1, 10):
            
                    # check that the value can be put into the position
                    if common.can_yx_be_z(sudoku, y, x, value):
                        sudoku[y][x] = value
                        # recursively check next value
                        if _backtracking(sudoku):
                            return True
                        sudoku[y][x] = 0
                return False
            
def _forwardchecking(sudoku, domain):
    variables.counter += 1
    
    # check for completeness
    if _check_complete(sudoku):
        return True
    
    # forward track
    for y in range(9):
        for x in range(9):
            # check for valid vs
            if sudoku[y][x] == 0:
                for value in range(1, 10):
                    if common.can_yx_be_z(sudoku, y, x, value):
                        # old_domain = _copy_domain(domain)
                        old_domain = list(map(list, domain))
                        sudoku[y][x] = value
                        # update domain by initializing
                        domain = _init_domain(sudoku)
                        
                        # if there are no empty domains
                        if _domain_empty(sudoku, domain):
                            result = _forwardchecking(sudoku, domain)
                            if result:
                                return True
                        sudoku[y][x] = 0
                        # set domain back to normal
                        domain = old_domain
                return False