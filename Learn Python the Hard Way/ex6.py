# declaring variables within strings 
x = "There are %d types of people." % 10
# string variable
binary  = "binary"
# string variable
do_not = "don't"
# string variable declared with other string variables
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the following variables x and than y
print x
print y

# prints the raw string and then a regular string
print "I said: %r." % x
print "I also said: '%s'." % y

# declares boolean value
hilarious = False
# declares string with raw string
joke_evaluation = "Isn't that joke funny?! %r"

# prints strings below
print joke_evaluation % hilarious

#declares two strings
w = "This is the left side of..."
e = "a string with a right side."

# prints the combined strings
print w + e