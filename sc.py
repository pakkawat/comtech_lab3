import threading
import socket
import time

class myServer (threading.Thread):
    def __init__(self, host, port):
      threading.Thread.__init__(self)
      self.host = host
      self.port = port

    def run(self):
      s = socket.socket()
      s.bind((self.host, self.port))
      s.listen(5)
      while True:
        c, addr = s.accept()
        print 'Got connection from', addr
        data = c.recv(1024)
        while data != "quit":
          c.send(data)
          data = c.recv(1024)
        c.close()

class myClient (threading.Thread):
    def __init__(self, host, port):
      threading.Thread.__init__(self)
      self.host = host
      self.port = port

    def run(self):
      time.sleep(5)
      s = socket.socket()
      data = ""
      s.connect((self.host, self.port))
      while data != 'quit':
        data = raw_input()
        s.send(data)
        print s.recv(1024)
      s.close

# Create new threads
sv = myServer(socket.gethostname(), 10001)
cl = myClient("chuchai.cloudapp.net", 10002)

# Start new Threads
sv.start()
cl.start()

