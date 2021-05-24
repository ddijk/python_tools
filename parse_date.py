#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2021-02-25
Purpose: Rock the Casbah
"""

import argparse
import datetime
import dateutil.relativedelta


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')
    a_date = datetime.datetime.strptime("2019-01-13", "%Y-%m-%d")
    print(a_date)
    a_month = dateutil.relativedelta.relativedelta(months=1)
    date_plus_month = a_date + a_month
    print(date_plus_month)
    date_minus_month = a_date - a_month
    print(date_minus_month)

    if pos_arg.isnumeric():
        print(f'{pos_arg} is numeric')
    else:
        print(f'{pos_arg} is niet numeric')

    if not pos_arg.isnumeric():
        print(f'{pos_arg} is NOT numeric')
    else:
        print(f'{pos_arg} is WEL numeric')

# --------------------------------------------------
if __name__ == '__main__':
    main()
