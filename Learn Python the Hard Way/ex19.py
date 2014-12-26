# function that takes in two parameters and prints the follow sentences
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# prints the following sentence and inputs numbers to the function	
print "We can just give the functions numbers directly:"
cheese_and_crackers(20, 30)

#prints the following sentence and declares two variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# sends the two variables into the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints the following sentence; sends numbers added together in the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# prints the following sentence; sends variables and numbers added together
# into the function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)