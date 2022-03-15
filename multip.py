from multiprocessing import Process
import time

def f(name):
    time.sleep(2)
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    print('started a new processs')
#    p.join()
    print('end of main thread')
