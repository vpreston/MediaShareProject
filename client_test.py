"""
Victoria Preston
November 9, 2013
Testing code to set-up a network
"""

import socket

s = socket.socket()
host = socket.gethostname()
port = 8000


s.connect((host, port))

s.send('Hey there server!')

print s.recv(1024)

s.close
