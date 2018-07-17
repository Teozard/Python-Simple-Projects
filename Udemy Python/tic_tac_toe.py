def display_board(board):
    print(f'\
{board[7]} {board[8]} {board[9]}\n\
{board[4]} {board[5]} {board[6]}\n\
{board[1]} {board[2]} {board[3]}\n')


def player_input():
	player1 = ''
	while player1 != 'X' or player1 != 'X':
		player1 = input("Please pick a marker 'X' or 'O'")
	print(player1)


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)
player_input()