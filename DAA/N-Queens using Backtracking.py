# N-Queens Problem using Backtracking
def is_attack(i, j, board, N):
    # Check the column
    for k in range(i):
        if board[k][j] == 1:
            return True

    # Check upper right diagonal
    k, l = i - 1, j + 1
    while k >= 0 and l < N:
        if board[k][l] == 1:
            return True
        k -= 1
        l += 1

    # Check upper left diagonal
    k, l = i - 1, j - 1
    while k >= 0 and l >= 0:
        if board[k][l] == 1:
            return True
        k -= 1
        l -= 1

    return False


def n_queen(row, n, N, board):
    # Base case: all queens placed
    if n == 0:
        return True

    # Try placing a queen in each column of the current row
    for j in range(N):
        if not is_attack(row, j, board, N):
            board[row][j] = 1  # Place queen
            # Recur to place rest of the queens
            if n_queen(row + 1, n - 1, N, board):
                return True
            # Backtrack
            board[row][j] = 0

    return False


# Driver code
N = int(input("Enter the size of the chessboard (N): "))
board = [[0 for _ in range(N)] for _ in range(N)]

# Place the first queen manually
board[0][0] = 1

# Call function to place remaining N-1 queens
if n_queen(1, N - 1, N, board):
    print("\nFinal N-Queens Solution:")
    for row in board:
        print(row)
else:
    print("Solution does not exist.")
