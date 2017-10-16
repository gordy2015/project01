
import socket
s = socket.socket()
s.bind(('localhost',8989))
s.listen(5)

print('waiting call.....')


conn,addr = s.accept()int('coming.')
print(conn,addr)
while True:
    data = conn.recv(1024)
    print(data)
    f = open("test.txt","rb")
    for line in f:
        conn.send(line)
    f.close()

conn.close()