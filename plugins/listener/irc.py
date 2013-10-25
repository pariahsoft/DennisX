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

import os, socket, string, sys

class Plugin:
	"""IRC Listener Plugin v1"""
	def __init__(self, manager):
		self.manager = manager
		self.world = manager.world
		self.path = ""
	
	def set_info(self):
		self.name = "listener_irc"
		self.version = 1
		self.require = ""
	
	def start(self):
		self.linebuf = []
		socket.setdefaulttimeout(float(self.world.config.get("irc", "timeout")))
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		self.world.console.register_listener(self.name, self)
		
		if not self.connect():
			self.socket.close()
			return False
		return True
	
	def tick(self):
		self.receive()
		
		for line in self.linebuf:
			try:
				if line[0:4] == 'PING': # Ping received.
					self.socket.send('PONG {0}\r\n'.format(line[5:]))
			
				elif line.split(' ')[1] == "002": # We're connected.
					self.socket.send('MODE {0} +B\r\n'.format(self.world.config.get("irc", "nickname")))
				
					if self.world.config.get("irc", "nickservpass"):
						self.socket.send('PRIVMSG NICKSERV :IDENTIFY {0}\r\n'.format(\
						self.world.config.get("irc", "nickservpass"))) #Identify with nickserv.
				
					for channel in self.world.config.get("irc", "channels").split(','):
						channel = channel.split(',')
						if len(channel) > 1:
							self.socket.send('JOIN {0} {1}\r\n'.format(channel[0], channel[1]))
						else:
							self.socket.send('JOIN {0}\r\n'.format(channel[0]))
			except IndexError:
				pass
	
	def finish(self):
		self.socket.close()
	
	def connect(self):
		try:
			host, port = self.world.config.get("irc", "server").split(',')
			self.socket.connect((host, int(port)))
			self.socket.setblocking(0)
			self.socket.send("NICK {0}\r\n".format(self.world.config.get("irc", "nickname")))
			
			self.receive()
			for line in self.linebuf:
				if line.split(' ')[1] == "443": # Nickname is in use.
					return False
			
			self.socket.send('USER {0} 8 * :{1}\r\n'.format(\
			self.world.config.get("irc", "username"), \
			self.world.config.get("irc", "realname")))
			
			return True
		except socket.error:
			return False
	
	def receive(self):
		try:
			buf = self.socket.recv(int(self.world.config.get("irc", "recvsize")))
			while not buf.endswith('\n'):
				buf += self.socket.recv(int(self.world.config.get("irc", "recvsize")))
			self.linebuf.extend(buf.split('\n'))
		except socket.error:
			pass
	
	def send(self, player, message):
		player = self.world.get_player(player)
		self.socket.send("PRIVMSG {0} :{1}\r\n".format(player.username, message))
	
	def get_lines(self):
		lines = []
		
		for line in self.linebuf:
			for char in line:
				if not char in string.printable: # Ignore weird characters.
					line = line.replace(char, '')
			
			complete = line[1:].split(':',1) # Split message into sections
			info = complete[0].split(' ') # Pieces of message
			
			try:
				info[1]
				msgpart=complete[1].rstrip()
			except IndexError: # Fake line
				continue
			
			sender = info[0].split('!')[0]
			player = self.world.get_player_by_username(sender)
			if not player:
				continue
			playerid = player.id
			
			lines.append((playerid, info[1:]))
		
		self.linebuf = []
		
		return tuple(lines)

