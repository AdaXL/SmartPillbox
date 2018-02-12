#
# server does:
# 1. call http server  2. call pillbox server 3. dell with the data
#


from socket import *
import os
import sys
import HttpServer
import PillboxServer


#
# main control: create two process pillboxserver and httpserver
#

pid = os.fork()
if pid == 0:
	print 'init http server'
	HttpServer.httpserver()
else:
    print 'init pillbox server'
    PillboxServer.pillboxserver()

