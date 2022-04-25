

class MyClass:

    @classmethod
    def run(cls):
        print('running ' + __class__.__name__)


def main():
    job = MyClass()
    print('About to run')
    job.run()
    print('Done running')

if __name__ == '__main__':
    main()
