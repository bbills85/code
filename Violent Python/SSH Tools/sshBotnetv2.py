#!/usr/bin/python

import pxssh

class Client:
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.session = self.connect()

	def connect(self):
	        try:
#			print 'connect'
        	        s = pxssh.pxssh()
                	s.login(self.host, self.user, self.password)
                	return s
        	except Exception, e:
#			print e
                	print '[-] Error Connecting'
                	return s

	def send_commands(self, cmd):
#		print 'inside real %r' % cmd
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before

def addClient(host, user, password):
#	print 'addClient'
	client = Client(host, user, password)
	botNet.append(client)

def send_command(cmd):
	for client in botNet:
#		print client
		output = client.send_commands(cmd)
		print '[*] Output from ' + client.host
		print '[+] ' + output

botNet = []

addClient('198.168.138.130', 'root', 'toor')
#addClient('198.168.138.133', 'root', 'toor')

#print botNet
send_command('uname -a')
send_command('cat /etc/issue')
