#!/usr/bin/python

import pexpect

PROMPT = [ '# ', '>>> ', '> ', '$ ' ]

print PROMPT

def send_command(child, cmd):
	# gives control to the user
#	child.interact()
	# sends cmd
	child.sendline(cmd)
	# what is expected after sending the command (this example is the prompt)
	child.expect(PROMPT)
	# prints the sendline and results
	print child.before

def connect(user, host, password):
	# declare two strings to use if needed
	ssh_newkey = 'Are you sure you want to continue connecting'
	connStr = 'ssh ' + user + '@' + host

	# spawn an external child command and then interact with the child 
	# by sending lines and expecting responses.
	child = pexpect.spawn(connStr)
	# create a list with pexpect expecting one of the following outputs (0, 1, 2)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])

	print ret
	# if a timeout occurs perform the following
	if ret == 0:
		print 'ZERO'
		print '[-] Error Connecting'
		return
	# if ssh_newkey is asked do the following
	if ret == 1:
		print 'ONE'
		# send yes if asking ssh_newkey
		child.sendline('yes')
		# create new expecting list with timeout or password
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
		print child.before
		# if another timeout occurs else send the password
		if ret == 0:
			print '[-] Error Connecting'
			return
	print 'TWO'
	# send the password variable
	child.sendline(password)
	# expect a prompt returned
	child.expect(PROMPT)
	print child.before
	# return the child spawn
#	print child (debugging)
	return child
	
def main():
	# variables for host username and password
	host = 'localhost'
	user = 'root'
	password = 'toor'
	
	# send three variables to connect and return to store in child
	child = connect(user, host, password)
	# send child object and command	
	send_command(child, 'cat /etc/shadow | grep root')

if __name__ == '__main__':
	main()

# good place for more info http://www.pythonforbeginners.com/systems-programming/how-to-use-the-pexpect-module-in-python
# http://pexpect.sourceforge.net/pexpect.html
