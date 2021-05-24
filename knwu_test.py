#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2021-05-24
Purpose: Rock the Casbah
"""

import argparse
import json


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument')

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
                        required=False,
                        type=argparse.FileType('rt'),
                        default='testdata.json')

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
    # pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    # print(f'positional = "{pos_arg}"')

    data = json.load(file_arg)

    cat = 'Nieuwelingen (M)' 
    # filter out races for Nieuwelingen:
    res =  list(filter(lambda x: filterCat(cat, x),  data))

    out_fh = open('out.txt', 'wt')
    for i in res:
        datum = i["date"][0]
        out_fh.write(f'wedst: {i["name"]} op {datum} state={i["state"]}\n')
        print(f'wedst: {i["name"]} op {datum} state={i["state"]}')

    out_fh.close()

    a1 = { 'races': [{ 'name': 'dick', 'age': 47}, { 'name': 'xxx', 'age': 47}]}
    a2 = { 'races': [{ 'name': 'jens', 'age': 15}, { 'name': 'yyy', 'age': 15}]}

    a = [a1, a2]

    print(filterCat('dick', a1))
    print('-----------')
    print(filterCat('dick', a2))



def filterCat(cat, e):
    if not 'races' in e:
        return False
    a = map(lambda y: y['name'], e['races'])
    print(list(a))
    return cat in map(lambda y: y['name'], e['races'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
