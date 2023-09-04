#!/usr/bin/python3
""" a program that solves the N queens problem"""
import sys
"""the allowed module """

def init_board(n):
	"""ïnitializing the board"""
	board = []
	[board.append([]) for i in range(n)]
	[row.append(' ') for i in range(n) for row in board]
	return (board)


def bod_cpy(board):
	"""Return a deepcopy of a chessboard."""
	if isinstance(board, list):
		return list(map(bod_cpy, board))
	return (board)


def get_sol(board):
	"""Return the list of lists representation in a board."""
	sol = []
	for r in range(len(board)):
		for c in range(len(board)):
			if board[r][c] == "Q":
				sol.append([r, c])
				break
	return (sol)


def xout(board, row, col):
	"""X spots on a chessboard."""

	for c in range(col + 1, len(board)):
		board[row][c] = "x"

	for c in range(col - 1, -1, -1):
		board[row][c] = "x"

	for r in range(row + 1, len(board)):
		board[r][col] = "x"

	for r in range(row - 1, -1, -1):
		board[r][col] = "x"

	c = col + 1
	for r in range(row + 1, len(board)):
		if c >= len(board):
			break
		board[r][c] = "x"
		c += 1

	c = col - 1
	for r in range(row - 1, -1, -1):
		if c < 0:
			break
		board[r][c]
		c -= 1

	c = col + 1
	for r in range(row - 1, -1, -1):
		if c >= len(board):
			break
		board[r][c] = "x"
		c += 1

	c = col - 1
	for r in range(row + 1, len(board)):
		if c < 0:
			break
		board[r][c] = "x"
		c -= 1


def solve(board, row, queens, sols):
	"""
		recursively solve an N-queens puzzle
	"""
	if queens == len(board):
		sols.append(get_sol(board))
		return (sols)

	for c in range(len(board)):
		if board[row][c] == " ":
			tmp_board = bod_cpy(board)
			tmp_board[row][c] = "Q"
			xout(tmp_board, row, c)
			sols = solve(tmp_board, row + 1,
							queens + 1, sols)

	return (sols)


if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: nqueens N")
		sys.exit(1)
	if sys.argv[1].isdigit() is False:
		print("N must be a number")
		sys.exit(1)
	if int(sys.argv[1]) < 4:
		print("N must be at least 4")
		sys.exit(1)

	board = init_board(int(sys.argv[1]))
	sols = solve(board, 0, 0, [])
	for sol in sols:
		print(sol)
