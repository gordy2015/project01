

import socket

sc = socket.socket()
sc.connect(("127.0.0.1", 9922))
print(sc.recv(1024))
sc.close()


