#!/usr/bin/python           

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 10001                # Reserve a port for your service.
data = ""
s.connect(("pakkawat.cloudapp.net", port))
while data != 'quit':
    data = raw_input()
    s.send(data)
    print s.recv(1024)
s.close                     # Close the socket when done

