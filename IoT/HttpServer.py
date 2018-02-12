from socket import *
import os
import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer

#
# http server: commuicate with doctor's client
#
def httpserver():
	Protocol     = "HTTP/1.0"
	port = 8000
	server_address = ('127.0.0.1', port)
	HandlerClass.protocol_version = Protocol
	httpd = ServerClass(server_address, HandlerClass)
	sa = httpd.socket.getsockname()
	print "Serving HTTP on", sa[0], "port", sa[1], "..."
	httpd.serve_forever()
