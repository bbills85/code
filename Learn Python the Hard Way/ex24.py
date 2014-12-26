# prints the following sentences with escape characters
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

# variable poem with extended comments """ incorporated
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# prints the following sentences with the variable poem
print "-------------"
print poem
print "-------------"

# variable five with addition and subtraction performed
five = 10 - 2 + 3 - 6
# prints the following sentence with variable five as a string
print "This should be five: %s" % five

# defined function with one parameter
# three variables within the function
# returns three values
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

# declares variable start_point with 10000
start_point = 10000
# declares three variables with the function secret_formula
beans, jars, crates = secret_formula(start_point)

# prints the following sentences with decimals
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# variable divided 10
start_point = start_point / 10

# prints the following sentences with function call
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)