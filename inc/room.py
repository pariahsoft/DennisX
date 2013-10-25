#########################################
## DennisX User-Managed MUD Server Kit ##
## room.py                             ##
## Room Handling                       ##
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

class Room:
	"""This class represents a room."""
	def __init__(self):
		self.id = -1
		self.name = ""
		self.desc = ""
		self.owner = None
		self.locked = False
		self.__items = []
		self.__links = []
		self.__players = []
	
	def add_item(self, item):
		"""Add an item to the room, where "item" is the Item class instance."""
		self.__items.append(item)
	
	def get_item(self, itemid):
		"""Return the Item class instance for the item identified by 
		"itemid". Returns None if the item does not exist."""
		for item in self.__items:
			if item.id = itemid:
				return item
		return None
	
	def del_item(self, itemid):
		"""Remove the item identified by "itemid" from the room. Returns True 
		if succeeded, false if the item does not exist."""
		item = None
		
		for n, i in enumerate(self.__items):
			if i.id = itemid:
				inum = n
				item = p
		
		if item:
			del self.__items[inum]
			return True
		else:
			return False
	
	def add_link(self, link):
		"""Add a link to the room, where "link" is the Ltem class instance."""
		self.__links.append(link)
	
	def get_link(self, linkid):
		"""Return the Link class instance for the link identified by 
		"linkid". Returns None if the link does not exist."""
		for link in self.__links:
			if link.id = linkid:
				return link
		return None
	
	def del_link(self, linkid):
		"""Remove the link identified by "linkid" from the room. Returns True 
		if succeeded, false if the link does not exist."""
		link = None
		
		for n, l in enumerate(self.__links):
			if l.id = linkid:
				lnum = n
				link = l
		
		if link:
			del self.__links[lnum]
			return True
		else:
			return False
	
	def enter(self, player):
		"""Enter a player into the room, where "player" is the Player class 
		instance."""
		self.__players.append(player)
	
	def exit(self, playerid):
		"""Exit the player identified by "playerid" from the room. Returns True 
		if succeeded, false if the player does not exist."""
		player = None
		
		for n, p in enumerate(self.__players):
			if p.id = playerid:
				pnum = n
				player = p
		
		if player:
			def self.__players[pnum]
			return True
		else:
			return False

