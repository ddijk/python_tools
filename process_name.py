import time
from multiprocessing import Process
import setproctitle

def func():
    i = 0
    setproctitle.setproctitle(multiprocessing.current_process().name)
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
