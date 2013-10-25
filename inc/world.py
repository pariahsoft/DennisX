#########################################
## DennisX User-Managed MUD Server Kit ##
## world.py                            ##
## World Handling                      ##
## Copyright 2013 PariahSoft LLC       ##
#########################################

## **********
## Permission is hereby granted, free of charge, to any person obtaining a copy 
## of this software and associated documentation files (the "Software"), to 
## deal in the Software without restriction, including without limitation the 
## rights to use, copy, modify, merge, publish, distribute, sublicense, and/or 
## sell copies of the Software, and to permit persons to whom the Software is 
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in 
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
## IN THE SOFTWARE.
## **********

import console, database, log, plugin

class World:
	"""This class handles the world."""
	def __init__(self, config):
		self.running = True
		self.config = config
		self.plugin_manager = plugin.PluginManager(self)
		self.console = console.Console(self)
		self.database = None
		self.log = log.Log(self)
		self.__players = []
		self.__rooms = []
	
	def tick(self):
		"""Runs tick functions for the console and plugins."""
		for plugin in self.plugin_manager:
			plugin.tick()
		
		self.console.tick()
	
	def log(self, message):
		"""Write "message" to the server log."""
		self.__log.write(message)
	
	def opendb(self, dbfile):
		"""Open a database "dbfile" for saving and loading the world."""
		self.database = database.DatabaseManager(dbfile, self)
	
	def restore(self):
		"""Restore server state from the database."""
		self.database.restore(self)
	
	def save(self):
		"""Save server state to the database."""
		self.database.write(self)
	
	def add_player(self, player):
		"""Add a player to the world, where "player" is the Player class 
		instance."""
		self.__players.append(player)
	
	def get_player(self, playerid):
		"""Return the Player class instance for the player identified by 
		"playerid". Returns None if the player does not exist."""
		for player in self.__players:
			if player.id == playerid:
				return player
		return None
	
	def get_player_by_username(self, username):
		"""Return the Player class instance for the player identified by 
		"username". Returns None if the player does not exist."""
		for player in self.__players:
			if player.username == username:
				return player
		return None
	
	def del_player(self, playerid):
		"""Remove the player identified by "playerid" from the world. Returns 
		True if succeeded, false if the player does not exist."""
		player = None
		
		for n, p in enumerate(self.__players):
			if p.id == playerid:
				pnum = n
				player = p
		
		if player:
			if player.online:
				player.logout()
			del self.__players[pnum]
			return True
		else:
			return False
	
	def add_room(self, room):
		"""Add a room to the world, where "room" is the Room class instance."""
		self.__rooms.append(room)
	
	def get_room(self, roomid):
		"""Return the Room class instance for the room identified by "roomid". 
		Returns None if the room does not exist."""
		for room in self.__rooms:
			if room.id == roomid:
				return room
		return None
	
	def list_players(self):
		"""Return a list of existing player IDs."""
		l = []
		
		for player in self.__players:
			l.append(player.id)
		return l
	
	def list_rooms(self):
		"""Return a list of existing room IDs."""
		l = []
		
		for room in self.__rooms:
			l.append(room.id)
		return l
	
