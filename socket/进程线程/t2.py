
#
# import _thread
# import time
# def print_time( threadName, delay ):
#     count = 0
#     while count <5:
#         time.sleep(delay)
#         count += 1
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#
# try:
#     _thread.start_new_thread(print_time,("Thread-1",2, ))
#     _thread.start_new_thread(print_time,("Thread-2",4, ))
# except:
#     print("Error: 无法启动线程")
#
# while 1:
#     pass

import time
import threading
def addNum():
    global addNum
    print('---get num:', num)
    time.sleep(1)
    num -= 1
num = 100
thread_list=[]
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)
for t in thread_list:
    t.join()
print('final num:', num)

