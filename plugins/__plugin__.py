#########################################
## DennisX User-Managed MUD Server Kit ##
## __plugin__.py                       ##
## Plugin Base Classes                 ##
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

class Plugin:
	"""Base plugin class."""
	def __init__(self, manager):
		self.manager = manager
		self.world = manager.world
		self.path = ""
		self.running = False
	
	def set_info(self):
		"""Sets the plugin info. This method is only an example; change the 
		values when you redefine it in your plugin."""
		self.name = PLUGIN_NAME
		self.version = PLUGIN_VERSION
		self.require = PLUGIN_REQUIRE
	
	def start(self):
		"""Start the plugin. Any initialization code should go here."""
		pass
	
	def tick(self):
		"""Run once per tick."""
		pass
	
	def finish(self):
		"""Finish the plugin. Any clean up code should go here."""
		pass
	
	def send(self, player, message):
		"""Listener plugins only. Send "message" to the "player" identified by 
		player id."""
		pass
	
	def get_lines(self):
		"""Listener plugins only. Returns all lines that have been collected 
		since the last call, in format ((player id, line text), ...)."""
		pass
	
	def command(self, player, cmdstring):
		"""Command plugins only. Tell the command it is being called by 
		player id "player" with the arguments "cmdstring"."""
		pass
	

