#########################################
## DennisX User-Managed MUD Server Kit ##
## player.py                           ##
## Player Handling                     ##
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

import hashlib

class Player:
	def __init__(self, world):
		self.id = -1
		self.username = ""
		self.name = ""
		self.desc = ""
		self.online = False
		self.room = -1
		self.__passhash = ""
		self.__world = world
		self.__ext_calls = {}
	
	def ext(self, name):
		"""Return a reference to the extension call "name". Returns None if 
		failed."""
		if name in self.__ext_calls:
			return self.__ext_calls[name]
		return None
	
	def register_extension_call(self, name, call):
		"""Register a new extension call "name" for this class, where "call" is 
		the extension function."""
		self.__ext_calls[name] = call
	
	def unregister_extension_call(self, name):
		"""Unregister an existing extension call "name" for this class."""
		if name in self.__ext_calls:
			del self.__ext_calls[name]
	
	def move(self, link):
		"""Move the player to the destination room of the Link class 
		instance "link"."""
		self.__world.get_room(self.room).exit(self.id)
		self.__world.get_room(link.dest).enter(self.id)
		self.room = link.dest
	
	def verify_pass(self, password):
		"""Verify "password" as the player's correct password. Returns True if 
		verified successfully, False if not."""
		m = hashlib.sha256()
		m.update(password)
		if m.digest() = self.passhash:
			return True
		return False
	
	def update_pass(self, password):
		"""Update the player's password to "password"."""
		m = hashlib.sha256()
		m.update(password)
		self.passhash = m.digest()

