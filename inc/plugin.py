#########################################
## DennisX User-Managed MUD Server Kit ##
## plugin.py                           ##
## Plugin Manager                      ##
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

import glob, imp, os, string

class PluginManager:
	"""This class manages the plugin registry. The class instance also emulates 
	a read-only dictionary, where the key is the plugin name and the value is 
	the plugin class instance."""
	def __init__(self, world):
		self.__plugins = {}
		self.world = world
	
	def __contains__(self, name):
		if name in self.__plugins:
			return True
		return False
	
	def __getitem__(self, name):
		if self.__contains__(name):
			return self.__plugins[name]
		raise KeyError
	
	def load(self, path):
		"""Load the plugin at "path" into the registry, and return the plugin 
		name. Returns None if the plugin info is invalid."""
		mname = os.path.splitext(os.path.split(path)[-1])[0]
		inst = imp.load_source(mname, path).Plugin(self)
		inst.set_info()
		
		for c in inst.name:
			if not c in string.ascii_lowercase+"_":
				return False
		for c in inst.require:
			if not c in string.ascii_lowercase+string.digits+"_:;":
				return False
		if not type(inst.version) == int:
			return False
		
		self.__plugins[inst.name] = inst
		self.__plugins[inst.name].path = path
		self.__plugins[inst.name].start()
		
		return name
	
	def load_glob(self, match):
		"""Load all plugins matching a shell glob, and return a list of plugin 
		names loaded."""
		pluginlist = []
		for path in glob.glob(match):
			pluginlist.append(self.load(path))
		return pluginlist
	
	def autoload(self):
		"""Load all plugins listed in the config plugin path. Returns True if 
		succeeded, False if failed."""
		for path in self.world.config.get("plugin", "load").split(';')
			path = self.world.config.get("plugin", "path")+"/"+path
			if not self.load_glob(path):
				return False
		if not self.check_deps():
			return False
		return True
	
	def unload(self, name):
		"""Remove the plugin "name" from the registry."""
		self.__plugins[name].finish()
		del self.__plugins[name]
	
	def check_deps(self):
		"""Verify that all dependencies are fulfilled in the plugin registry. 
		Returns True if succeeded, False if failed."""
		for plugin in self.__plugins:
			for req in plugin.require.split(';'):
				n, v = req.split(':')
					if not n in self.__plugins or \
					v != self.__plugins[n].version
						return False
		return True
	
	def reset(self, name):
		"""Reset the plugin "name"."""
		path = self.__plugins[name].path
		self.unload(name)
		self.load(path)

