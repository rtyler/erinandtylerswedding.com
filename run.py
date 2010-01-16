#!/usr/bin/env python

import BaseHTTPServer
import SimpleHTTPServer

if __name__ == '__main__':
    server = BaseHTTPServer.HTTPServer(('', 8081), SimpleHTTPServer.SimpleHTTPRequestHandler)
    server.serve_forever()

