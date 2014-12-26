#!/usr/bin/python

import SocketServer

class EchoHandler(SocketServer.BaseRequestHandler):

	def handle(self):

		print "Got Connection from: ", self.client_address

		data = 'dummy'

		while len(data):
			data = self.request.recv(1024)
			print "Client sent: " + data
			self.request.send(data)

		print "Client left"

serverAddress = ('0.0.0.0', 8000)

server = SocketServer.TCPServer(serverAddress, EchoHandler)

server.serve_forever()
