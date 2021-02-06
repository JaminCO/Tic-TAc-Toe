import random
import time

directions_made = []

try:
	board = ["_", "_", "_",
			 "_", "_", "_",
			 "_", "_", "_"]

	def display_board():
		print(board[0] + " | " + board[1] + " | " + board[2])
		print(board[3] + " | " + board[4] + " | " + board[5])
		print(board[6] + " | " + board[7] + " | " + board[8],'\n')

	def Human_turn():
		check_winner()
		print('Human turn')
		direction = input('Enter a position of choice 1-9 :')
		if direction == 'exit':
			time.sleep(2)
			exit()
		else:
			direction = int(direction)
			if direction != 0:
				direction = direction-1
			else:
				direction = (direction)
			if direction in directions_made:
				print("Space taken\n")
				Human_turn()
			else:
				directions_made.append(direction)
				board[direction] = "X"
				time.sleep(1)

	def Robot_turn():
		t = 0
		check_winner()
		direction = random.randrange(0,8)
		if direction in directions_made:
			t += 1
			if t == 10:
				print('Filled up spaces')
				time.sleep(3)
				exit()
			else:
				Robot_turn()
		else:
			print('Robots turn')
			time.sleep(1)
			directions_made.append(direction)
			board[direction] = "O"
			time.sleep(1)


	def play():
		print('welcometo my tic-tac-toe game')
		time.sleep(1)
		print('we play the game by choosing a position from 1-9 according to the table above \nand the computer allocates it in the position of your choice \nstill in the testing phase. \nEnjoy')
		time.sleep(2)
		while True:
			display_board()
			Human_turn()
			display_board()
			Robot_turn()

	a = board[0] and board[1] and board[2]
	b = board[3] and board[4] and board[5]
	c = board[6] and board[7] and board[8]

	def check_winner():
		if board[0] =='X' and board[1]=='X' and board[2]=='X':
			print('Human is the winner\n')
			print('Robot lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[3]=='X' and board[4]=='X' and board[5]=='X':
			print('Human is the winner\n')
			print('Robot lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[6]=='X' and board[7]=='X' and board[8]=='X':
			print('Human is the winner\n')
			print('Robot lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[0]=="X" and board[3]=="X" and board[6]=='X':
			print('Human is the winner\n')
			print('Robot lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[1]=="X" and board[4]=="X" and board[7]=='X':
			print('Human is the winner\n')
			print('Robot lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[2]=="X" and board[5]=="X" and board[8]=='X':
			print('Human is the winner\n')
			print('Robot lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[0]=="X" and board[4]=="X" and board[8]=='X':
			print('Human is the winner\n')
			print('Robot lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[6]=="X" and board[4]=="X" and board[2]=='X':
			print('Robot is the winner\n')
			print('Human lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()

		elif board[0] =='O' and board[1]=='O' and board[2]=='O':
			print('Robot is the winner\n')
			print('Human lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[3]=='O' and board[4]=='O' and board[5]=='O':
			print('Robot is the winner\n')
			print('Human lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[6]=='O' and board[7]=='O' and board[8]=='O':
			print('Robot is the winner\n')
			print('Human lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[0]=="O" and board[3]=="O" and board[6]=='O':
			print('Human is the winner\n')
			print('Robot lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[1]=="O" and board[4]=="O" and board[7]=='O':
			print('Robot is the winner\n')
			print('Human lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[2]=="O" and board[5]=="O" and board[8]=='O':
			print('Robot is the winner\n')
			print('Human lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[0]=="O" and board[4]=="O" and board[8]=='O':
			print('Robot is the winner\n')
			print('Human lost')
			time.sleep(10)
			print('BYE')
			time.sleep(2)
			exit()
		elif board[2]=="O" and board[4]=="O" and board[6]=='O':
			print('Robot is the winner\n')
			print('Human lost')
			time.sleep(10)
			print('BYE')			
			time.sleep(2)
			exit()
		elif board[6]=="O" and board[4]=="O" and board[2]=='O':
			print('Robot is the winner\n')
			print('Human lost')
			time.sleep(10)
			print('BYE')			
			time.sleep(2)
			exit()
	play()
except Exception as e:
	print(e)
	input("Problem detected EXIT>>")