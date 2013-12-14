"""
Victoria Preston
November 9, 2013
Network test code to establish connection with the internet

Tutorial to figure this stuff out: http://www.tutorialspoint.com/unix_sockets/network_addresses.htm
"""

import socket



s = socket.socket()
host = socket.gethostname()
port = 8000
s.bind(('', port))

s.listen(5)
print 'Listening!'
#while False:
#    print 'Oh man, no connection yet!'
while True:
    c, addr = s.accept()
    print c.recv(1024)
    print 'Got the connection from', addr
    c.send('You just got served!')
    c.close()

