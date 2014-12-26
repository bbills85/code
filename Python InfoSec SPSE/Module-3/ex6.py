#!/usr/bin/env python

import BaseHTTPServer
import CGIHTTPServer

BaseHTTPServer.HTTPServer.allow_reuse_address = True
httpServer = BaseHTTPServer.HTTPServer(("", 10000), CGIHTTPServer.CGIHTTPRequestHandler)
httpServer.serve_forever()
