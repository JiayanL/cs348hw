import common

def minmax_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	return common.constants.NONE

def abprun_tictactoe(board, turn):
    '''
	it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	use the function common.game_status(board), to evaluate a board
	it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	the program will keep track of the number of boards evaluated
	result = common.game_status(board);
    '''
    alpha = float("-inf")
    beta = float("inf")
    result = _abprun(board, turn, alpha, beta)

    if result > 0:
        return common.constants.X
    elif result < 0:
        return common.constants.O
    else:
        return common.constants.NONE
    # return common.constants.NONE

# ---------------------------------------------------------------------------- #
#                                    Helpers                                   #
# ---------------------------------------------------------------------------- #

# alpha beta pruning function
def _abprun(board, turn, alpha, beta):
    # check status of the game
    # if the game is done, return utility
    game_status = common.game_status(board)
    if _fullboard(board) or game_status:
        # zero sum
        if game_status == 2:
            game_status = -1
        return game_status

    #check turn for max or min
    # ------------------------------------ max ----------------------------------- #
    if turn == common.constants.X:
        v = float("-inf")
        # for all empty board positions, p
        for move in _nextmoves(board):
            y = move[0]
            x = move[1]
            # place x at position p on the board
            common.set_cell(board, y, x, turn)
            # value = prune(board, O, alpha, beta)
            value = _abprun(board, common.constants.O, alpha, beta)
            # v = max(v, value)
            v = max(v, value)
            # remove x from p
            common.set_cell(board, y, x, common.constants.NONE)
            # if v >= B, return v
            if v >= beta:
                return v
            alpha = max(alpha, v)
            # alpha = max(alpha, v)
        return v

    # ------------------------------------ min ----------------------------------- #
    elif turn == common.constants.O:
        v = float("inf")
        # for all empty board positions, p
        for move in _nextmoves(board):
            y = move[0]
            x = move[1]
            # place X at position p on the board
            common.set_cell(board, y, x, turn)
            # value = prune(board, X, alpha, beta)
            value = _abprun(board, common.constants.X, alpha, beta)
            # v = min(v, value)
            v = min(v, value)
            # remove X from p
            common.set_cell(board, y, x, common.constants.NONE)
            # if v <= A, return v
            if v <= alpha:
                return v
            # beta = min(beta, v)
            beta = min(beta, v)
        return v

# check if the board is full
def _fullboard(board):
    for y in range(3):
        for x in range(3):
            if common.get_cell(board, y, x) == common.constants.NONE:
                return False
    return True

# find empty positions
def _nextmoves(board):
    next_positions = []
    for y in range(3):
        for x in range(3):
            if common.get_cell(board, y, x) == common.constants.NONE:
                next_positions.append([y, x])
    return next_positions
