
def printSolution(board, n):
  for i in range(n):
    for j in range(n):
      if board[i][j] == 1:
        print("Q", end="")
      else:
        print(".", end="")
    print()
  print()


def isSafe(board, row, col):
	# Check this row on left side
	for i in range(col):
		if board[row][i] == 1:
			return False

	# Check upper diagonal on left side
	for i, j in zip(range(row, -1, -1),
					range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	# Check lower diagonal on left side
	for i, j in zip(range(row, n, 1),
					range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	return True


def n_queens(board, col, n):
	if col >= n:
		printSolution(board, n)

	for i in range(n):
		if isSafe(board, i, col):
			board[i][col] = 1

			n_queens(board, col + 1, n)

			# remove the queen if solution is not possible
			board[i][col] = 0


n = int(input())
board = [[0] * n for _ in range(n)]
n_queens(board, 0, n)