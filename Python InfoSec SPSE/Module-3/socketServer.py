#!/usr/bin/env python

import SocketServer

class EchoHandler(SocketServer.BaseRequestHandler):

    # Methods inherited from BaseRequestHandler:
    #  __init__(self, request, client_address, server)

    # Overrides BaseRequestHanlder handle() method
    # This method handles the incoming requests
    def handle(self):
        print "Got connection from: ", self.client_address
        data = 'dummy'

        while len(data):
            # self.request is the client socket
            data = self.request.recv(1024)
            print "Client sent: " + data
            self.request.send(data)

        print "Client left"

serverAddr = ("0.0.0.0", 9000)

# Instantiating TCPServer class passing in Server Address and Handler Class
server = SocketServer.TCPServer(serverAddr, EchoHandler)
# Handle requests until BaseServer.shutdown() request
server.serve_forever()
