# defines a class
class Song(object):
	
	# self is the name of the variable; lyrics is what is passed
	def __init__(self, lyrics):
		 # saying variable_name.lyrics will contain what was passed in
		self.lyrics = lyrics
	
	# self is the name of the variable
	def sing_me_a_song(self):
		# a list is passed in, so a for loop is used to print each index
		# self is the name of the variable; lyrics was what was passed in
		for line in self.lyrics:
			print line

# sends in a list of size 3			
happy_bday = Song(["Happy birthday to you",
				  "I don't want to get sued",
				  "So I'll stop right there"])
				  
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()