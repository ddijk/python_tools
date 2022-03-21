import time
from multiprocessing import Process
import multiprocessing
import setproctitle

def func():
    i = 0
    naam = multiprocessing.current_process().name
    print(f'name to set is {naam}')
    setproctitle.setproctitle(naam)
    while True:
        print(f'Running {i}')
        i = i + 1
        time.sleep(3)

def main():
    print('hallo, about to start new process')
    p = Process(target=func, name='my_func')
    p.start()
    print('main ended')


if __name__=='__main__':
    main()
