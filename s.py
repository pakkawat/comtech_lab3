#!/usr/bin/python           

import socket               # Import socket module

#s = socket.socket()         # Create a socket object
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname() # Get local machine name
port = 80                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
test = "HTTP/1.0 200 OK\nContent-Type:text/html\n\n<h1>Member List</h1>"
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
  
   data = c.recv(1024)
   print "----\n"
   print data
   c.send("okkk") 
   #print c.getpeername()
   #while data != "quit":
       #c.send(test)
       #data = c.recv(1024)
       #print "----\n"
       #print data
   c.close()                # Close the connection

