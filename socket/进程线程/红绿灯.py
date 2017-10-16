

import threading,time



def lighter():
    count = 0
    while True:

        if count >5 and count <10:
            print(count,"red light is on ...")

            event.clear()
            time.sleep(1)

        elif count > 10:

            #print(count, "green")
            event.set()
            count = 0
            time.sleep(1)

        else:
            print(count,"green light is on")
            event.set()
            time.sleep(1)
        count += 1

def carer(name):
    while True:
        if event.is_set():
            print('%s running...' % name)
            time.sleep(1)
        else:
            print('saw green light, %s waiting' % name)
            event.wait()
            time.sleep(1)


if __name__ == '__main__':
    event = threading.Event()
    #event.set()
    light = threading.Thread(target=lighter)
    car = threading.Thread(target=carer, args=('BMW',))
    light.start()
    car.start()