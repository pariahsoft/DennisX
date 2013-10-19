########################################
## Dennis User-Managed MUD Server Kit ##
## __plugin__.py                      ##
## Plugin Base Classes                ##
## Copyright 2013 PariahSoft LLC      ##
########################################

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
	"""Base plugin class for general extensions, and inherited by all other 
	plugin types."""
	def __init__(self, manager):
		self.manager = manager
		self.world = manager.world
		self.path = ""
	
	def set_type(self):
		self.type = "extension"
	
	def set_info(self): # Replace this in your plugin.
		self.name = PLUGIN_NAME
		self.version = PLUGIN_VERSION
	
	def start(self):
		pass
	
	def finish(self):
		pass

class Command(Plugin):
	"""Base plugin class for commands. Inherits "Plugin" class."""
	def set_type(self):
		self.type = "command"

class Database(Plugin):
	"""Base plugin class for database drivers. Inherits "Plugin" class."""
	def set_type(self):
		self.type = "database"

class Listener(Plugin):
	"""Base plugin class for listener drivers. Inherits "Plugin" class."""
	def set_type(self):
		self.type = "listener"

