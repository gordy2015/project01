

import socket

def sock_server():
    sock = socket.socket()
    sock.bind(('',9999))
    sock.listen()
    print('starting socket_Server...')


    while True:
        conn, addr = sock.accept()
        print(conn, addr)
        conn.send(b'weclome link to my house...')
        while True:
            print('waiting for data from client...')
            #一个发一句
            data = conn.recv(1024)
            if not data:
                print('client not data, quiting')
                break
            else:
                print('recv:', data.decode())
            f = input('pls input the word>>>')
            if not f:
                break
            conn.send(f.encode())

    sock.close()


sock_server()



