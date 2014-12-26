#!/usr/bin/python

import SocketServer

class EchoHandler(SocketServer.BaseRequestHandler):

	def handle(self):
		print "def in class"
		print "Got Connection from: ", self.client_address

		data = 'dummy'

		while len(data):
			data = self.request.recv(1024)
			print "Client sent: " + data
			self.request.send(data)
		print "Client left"

serverAddress = ('0.0.0.0', 8000)

try:
	SocketServer.ThreadingTCPServer.allow_reuse_address = True
	server = SocketServer.ThreadingTCPServer(serverAddress, EchoHandler)
	print "[+] server initalized at " + str(server.server_address)
except:
	print "[-] server initalization failed"
finally:
	server.serve_forever()

