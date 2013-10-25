import __plugin__

class Plugin(__plugin__.Plugin):
	def set_info(self):
		self.name = "example"
		self.version = 0
		self.require = "someplugin:3;thatone:1"

