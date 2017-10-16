#
# import threading
# import time
#
# def show(arg):
#     time.sleep(1)
#     print('thread' +str(arg))
# for i in range(10):
#     t = threading.Thread(target=show, args=(i,))
#
#     t.start()
# print('main thread stop')

#------------------------------

# import threading
# import time
# class Mythread(threading.Thread):
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num = num
#     def run(self):
#         print("running on number: %s" %self.num)
#         time.sleep(3)
#
# if __name__ == '__main__':
#     t1 = Mythread(1)
#     t2 = Mythread(2)
#     t1.start()
#     t2.start()

#------------------------------------

# import threading
# import time
# num = 0
# def show(arg):
#     global num
#     time.sleep(1)
#     num += 1
#     print(num)
#
# for i in range(10):
#     t = threading.Thread(target=show, args=(i,))
#     t.start()
# def loo():
#     print('thread %s is running...' %threading.current_thread().name)
# # s = show
# # print(s)
# # print('main thread stop')
# print(loo())
#----------------------------------

# import threading
# import time
# num = 0
# lock = threading.RLock()
# def Func():
#     lock.acquire()
#     global num
#     num += 1
#     time.sleep(1)
#     print(num)
#     lock.release()
# for i in range(10):
#     t = threading.Thread(target=Func)
#     t.start()

#-----------------------------
# import threading,time
# def run(n):
#     semaphore.acquire()
#     time.sleep(1)
#     print("run the thread: %s" %n)
#     semaphore.release()
# if __name__ == '__main__':
#    num = 0
#     semaphore = threading.BoundedSemaphore(5)
#     for i in range(20):
#         t = threading.Thread(target=run, args=(i,))
#         t.start()

#-----------------------------------------------

# import threading, time
# def sayhi(num):
#     print("running on number: %s" %num)
#     time.sleep(3)
# if __name__ == '__main__':
#     t1 = threading.Thread(target=sayhi, args=(1,))
#     t2 = threading.Thread(target=sayhi, args=(2,))
#     t1.start()
#     t2.start()
#     print(t1.getName())
#     print(t2.getName())

#-------------------------------------------------

# import threading, time
# def run(n):
#     print('[%s]------running------\n' % n)
#     time.sleep(2)
#     print('--done--')
# def main():
#     for i in range(5):
#         t = threading.Thread(target=run, args=[i,])
#         t.start()
#         t.join(1)
#         print('starting thread', t.getName())
#
# m = threading.Thread(target=main, args=[])
# m.setDaemon(True)
# m.start()
# m.join(timeout=2)
# print('---main thread done---')

# import threading
# import time
#
#
# class MyThread(threading.Thread):
#     def __init__(self, num):
#         threading.Thread.__init__(self)
#         self.num = num
#
#     def run(self):  # 定义每个线程要运行的函数
#
#         print("running on number:%s" % self.num)
#
#         time.sleep(3)
#
#
# if __name__ == '__main__':
#     t1 = MyThread(1)
#     t2 = MyThread(2)
#     t1.start()
#     t1.join()
#     t2.start()
#     t2.join()


# import time
# import threading
#
#
# def addNum():
#     global num  # 在每个线程中都获取这个全局变量
#     print('--get num:', num)
#     time.sleep(1)
#     num -= 1  # 对此公共变量进行-1操作
#
#
# num = 100  # 设定一个共享变量
# thread_list = []
# for i in range(100):
#     t = threading.Thread(target=addNum)
#     t.start()
#     thread_list.append(t)
#
# for t in thread_list:  # 等待所有线程执行完毕
#     t.join()
#
# print('final num:', num)


# import time
# import threading
#
#
# def addNum():
#     global num  # 在每个线程中都获取这个全局变量
#     print('--get num:', num)
#     time.sleep(1)
#     lock.acquire()  # 修改数据前加锁
#     num -= 1  # 对此公共变量进行-1操作
#     lock.release()  # 修改后释放
#
#
# num = 100  # 设定一个共享变量
# thread_list = []
# lock = threading.Lock()  # 生成全局锁
# for i in range(100):
#     t = threading.Thread(target=addNum)
#     t.start()
#     thread_list.append(t)
#
# for t in thread_list:  # 等待所有线程执行完毕
#     t.join()
#
# print('final num:', num)


# import threading, time
#
#
# def run1():
#     print("grab the first part data")
#     lock.acquire()
#     global num
#     num += 1
#     lock.release()
#     return num
#
#
# def run2():
#     print("grab the second part data")
#     lock.acquire()
#     global num2
#     num2 += 1
#     lock.release()
#     return num2
#
#
# def run3():
#     lock.acquire()
#     res = run1()
#     print('--------between run1 and run2-----')
#     res2 = run2()
#     lock.release()
#     print(res, res2)
#
#
# if __name__ == '__main__':
#
#     num, num2 = 0, 0
#     lock = threading.RLock()
#     for i in range(1):
#         t = threading.Thread(target=run3)
#         t.start()
#
# while threading.active_count() != 1:
#     print(threading.active_count())
# else:
#     print('----all threads done---')
#     print(num, num2)

import threading,time

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s\n" %n)
    semaphore.release()

if __name__ == '__main__':
    num = 0
    semaphore = threading.BoundedSemaphore(1)
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()
while threading.active_count() != 1:
    pass
else:
    print('---all threads done---')
    print(num)