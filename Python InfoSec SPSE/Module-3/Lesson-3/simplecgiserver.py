#!/usr/bin/env python

import sys
import CGIHTTPServer
from BaseHTTPServer import HTTPServer

servIp = sys.argv[1]
servPort = int(sys.argv[2])

print("Server Starting.  Listening on IP %s and port %d" %(servIp, servPort))
server_address=(servIp,servPort)
httpd = HTTPServer(server_address, CGIHTTPServer.CGIHTTPRequestHandler)
try:
        httpd.serve_forever()
except KeyboardInterrupt:
        pass

print("\nQuitting")
httpServer.server_close()
