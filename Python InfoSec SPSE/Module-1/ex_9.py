#!/usr/bin/python

class pin(object):

	def __init__(self, num):
		try:
			int(num)
		except:
			print "Contains something other then a number!"
		else:
			self.num = num
		finally:
			print "Goodbye!"


pin_num = raw_input("Enter 4 digit PIN: ")
pin = pin(pin_num)
