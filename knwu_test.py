#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2021-05-24
Purpose: Rock the Casbah
"""

import argparse
import json
import re
import time


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

    # writeRaces(file_arg)

    for i in range(1,10):
        print(f"page {i}", end='\r' if i<9 else '\n')
        time.sleep(1)



def writeRaces(file_arg):
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


def filterCat(cat, e):
    if not 'races' in e:
        return False
    for cat_name in map(lambda y: y['name'], e['races']):
        if re.search(r'Nieuweling.*\(M\)',cat_name):
            return True 

    return False

# --------------------------------------------------
if __name__ == '__main__':
    main()
