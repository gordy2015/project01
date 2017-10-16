

import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sk.bind(("127.0.0.1",9922))
sk.listen(5)

print("starting listen...")
while True:
    conn, address = sk.accept()
    print(conn, address)
    conn.sendall(bytes("hi", encoding="utf-8"))

sk.close()







