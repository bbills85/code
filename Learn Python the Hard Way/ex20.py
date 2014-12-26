# importing argv from sys
from sys import argv

# declaring two arguments for argv
script, input_file = argv

# function to print the entire file
def print_all(f):
	print f.read()

# function to move to any part of the file
def rewind(f):
	f.seek(0)

# function to print the parameter line_count and the current line
def print_a_line(line_count, f):
	print line_count, f.readline()

# declares variable to hold the file
current_file = open(input_file)

# prints the following sentence
print "First let's print the whole file:\n"

# calls print_all
print_all(current_file)

# prints the following sentence
print "Now let's rewind, kind of like a tape."

# calls rewind
rewind(current_file)

# prints the following sentence
print "Let's print three lines:"

# declares variable and stores 1; calls print_a_line
current_line = 1
print_a_line(current_line, current_file)

# declares variable and stores 2; calls print_a_line
current_line += 1
print_a_line(current_line, current_file)

# declares variable and stores 3; calls print_a_line
current_line += 1
print_a_line(current_line, current_file)