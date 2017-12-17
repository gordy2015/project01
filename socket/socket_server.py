
# import socket
# server = socket.socket()
# server.bind(('localhost',5566))
# server.listen(5)
#
# print('我要开始等电话了')
#
# while True:
#     conn,addr = server.accept()
#     print(conn,addr)
#     print('电话来了')
#     while True:
#         data = conn.recv(1024)
#         print('recv:', data.decode())
#         conn.send(data.upper())
#
# server.close()



#--------------------------------------------
# import socket
# s = socket.socket()
# s.bind(('127.0.0.1',9999))
# s.listen(5)
# print('waiting for connection...')
#
# def tcplink(sock,addr):
#     print('Accept new connection from %s: %s...' % addr)
#     sock.send(b'Welcome')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s: %s closed' % addr)
# while True:
#     sock, addr = s.accept()
#     t = threading.Thread(target=tcplink, args=(sock,addr))
#     t.start()
#-------------------------------------------

import socket
s = socket.socket()
s.bind(('localhost',9900))
s.listen(5)

print('waiting call.....')


conn,addr = s.accept()
print('coming.')
print(conn,addr)
while True:
    data = conn.recv(1024)
    print(data)
    conn.sendall(data.upper())

conn.close()