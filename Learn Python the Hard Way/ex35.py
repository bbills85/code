from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input("> ")
	if next.isdigit() == True:
		how_much = int(next)
	else:
		dead("Man, learn to type a number")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
# bear function		
def bear_room():
	# prints the following
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	# declares input as false
	bear_moved = False
	
	# while statement to run if/else infinity
	while True:
		# asks for user input
		next = raw_input("> ")
		
		# if/else statement
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
# cthulhu_room function
def cthulhu_room():
	# prints the following
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	# asks for user input
	next = raw_input("> ")
	
	# if/else statement
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
# dead function
def dead(why):
	# prints whatever was sent in and the following, then ends the program
	print why, "Good job!"
	exit(0)

# start function
def start():
	# prints the following
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	# asks for user input
	next = raw_input("> ")
	
	# if/else statement
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
# begins the game, calls the start() function		
#start()
gold_room()