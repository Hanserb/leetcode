import collections


def isValidSudoku(board):

    # Create sets for rows, columns, and squares
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    # Looping through each position on the board
    for r in range(9):
        for c in range(9):

            # Check if position is empty
            if board[r][c] == ".":
                continue

            # Check if position already exist in one of the dicts
            if (
                (board[r][c] in rows[r])
                or (board[r][c] in cols[c])
                or (board[r][c] in squares[(r // 3, c // 3)])
            ):
                return False

            # Add position to dict
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(isValidSudoku(board))
