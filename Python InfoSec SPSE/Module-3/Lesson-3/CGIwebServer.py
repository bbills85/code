#!/usr/bin/env python

import CGIHTTPServer


handler = CGIHTTPServer.CGIHTTPRequestHandler

serve_addr = ("localhost", 8002)

handler.cgi_directories = ['/cgi-bin']

web = CGIHTTPServer.BaseHTTPServer.HTTPServer(serve_addr, handler)

web.serve_forever()
