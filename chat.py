# chatserver5.py

import socket, threading

class server5(threading.Thread) :
   def __init__(self, (socket, address) ):
      threading.Thread.__init__(self)
      self.SOCKET=socket
      self.ADDRESS=address

   def run(self) :
      lock.acquire()
      vector.append(self)
       lock.release()
      print 'Connected ', self.ADDRESS
      while True :
         From=self.SOCKET.recv(1024) # Read from client
         if not From : break
         for s in vector :
               if s != self :
                  s.SOCKET.send(From)
         self.SOCKET.close()
      print 'Disconnected ', self.ADDRESS
      lock.acquire()
      vector.remove(self)
       lock.release()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 888))
s.listen(4)
vector = []
lock=threading.Lock()

while True :             # Wait for connection/run server
   server5( s.accept() ).start();
