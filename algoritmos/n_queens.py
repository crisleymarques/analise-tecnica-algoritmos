
def printSolution(board, n):
  for i in board:
    print("." * i + "Q" + "." * (n - i - 1))
  print()


def is_valid(row, col):
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col + row:
            return False
    return True

def n_queens(board, row, n):
    if row == n:
        printSolution(board, n)

    for col in range(n):
        if is_valid(row, col):
            board[row] = col
            n_queens(board, row + 1, n)
            board[row] = 0
            

n = int(input())
board = [0] * n 
n_queens(board, 0, n)