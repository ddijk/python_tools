import sys


def main():
    flag = sys.argv[1] if len(sys.argv)>1 else None
    print(f'here we go, flag = {flag}')
    if flag:
        user_ids=set()


    user_ids.add('dick')

    print('user ids', user_ids)


if __name__ == '__main__':
    main()
