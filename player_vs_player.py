board = ['-','-','-',
		 '-','-','-',
		 '-','-','-']


status_game = True
winner  = None
current_player = 'x'


def dis_board():

	print(board[0] + '|' + board[1] + '|' + board[2])
	print(board[3] + '|' + board[4] + '|' + board[5])
	print(board[6] + '|' + board[7] + '|' + board[8])



def main():

	dis_board()

	while status_game:

		input_player()

		check()

		flip_player()

		if winner == 'x':
			print(f'{winner} won')
			break

		elif winner == 'o':
			print(f'{winner} won')
			break



# crete input

def input_player():

	global current_player

	list_number  = [1,2,3,4,5,6,7,8,9]

	valid = True

	while valid:

		player = int(input('choose number 1 - 9: '))
	
		if player in list_number:
			
			player = player - 1

			if board[player] == '-':

				valid = False
			else:
				print('cant enter this number again')

		else:

			player = int(input('choose number 1 - 9: '))


	

	board[player] = current_player

	dis_board()



def flip_player():

	global current_player

	if current_player == 'x':
		current_player = 'o'
	
	elif current_player == 'o':
		current_player = 'x'



# check winner 

def check():

	global winner

	row_winner = row_check()
	cols_winner = cols_check()
	diagonal_winner = diagonal_check()

	if row_winner:
		winner = row_winner

	elif cols_winner:
		winner = cols_winner

	elif diagonal_check:
		winner = diagonal_winner

	else:

		print('tie')


def row_check():

	row_1 = board[0] == board[1] == board[2] != '-'
	row_2 = board[3] == board[4] == board[5] != '-'
	row_3 = board[6] == board[7] == board[8] != '-'

	if row_1 or row_2 or row_3:
		status_game = False

	if row_1:
		return board[0]

	elif row_2:
		return board[3]

	elif row_3:
		return board[6]

	else:
		return None

def cols_check():

	cols_1 = board[0] == board[3] == board[6] != '-'
	cols_2 = board[1] == board[4] == board[7] != '-'
	cols_3 = board[2] == board[5] == board[8] != '-'

	if cols_1 or cols_2 or cols_3:
		status_game = False

	if cols_1:
		return board[0]

	elif cols_2:
		return board[1]

	elif cols_3:
		return board[2]

	else:
		return None


def diagonal_check():

	diag_1 = board[0] == board[4] == board[8] != '-'
	diag_2 = board[2] == board[4] == board[6] != '-'
	
	if diag_1 or diag_2 :
		status_game = False

	if diag_1:
		return board[0]

	elif diag_2:
		return board[2]

	else:
		return None




# execute the game

main()
