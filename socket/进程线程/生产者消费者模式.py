
import threading,queue,time

def producer():
    for i in range(10):
        q.put('骨头 %s' %i)
        print("生产骨头 %s" %i)
        #time.sleep(1)

    q.join()

def customer(n):
    while q.qsize() >0:
        print("%s 取到" %n , q.get())
        q.task_done()

q = queue.Queue()

p = threading.Thread(target=producer,)
c = threading.Thread(target=customer,args=('alex',))
p.start()
c.start()
c1 = customer("alex")