#!/usr/bin/env python

"""

			Creating a Simple HTTP Server

"""

import SocketServer
import SimpleHTTPServer

class HttpRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/admin':
            self.wfile.write('This page is only for Admins!\n')
            self.wfile.write(self.headers)
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

SocketServer.TCPServer.allow_reuse_address = True
httpServer = SocketServer.TCPServer(("", 10000), HttpRequestHandler)
httpServer.serve_forever()
