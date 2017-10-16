
# import socket
#
# client = socket.socket()
# client.connect(('192.168.2.11',5566))
# while True:
#     msg = input('>>:').strip()
#     if len(msg) == 0: continue
#     client.send(msg.encode('utf-8'))
#     data = client.recv(1024)
#     print("recv:", data.decode())
#
# client.close()


#--------------------------------------
# import socket
# s = socket.socket()
# s.connect(('127.0.0.1',9999))
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michael',b'Tracy',b'Sarah']:
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()

#----------------------------------------
import socket
c = socket.socket()
c.connect(('localhost',9900))
while True:
    data = input('>>: ')
    if len(data) == 0:continue
    c.sendall(data.encode())
    rec = c.recv(1024)
    print(rec.decode())
c.close()

