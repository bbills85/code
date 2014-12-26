ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

# splits the string ten_things into the list stuff
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	# remove and returns value at index (default last)
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	# add object to the end
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

# stuff index 1
print stuff[1]
# stuff index last
print stuff[-1] # whoa! fancy
print stuff.pop()
# translates to join(' ', stuff); join stuff with ' ' between them
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) #super stellar!