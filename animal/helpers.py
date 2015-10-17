####################
# HELPER FUNCTIONS #
####################

def generateBoard(min, max):
	board = []
	for i in range(min, max):
		board.append([-1, -1, -1])
	return board


def printBoard(board):
	for row in board:
		print row
	return

def placePiece(board, name, x, y):
	board[x][y] = name
	return

