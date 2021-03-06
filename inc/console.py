#########################################
## DennisX User-Managed MUD Server Kit ##
## console.py                          ##
## Player Console and Command Manager  ##
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

class Console:
	"""This class handles the server listeners, processes command strings from 
	them, and passes these to the appropriate command plugins."""
	def __init__(self, world):
		self.__linebuf = []
		self.__commands = {}
		self.__listeners = {}
		self.__world = world
	
	def tick(self):
		"""Get lines from the listeners each tick."""
		for listener in self.__listeners.values():
			self.process(listener.get_lines())
	
	def process(self, lines):
		"""Process lines received and pass to the appropriate commands, where 
		"lines" is a list of lines received."""
		for line in lines:
			player = line[0]
			name, args = line[1][0], line[1][1:]
			
			if name in self.__commands:
				self.__commands[name].command(player, args)
			else:
				msg = self.__world.config["messages"]["invalid_command"]
				self.send(player, msg.format(name))
	
	def send(self, player, message):
		"""Send a message to a player through their listener, where "player" 
		is the player id and "message" is the message to be sent."""
		listener = self.__world.get_player(player).listener
		listener.send(player, message)
	
	def register_command(self, name, inst):
		"""Register the command plugin class instance "inst" by its "name"."""
		self.__commands[name] = inst
	
	def unregister_command(self, name):
		"""Unregister the command "name". Returns True if succeeded, False if 
		the command does not exist."""
		if name in self.__commands:
			del self.__commands[name]
			return True
		return False
	
	def register_listener(self, name, inst):
		"""Register the listener plugin class instance "inst" by its "name"."""
		self.__listeners[name] = inst
	
	def unregister_listener(self, name):
		"""Unregister the listener "name". Returns True if succeeded, False if 
		the listener does not exist."""
		if name in self.__listeners:
			del self.__listeners[name]
			return True
		return False

