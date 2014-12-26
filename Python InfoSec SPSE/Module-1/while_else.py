#!/usr/bin/python

print "While Else Loop Example!"

age = raw_input("Enter your age: ")

while int(age) == 28:
	print "BOOM BABY! You're 28!!"
	break

else:
	print "Not so much."

print "Were outside the While Else Loop now."
