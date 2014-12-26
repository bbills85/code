# Imports argv from the module sys
from sys import argv

# declares the variable names for argv; 2 of them
script, filename = argv

# the variable txt will open the file stored in filename
txt = open(filename)

# prints the following sentence including the filename
print "Here's your file %r:" % filename
# reads the file stored in variable txt
#print txt.read()

# prints one line at a time from the txt variable
print txt.readline()
print txt.readline()

txt.close()

# prints the following sentence
print "Type the filename again:"
# prompts the user to enter the filename
file_again = raw_input("> ")

# the variable txt_again will store the file stored in file_again
txt_again = open(file_again)

# prints out the file stored in variable txt_again
print txt_again.read()

txt_again.close()