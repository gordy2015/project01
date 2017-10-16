
import multiprocessing,os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getppid())
    print("\n\n")

def f(name):
    info('033[31;1mcalled from child process function f\033[0m')
    print('hello', name)

if __name__ == '__main__':
    info('\033[31;1m main process line\033[0m')
    p = multiprocessing.Process(target=f, args=('bob',))
    p.start()