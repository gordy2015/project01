
import socket
sock = socket.socket()
sock.connect(('127.0.0.1',9999))

while True:
    # 一个发一句
    print('waiting for data from server')
    data = sock.recv(1024)
    if not data:
        print('server not data, quiting')
        break
        sock.close()
    else:
        print(data)
    q = input('pls input the word>>>')
    if not q:
        break
    sock.send(q.encode('utf-8'))

