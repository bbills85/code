size = 10
update_rate = 2
numbers = []

def after(update_rate):
	i = 0
	z = i
	for i in range(0, size):
		print "At the top of append is %d" % z	
		numbers.append(z)
		z += update_rate
		print "Numbers now: ", numbers
		print "At the bottom append is %d" % z

after(update_rate)

print "The numbers: "

for num in numbers:
	print num