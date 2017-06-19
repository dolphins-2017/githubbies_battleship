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

		self.hits = [] #where opp has fired and hit
		self.misses = []  #where the opp have fired and missed

		#self.own_shots = [] #where you have shot
		#self.own_hit = []  #where you have hit
		#self.own_misses = []


	

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
			player = self.players[current_player_idx]
			print("{} it is your turn. Your current score is {}".format(player.name, player.score))
			
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


		#have each player place their ships
		for player in self.players:
			#assign coords to players self.ship_position, set boards
			self.place_ships()

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
		self.players.append(Player(name))

	def get_orientation(self):
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
			coord = input("Please enter a starting coordinate for your ship to be placed. \n (The letter of the column followed by the row number \n without any spaces b/w the characters)) \n").upper()
			if len(coord) != 2:
				print("'{}' is not a valid choice for the ship's starting coordinate.\n").format(coord) 
				coord = input("The letter of the column followed by the row number \n without any spaces b/w the characters.\n")
			elif not (coord[0]).isaplpha() and (coord[1]).isnumeric():
				print("'{}' is not a valid choice for the ship's starting coordinate.\n").format(coord) 
				coord = input("The letter of the column followed by the row number \n without any spaces b/w the characters.\n")
			else:
				is_valid = True

		return coord.strip()

	def valid_coord(self, ship_name, coord, orientation):
		#check if ship can be placed at given coordinates

		columns = "abcdefghij"

		col = coord[0]
		col_index = columns.index(col)
		row = coord[1]


		ships = self.player.ships.items()

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
				possible_coord = col + str(row_coord)
				possible_coords.append(possible_coord)
		else:
			for i in range(ship_size):
				col_coord = columns[col_index + i]
				possible_coord = col_coord + str(row)
				possible_coords.append(possible_coord)

		if orientation == "v" and (col_index + ship_size) > 9:
			return False
		elif orientation == "h" and (row + ship_size) > 10:
			return False
		else:
			#check if there is another ship there 
			positions = self.player.ship_position
			for coords in positions.values():
				for position in coords:
					if position in possible_coords:
						return False
		
		return True



	def place_ships(self):
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
		ships = player.ship_position
		for ship in ships.keys():
			is_valid = False
			while not is_valid:
				self.board.print_player_board()

				print ("Place your " + str(ship))
				orientation = self.get_orientation()
				coord = self.get_coord()
				is_valid = self.valid_coord(ship,coord, orientation)

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
					possible_coord = col + str(row_coord)
					coords.append(possible_coord)
			else:
				for i in range(ship_size):
					col_coord = columns[col_index + i]
					possible_coord = col_coord + str(row)
					coords.append(possible_coord)

			#add list of all coords as value for corresponding ship key
			ships[ship] = coords

		#generate board with placed ship, store it with player
		self.player.own_board = self.gen_board(ships)

	def gen_board(self, player):

		self.board.generate_blank_board()

	def is_game_over(self):
		"""
		#check if all ships have been sunk
		#hits match up with ship positions, 
		compare coords of ship w/ shots, 
		if hits = size of ship, then ship has been sunk

		Or

		if total number of hits == 17/ "X's" = 17, then game is over
		"""
		is_active = True
		hits = self.player.hits

		#Review - length or sum?
		if len(hits) > 17:
			is_active = False

		return is_active


class Board: #Casey
	def __init__(self, size):
		self.size = size

	def generate_blank_board(self):

		blank_board = {'A': {'1': '~', '2': '~','3': '~','4' : '~' , '5': '~', '7': '~', '6': '~', '8' : '~', '9' : '~'},
	    'B': {'1': '~', '2': '~','3': '~','4' : '~', '5': '~', '7': '~', '6': '~', '8' : '~', '9' : '~'},
	    'C': {'1': '~', '2': '~','3': '~','4' : '~', '5': '~', '7': '~', '6': '~', '8' : '~', '9' : '~'},
	    'D': {'1': '~', '2': '~','3': '~','4' : '~', '5': '~', '7': '~', '6': '~', '8' : '~', '9' : '~'},
	    'E': {'1': '~', '2': '~','3': '~','4' : '~', '5': '~', '7': '~', '6': '~', '8' : '~', '9' : '~'},
	    'F': {'1': '~', '2': '~','3': '~','4' : '~', '5': '~', '7': '~', '6': '~', '8' : '~', '9' : '~'},
	    'G': {'1': '~', '2': '~','3': '~','4' : '~', '5': '~', '7': '~', '6': '~', '8' : '~', '9' : '~'},
		'H': {'1': '~', '2': '~','3': '~','4' : '~', '5': '~', '7': '~', '6': '~', '8' : '~', '9' : '~'},
		'I': {'1': '~', '2': '~','3': '~','4' : '~', '5': '~', '7': '~', '6': '~', '8' : '~', '9' : '~'}}

		board = blank_board

		print (board)
		strs = "{0:^2} {1:^2} {2:^2} {3:^2} {4:^2} {5:^2} {6:^2} {6:^2} {7:^2} {8:^2} {9:^2} "    

		print (strs.format(" ", *sorted(board)))

		for x in sorted(blank_board):
			print (strs.format(x, *(blank_board[x].get(y, "~" ) for y in sorted(blank_board))))

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
		pass

class Turn: #Jimmy
	def __init__(self, player):
		self.player = player
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

		return attack


		"""
		while attack and is False: 		
			if attack == board.tile:
				found = True
			else: 
				current = current.next
		if attack is None:
			raise Exception("Not a valid tile")
		"""

		#return 
			#if value isn't a valid tile, or if value has already been called in previous round
			
			
			#User will input coordinates, each coordinate corresponds with a dictionary value?
		
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
		"""


		

		if attack is in #boat location in dict on opposing board: 
			#append list? Not sure I get how the list of hits and misses is supposed to work
			#in relation to the dictionary of values
			print ("Hit!")

			else if attack is not in #boat location in dict on opposing board:
				#append list? See above comment
				print ("Miss!")			
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
	

"""

	def check_ships (self):
			#if ship is sunk:
		#say which ship is sunk
		pass
	



 