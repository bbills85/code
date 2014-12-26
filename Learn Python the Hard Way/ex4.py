# Variables declared for program
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
# Taking the subtraction of cars minus drivers
cars_not_driven = cars - drivers
cars_driven = drivers
# Taking the capacity based on the amount of cars driven and space in the cars
carpool_capacity = cars_driven * space_in_a_car
# Takes the average passengers per car by dividing the passengers by cars driven
average_passengers_per_car = passengers / cars_driven


# Prints the following sentences and variables
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."