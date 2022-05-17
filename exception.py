import sys

class MyException(Exception):
    pass

class NoArgsException(Exception):
    pass

def func():
    print(f'hallo: {len(sys.argv)}')
    if len(sys.argv) == 1:
        try:
            raise MyException('Geen args')
        except MyException as ex:
            raise NoArgsException('no args') from ex
     

def main():
    func()

if __name__ == '__main__':
    main()
