# create a mapping of state to abbreviation
# creates a dict states
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states and some cities in them
# creates a dict cities
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the states then cities dict
# calls the state, gets abbreviation, which cities calls to get the city
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
# print every city in state
# items() returns a list of dict's (key, value) tuple pairs with variables
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

#print cities.items()
	
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be the there
# checks if Texas is in states, if not does None
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."
	
# get a city with a default value
# checks if TX is in cities if not Does Not Exist
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
