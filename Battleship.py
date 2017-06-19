#Battleship Game

import random

class Player: #MIRA
	def __init__(self, ships):
	self.name = name

	"""Player's ships: dict with ship name as key and 
	[bool indicating whether ship has been placed, 
		bool indicating whether ship has been sunk,
	 	size of ship] as value"""
	self.ships = {
	"Carrier": [False, False, 5],
	"Battleship" : [False, False, 4],
	"Cruiser": [False, False, 3], 
	"Destroyer" : [False, False, 2],
	"Submarine" : [False, False, 3]}

	"""Position of Player's ships: dict with ship name as key 
	and list with all coords for ships as values"""
	self.ship_position = {
	"Carrier" : [],
	"Battleship": [],
	"Cruiser" : [],
	"Destroyer" : [],
	"Submarine" : []
	}

	self.opp_hits = [] #where opp has fired and hit
	self.opp_misses = []  #where the opp have fired and missed
	self.own_shots = [] #where you have shot
	self.own_hit = []  #where you have hit
	self.own_misses = []
	

class Game: #Mira and Andrew
	def __init__(self, size):
		self.size = size
		self.players =[]

	def play (self): 
		self.setup()
		self.run()

	def run (self):
		pass

	def setup (self):
		#display instructions
		self.instructions(self)

		#add players
		player_count = self.get_number_of_players()
		for i in range(player_count):
			self.gen_player("Player #{}".format(i + 1))

		#have each player place their ships
		for player in self.players:
			#assign coords to players self.ship_position

			self.place_ships()

	def instructions(self):
		#print (<instructions>)
		pass

	def get_number_of_players(self):
		is_valid = False
		while not is_valid:
			player_count = input("How many players?\n")
			if not player_count.isnumeric():
				print("'{}' is not a whole number.\n Please enter a whole number.".format(player_count))
			else:
				is_valid = True
		return int(player_count.strip())


	def gen_player(self, title):
		#create instances of players
		name = ""
		while not name:
			name = input("{}, please enter your name: ".format(title))
			name = name.strip()
		self.players.append(Player(name))

	def get_orienation(self):
		#ask user for orientation of ship
		is_valid = False
		while not is_valid:
			orientation = input("Would you like to place your ship vertically or horizontally? (Type 'v' or 'h') \n").lower()
			if not player_count.isalpha():
				print("'{}' is not a valid choice for the ship's orientation.\n Please enter either 'v' or 'h'.".format(orientation))
			else:
				is_valid = True

		return orientation.strip()

	def get_coord(self):
		#get a valid coord from user
		is_valid = False
		while not is_valid:
			coord = input("Please enter a starting coordinate for your ship to be placed. \n (The letter of the column followed by the row number \n without any spaces b/w the characters)) \n").lower()
			if len(coord) != 2:
				print("'{}' is not a valid choice for the ship's starting coordinatine.\n The letter of the column followed by the row number \n without any spaces b/w the characters.".format(coord))
			elif not (coord[0]).isaplpha() and (coord[1]).isnumeric():
				print("'{}' is not a valid choice for the ship's starting coordinatine.\n The letter of the column followed by the row number \n without any spaces b/w the characters.".format(coord))
			else:
				is_valid = True

		return coord.strip()

	def valid_coord(self, ship, coord, orientation):
		#check if ship can be placed at given coordinates

		columns = "abcdefghij"

		col = coord[0]
		col_index = columns.index(col)
		row = coord[1]

		ships = self.player.ships.items():
		#find orientation
		for ship in ships:
			if ship_name == :
				ship_size = 

		if orientation == "v" and (col_index + ship_size) > 9:
			return False
		elif orientation == "h" and (row + ship_size) > 10:
			return False
		else:
			#check if there is another ship there 


	def place_ships(self):
		#get coords, orientation, make sure coords are not already used, place ships
		ships = self.player.ship_position
		for ship in ships.keys():
			is_valid = False
			while not is_valid:
				self.board.print_player_board()
				print ("Place your " + str(ship))
				orientation = self.get_orientation()
				coord = self.get_coord()
				is_valid = self.valid_goord(ship,coord, orientation)
				



		#For keys in dictionary - ship position,
			#print Player board
			#what is the starting coordinate for your ship
			#what direction (vertical, horizontal) explain directions etc.
			#check to see if it overlaps / is off the board
				#if not - updated ship location
				#if yes - prompt user


	def gen_board(self):
		#creates a new gameboard
		pass

	def switch_players():
		#this function recognizes the end of a turn, a changes players
		pass

	def is_game_over(self):
		#check if all ships have been sunk 



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
	



 