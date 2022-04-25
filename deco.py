

def mydeco(fie):
    def wrapper():
        print('before running')
        fie()
        print('after running')

    return wrapper

@mydeco
def myfunc():
    print('running myfunc')

def main():
    myfunc()

if __name__=='__main__':
    main()
