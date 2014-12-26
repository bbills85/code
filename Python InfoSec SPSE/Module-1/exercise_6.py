#!/usr/bin/python

# parent class to contain function override
class Parent(object):

	var = 'local variable to the class'

	print var
	
	def override(self):
		var = "PARENT() override()"
		print var
	
	print var

# child class must contain override function or parent class will always execute
class Child(Parent):

	def override(self):
		print "CHILD() override()"

var = 'local variable to the program'

father = Parent()
son = Child()

father.override()
son.override()
	
print var
