def bar(*args, **kwargs):
    for i in args:
        print(f'args {i}')
    for a in kwargs:
        print(a, kwargs[a])  

def fun(a,b):
    print(f'a={a} en b={b}')


def main():
    bar('hallo','daar',name='one', age=27)
    fun(*[12,13])

if __name__=='__main__':
    main()
