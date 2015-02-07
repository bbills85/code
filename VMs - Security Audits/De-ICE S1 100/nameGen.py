#!/usr/bin/python

import optparse
import sys

def main():
	parser = optparse.OptionParser("usage: %prog -f <input file> -o <output file>")

	parser.add_option("-f", dest = "inputFile",
			  type = "string", help = "specify username input file")
	parser.add_option("-o", dest = 'outputFile',
			  type = "string", help = "specify username output file")

	(options, args) = parser.parse_args()

	if (options.inputFile == None) | (options.outputFile == None):
		print parser.usage
		exit(0)
	else:
		inputFile = options.inputFile
		outputFile = options.outputFile

	fromFile = open(inputFile)
	toFile = open(outputFile, 'w')

	for line in fromFile.readlines():
		name = line.lower().strip('\r\n').split(' ')

		toFile.write(name[0] + '\n')			# bob
		toFile.write(name[1] + '\n')			# smith
		toFile.write(name[0] + name[1] + '\n')		# bobsmith
		toFile.write(name[1] + name[0] + '\n')		# smithbob
		toFile.write(name[0] + "." + name[1] + '\n')	# bob.smith
		toFile.write(name[1] + "." + name[0] + '\n')	# smith.bob
		toFile.write(name[1] + name[0][0] + '\n')	# smithb
		toFile.write(name[1] + "." + name[0][0] + '\n') # smith.b
		toFile.write(name[0][0] + name[1] + '\n')	# bsmith
		toFile.write(name[0][0] + "." + name[1] + '\n') # b.smith
		toFile.write(name[0] + name[1][0] + '\n')	# bobs
		toFile.write(name[0] + "." + name[1][0] + '\n')	# bob.s
		toFile.write(name[1][0] + name[0] + '\n')	# sbob
		toFile.write(name[1][0] + "." + name[0] + '\n')	# s.bob

	fromFile.close()
	toFile.close()

if __name__ == "__main__":
	main()
