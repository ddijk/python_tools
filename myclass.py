

class MyClass:

    @classmethod
    def run(cls):
        result = add(3,5)
        print(f'result is {result}')
        print('running ' + __class__.__name__)

def add(a, b):
    return a+b


def main():
    job = MyClass()
    print('About to run')
    job.run()
    print('Done running')

if __name__ == '__main__':
    main()
