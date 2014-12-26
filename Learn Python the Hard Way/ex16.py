# import argv from sys module
from sys import argv

# two argv when running program
script, filename = argv

# print the following sentences with filename string in raw format
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# wait for user interaction
raw_input("?")

# print the following sentence and open the file to object "target"
print "Opening the file..."
target = open(filename, 'w')

# print the following sentence and erase the file
print "Truncating the file. Goodbye!"
target.truncate()

# print the following sentence
print "Now I'm going to ask you for three lines."

# ask for user input with the following variables
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# print the following sentence
print "I'm going to write these to the file."

# write the following variables to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# prints the following sentence and closes the file
print "And finally, we close it."
target.close()