QUEENS = 10

# ---------------------------------------------------------------------------- #
#                                     Main                                     #
# ---------------------------------------------------------------------------- #

# stores attack count and state to compare different states
class StateContainer:
    def __init__(self, attacks, state=None):
        self.attacks = attacks
        self.state = state

def gradient_search(board):
    # queens is a proxy for board status
    old_board = find_queens(board)
    reduced = True
    
    # greedy search
    while reduced:
        reduced = False
        best_board = copy_queens(old_board)

        # measures current attack score as index for other moves
        curr_attack_score = attacks(best_board)
        # array stores best moves for each queen - contains score and state
        best_moves = [StateContainer(curr_attack_score, best_board) for i in range(QUEENS)]

        # loop through all 10 queens
        for column, old_row in enumerate(old_board):
            # for each queen, choose the best move
            # loop through all possible rows
            for new_row in range(QUEENS):
                new_board = copy_queens(old_board)
                # assign new row to queen
                new_board[column] = new_row
                new_attacks = attacks(new_board)
                # if attacks(new_board) < attacks(best_board)
                if new_attacks < best_moves[column].attacks:
                    best_moves[column] = StateContainer(new_attacks, new_board)
        # select best_board
        best_moves.sort(key=lambda x: x.attacks)
        next_move = best_moves[0]

        if next_move.attacks < curr_attack_score:
            reduced = True
            best_board = next_move.state

        old_board = best_board

    # redraw board, using best_board as a reference
    for y in range(QUEENS):
        for x in range(QUEENS):
            if best_board[x] == y:
                board[y][x] = 1
            else:
                board[y][x] = 0

    if attacks(best_board) == 0:
        return True
    return False

# ---------------------------------------------------------------------------- #
#                               Helper Functions                               #
# ---------------------------------------------------------------------------- #

# Helper function to copy position of queens
def copy_queens(array):
    queens_copy = [0 for i in range(QUEENS)]
    for x in range(QUEENS):
        queens_copy[x] = array[x]
    return queens_copy

# Helper function to find where the queens are
def find_queens(board):
    queens = [0 for i in range(QUEENS)]
    for y in range(QUEENS):
        for x in range(QUEENS):
            if board[y][x] == 1:
                queens[x] = y
    return queens

# Helper function to find attacks 
def attacks(board):
    attacks = 0 
    # for all pairs of queens
    for qa_column, qa_row in enumerate(board):
        for qb_column, qb_row in enumerate(board):
            if qa_column != qb_column:
                y_diff = qb_column - qa_column
                x_diff = qb_row - qa_row

                # if row(A) = row(B), increment attack
                if qa_row == qb_row:
                    attacks += 1
                # if diag(A) = Diag(B), increment attack
                elif y_diff == x_diff:
                    "diag up"
                    attacks +=1
                elif y_diff == -x_diff:
                    "diag down"
                    attacks +=1

    return attacks
