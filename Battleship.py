#Battleship Game

#import random

class Player: #MIRA
	def __init__(self, name):
		self.name = name

		"""Player's ships: dict with ship name as key and 
		[ bool indicating whether ship has been sunk,
		 	size of ship] as value"""
		self.ships = {
		"Carrier": [False, 5],
		"Battleship" : [False, 4],
		"Cruiser": [False, 3], 
		"Destroyer" : [False, 2],
		"Submarine" : [False, 3]}

		"""Position of Player's ships: dict with ship name as key 
		and list with all coords for ships as values"""
		self.ship_position = {
		"Carrier" : [],
		"Battleship": [],
		"Cruiser" : [],
		"Destroyer" : [],
		"Submarine" : []
		}

		# self.opp_hits = [] #where opp has fired and hit
		# self.opp_misses = []  #where the opp have fired and missed
		# self.own_hits = []
		# self.own_misses = []
		self.hits = []
		self.misses = []

		#self.own_shots = [] #where you have shot
		#self.own_hit = []  #where you have hit
		#self.own_misses = []

		#own hits, misses, opp's ships hidden
		# board = Board(player)
		# self.attack_board = Board.gen_attack_board()
		# self.self_board = board.gen_self_board()

		#your ships, opp's hits, opp's misses
		#self.self_board = self_board
	

class Game: #Mira and Andrew
	def __init__(self):
		#self.size = size
		self.players = []
		self.play()

	def play (self): 
		self.setup()
		self.run()

	def run (self):
		current_player_idx = len(self.players) - 1

		while not self.is_game_over():
			current_player_idx = (current_player_idx + 1) % len(self.players)
			#other_player_idx = (current_player_idx + 2) % len(self.players)
			player = self.players[current_player_idx]
			#other_player = self.players[other_player_idx]
			print("{} it is your turn. Your current score is {}".format(player.name))
			
			#print opponent's board (with hits and misses) ADD THIS IN!!

			self.log.append(Turn(player))

		winner = self.log[-1].player
		print("Congratulations {}!!!  You Win!!!".format(winner.name))

	def setup (self):
		#display instructions
		self.instructions()

		#add players
		player_count = self.get_number_of_players()
		for i in range(player_count):
			self.gen_player("Player #{}".format(i + 1))

		#print (self.players)
		#have each player place their ships
		for player in self.players:
			# ships = player.ship_position
			# print (ships)
			#assign coords to players self.ship_position, set boards
			self.place_ships(player)



	def instructions(self):
	        print ("""Game Objective
	            The object of Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates.  Neither you nor the other player can see the other's board so you must try to guess where they are.  Each board in the physical game has two grids:  the lower (horizontal) section for the player's ships and the upper part (vertical during play) for recording the player's guesses.
	            Each player places the 5 ships somewhere on their board.  The ships can only be placed vertically or horizontally. Diagonal placement is not allowed. No part of a ship may hang off the edge of the board.  Ships may not overlap each other.  No ships may be placed on another ship. 
	            A player can choose to place their ships vertically and horizontally, which goes up and right from the start position, respectively.
	            
	            Once the guessing begins, the players may not move the ships.
	            The 5 ships are:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).  
	            Player's take turns guessing by calling out the coordinates. The opponent responds with "hit" or "miss" as appropriate.  Both players should mark their board with pegs:  red for hit, white for miss. For example, if you call out F6 and your opponent does not have any ship located at F6, your opponent would respond with "miss".  You record the miss F6 by placing a white peg on the lower part of your board at F6.  Your opponent records the miss by placing.
	            When all of the squares that one your ships occupies have been hit, the ship will be sunk.   You should announce "hit and sunk".  In the physical game, a red peg is placed on the top edge of the vertical board to indicate a sunk ship. 
	            As soon as all of one player's ships have been sunk, the game ends.""")
      
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
		#board = Board()
		# self_board = Board()
		self.players.append(Player(name))

	def get_orientation(self):
		#ask user for orientation of ship
		is_valid = False
		while not is_valid:
			orientation = input("Would you like to place your ship vertically or horizontally? (Type 'v' or 'h') \n").lower()
			if not orientation.isalpha():
				print("'{}' is not a valid choice for the ship's orientation.\n Please enter either 'v' or 'h'.".format(orientation))
			else:
				is_valid = True

		return orientation.strip()

	def get_coord(self):
		#get a valid coord from user
		is_valid = False
		while not is_valid:
			coord = input("Please enter a starting coordinate for your ship to be placed. \n (The letter of the column followed by the row number \n without any spaces b/w the characters)) \n").upper()
			if len(coord) != 2:
				print("'{}' is not a valid choice for the ship's starting coordinate.\n").format(coord) 
				coord = input("The letter of the column followed by the row number \n without any spaces b/w the characters.\n")
			elif not (coord[0]).isalpha() and (coord[1]).isnumeric():
				print("'{}' is not a valid choice for the ship's starting coordinate.\n").format(coord) 
				coord = input("The letter of the column followed by the row number \n without any spaces b/w the characters.\n")
			else:
				is_valid = True

		stripped_coord = coord.strip()
		list_coord = []
		for char in stripped_coord:
			list_coord.append(char)
		return list_coord

	def valid_coord(self, player, ship_name, coord, orientation):
		#check if ship can be placed at given coordinates

		columns = "ABCDEFGHIJ"

		col = coord[0]
		col_index = columns.index(col)
		row = coord[1]


		ships = player.ships.items()

		#find ship size
		for ship, info in ships:
			if ship_name == ship:
				ship_size = info[1]
				break
				#^ is this how we can stop the loop

		possible_coords = []
		if orientation == "v":
			for i in range(ship_size):
				col_coord = columns[col_index + i]
				row_coord = row + i
				possible_coord = []
				possible_coord.append(col)
				possible_coord.append(str(row_coord))
				possible_coords.append(possible_coord)
		else:
			for i in range(ship_size):
				col_coord = columns[col_index + i]
				possible_coord = []
				possible_coord.append(col_coord)
				possible_coord.append(str(row))
				possible_coords.append(possible_coord)

		if orientation == "v" and (col_index + ship_size) > 9:
			return False
		elif orientation == "h" and (row + ship_size) > 10:
			return False
		else:
			#check if there is another ship there 
			positions = player.ship_position
			for coords in positions.values():
				for position in coords:
					if position in possible_coords:
						return False
		
		return True



	def place_ships(self, player):
		"""
			For keys in dictionary - ship position,
			print Player board
			what is the starting coordinate for your ship
			what direction (vertical, horizontal) explain directions etc.
			check to see if it overlaps / is off the board
				if not - updated ship location
				if yes - prompt user
		"""

		#get coords, orientation, make sure coords are not already used, place ships
		#parent and child classes?
		#find ship size

		ships = player.ship_position
		ship_info = player.ships


		for ship in ships.keys():
			#find ship size
			for ship, info in ship_info.items():
				ship_size = info[1]

				is_valid = False
				while not is_valid:
					#board.generate_blank_board()


					print ("Place your " + str(ship) + "\n which has a size of " + str(ship_size) + " tiles.")
					orientation = self.get_orientation()
					coord = self.get_coord()
					is_valid = self.valid_coord(player, ship, coord, orientation)

					#if the loop gets here, is_valid is still False
					print ("Your ship cannot be placed there. Please try again.")

					#this would make the user place all of their ships again...
					self.place_ships()

			#get all coords of ship 


			coords = []
			if orientation == "v":
				for i in range(ship_size):
					col_coord = columns[col_index + i]
					row_coord = row + i
					possible_coord = []
					possible_coord.append(col)
					possible_coord.append(str(row_coord))
					coords.append(possible_coord)
			else:
				for i in range(ship_size):
					col_coord = columns[col_index + i]
					possible_coord = []
					possible_coord.append(col_coord)
					possible_coord.append(str(row))
					coords.append(possible_coord)

			#add list of all coords as value for corresponding ship key
			ships[ship] = coords

		#generate board with placed ship, store it with player
		self.gen_board(player)

	def gen_board(self, player):
		board = Board(player)
		board.gen_self_board()
		board.print_self_board()
		
	def is_game_over(self, player):
		"""
		#check if all ships have been sunk
		#hits match up with ship positions, 
		compare coords of ship w/ shots, 
		if hits = size of ship, then ship has been sunk

		Or

		if total number of hits == 17/ "X's" = 17, then game is over
		"""
		is_active = True
		hits = player.hits

		#Review - length or sum?
		if len(hits) > 17:
			is_active = False

		return is_active


class Board: #Casey

	def __init__(self, player):
		self.hits = player.hits 
		self.misses = player.misses 
		self.ship_position = player.ship_position

		self.blank_board = [{1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 0:None},
		{1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 0:None},
		{1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 0:None},
		{1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 0:None},
		{1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 0:None},
		{1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 0:None},
		{1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 0:None},
		{1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 0:None},
		{1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 0:None},
		{1:None, 2:None, 3:None, 4:None, 5:None, 6:None, 7:None, 8:None, 9:None, 0:None},]
		
		self.reference_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}

		self.board = self.blank_board
		self.save_board = self.blank_board

		[[a,5],]
	def add_hits(self):

		for item in self.hits: 
			if self.board[self.reference_dict[item[0]]][item[1]] is None: 
				self.board[self.reference_dict[item[0]]][item[1]] = "X"
		return self.board

	def add_ships(self):
		for item in self.ship_position: 
			self.board[self.reference_dict[item[0]]][item[1]] = "[ ]"
		return self.board

	def add_misses(self):
		for item in self.misses: 
			if self.board[self.reference_dict[item[0]]][item[1]] is None: 
				self.board[self.reference_dict[item[0]]][item[1]] = "O"
		return self.board

	def fill_ocean():
		for item in self.board:
			if self.board[item[item]] is None: 
				self.board[item[item]] = "~"
		return self.board

	def gen_attack_board(self):
		self.add_hits() #these are the player hits
		self.add_misses() #these are the player misses
		self.fill_ocean()
		player.attack_board = self.board
		return player.attack_board


	def gen_self_board(self):
		self.add_ships()
		self.fill_ocean()
		player.self_board = self.board
		self.board = self.blank_board
		return player.self_board

	def print_attack_board(self):
		print(self.gen_attack_board)

	def print_self_board(self):
		print(self.gen_self_board)


class Turn: #Jimmy
	def __init__(self, player, other_player):
		self.player = player
		self.other_player = other_player
		#self.other_player = other_player
		self.hit_or_miss()

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

	def attack_Command (self): 
		#Realize which player turn it is so attacks can call on the opposing board
		
		#display opp's board
		own_board = self.other_player.gen_self_board()
		board = self.player.gen_attack_board()
		is_valid = False
		hits = self.player.hits
		misses = self.player.misses
		while not is_valid:
			attack = input("Please input the tile you would like to attack \n (The letter of the column followed by the row number) \n").upper()
			if len(coord) != 2:
				print("'{}' is not a valid choice for a tile.\n").format(coord)
				attack = input("Please enter the letter of the column followed by the row number \n without any spaces b/w the characters. \n")
			elif not (coord[0]).isaplpha() and (coord[1]).isnumeric():
				print("'{}' is not a valid choice for a tile.\n").format(coord)
				attack = input("Please enter the letter of the column followed by the row number \n without any spaces b/w the characters. \n")
			elif (attack in hits) or (attack in misses): 
				print("'{}' has been previously entered.\n").format(coord)
				attack = input("Please enter the letter of the column followed by the row number \n without any spaces b/w the characters. \n")
			else:
				is_valid = True

		stripped_attack = attack.strip()
		list_attack = []
		for char in stripped_attack:
			list_attack.append(char)
		return list_attack


		
	def hit_or_miss (self):

		attack = self.attack_Command()
		hits = self.player.hits
		misses = self.player.misses

		ship_coords = self.player.ship_position.values()

		if attack in ship_coords: 
			hits.append(attack)
			print ("Hit!")
		else:
			misses.append(attack)
			print ("Miss!")

		self.player.gen_attack_board()

		

		#take their hit or miss board, pass to opponent, opponent adds ships at beginning 		


	"""
	def check_ships (self):
			#if ship is sunk:
		#say which ship is sunk
		pass
	"""
	



 