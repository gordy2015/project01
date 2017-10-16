import  multiprocessing
# import time
# def f(name):
#     time.sleep(2)
#     print('hello', name)
#
# if __name__ == '__main__':
#     p = multiprocessing.Process(target=f, args=('bob',))
#     p.start()
#     p.join()


#-----------------------------
# from multiprocessing import Queue
# def f(q):
#     q.put([42, None, 'he)
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()


