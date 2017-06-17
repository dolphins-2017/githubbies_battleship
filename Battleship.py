#Battleship Game

import random

class Player: #MIRA
	def __init__(self, ships):
		self.ships = ships

		#Function - store player data
		#name
		#each players gameboard
	pass

	self.ships = [[False, False, 5, "Carrier"], [False, False, 4, "Battleship"], [False, False, 3, "Cruiser"], [False, False,2,"Destroyer"], [False, False,3, "Submarine"]]
		# ships should store their co-ords for position and points have have been hit
		#ships has three arguments, a bool, ship size, and ship name
	where_ships
	miss_shots = []  #where the opp have fired and missed
	shot_shots = [] #where you have shot
	hit_shots = []  #where you have hit
	ship_position = {"Carrier" : [[],[],[],[],[]],"Battleship": [[],[],[],[]], "Cruiser" : [[],[],[]], "Destroyer" : [[],[]], "Submarine" : [[],[],[]]}

class Game: #Mira and Andrew
	def __init__(self, size):
		self.size = size

	def instruction(self):
		#print (<instructions>)
		pass

	def gen_player(self):
	#create instances of players
		pass

	def place_ships(self):
		#For keys in dictionary - ship position,
			#print Player board
			#what is the starting coordinate for your ship
			#what direction (vertical, horizontal) explain directions etc.
			#check to see if it overlaps / is off the board
				#if not - updated ship location
				#if yes - prompt user

	def check_winner(self):
		#has any player won the game
		pass

	def gen_board(self):
		#creates a new gameboard
		pass

	def switch_players():
		#this function recognizes the end of a turn, a changes players
		pass


class Board: #Casey
	def __init__(self, size):
		self.size = size

	def generate_blank_board(self):
		#function is to generate a 10 x 10 gameboard. 
		#Board will be stored as a list of lists

		# listed_list = []
		# new = []
		# for i in range (0, self.size):
		# 	for j in range (0, self.size):
		# 		new.append(random.randrange(1, 51))
		# 	listed_list.append(new)
		# 	new = []
		# 	#this will have returned a list of lists

		# s = [[str(e) for e in row] for row in listed_list]
		# lens = [max(map(len, col)) for col in zip(*s)]
		# fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
		# table = [fmt.format(*row) for row in s]
		# print ('\n'.join(table))
		pass

	def print_player_board(self):
		#function is to, after every turn, print the current status of each players board.
		#call:
			#player1 ships
			#other player missed shots
			#other player hit shots
		#display board
		pass

	def print_opp_board(self):
		#function is to, after every turn, print the current status of each players board.
		#call:
			# player1 missed shots
			# player1 hit shots
		#display board


class Turn: #Jimmy

	#call the opp board function 
	#prompt user for where they would like to shoot
	#user input the co-ords
		#check if a ship is there
		#check to see if ship is sunk
		#if yes,
			#adjust the hit list
			#adjust the ship list
		#if no,
			#adjust the miss list	
	#tell user what the result of the attack was
	
	#if ship is sunk:
		#say which ship is sunk
	



 