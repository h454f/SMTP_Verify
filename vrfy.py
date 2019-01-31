#!/usr/bin/env python
import socket
import sys
if len(sys.argv) != 3:
	print "[==>] Usage: vrfy.py <username> <server>"
	print "[==>]    EG: vrfy.py <username> 127.0.0.1"
        sys.exit(0)

# create the socket 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the target SMT Server
connect=s.connect((sys.argv[2],25))
# receive and print the banner
banner=s.recv(1024)
print banner
# start the VRFY loop
s.send('VRFY ' + sys.argv[1] + '\r\n')
result=s.recv(1024)
print result
# the program exits
s.close()
