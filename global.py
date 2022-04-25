result  =10
def add(value1, value2):
    global result
    result = value1 + value2

def main():
    print(result)
    add(2, 4)
    print(result)

if __name__=='__main__':
    main()
