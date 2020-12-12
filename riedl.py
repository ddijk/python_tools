#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2020-12-12
Purpose: Regex tester
"""

import argparse

import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='pattern',
                        help='regex pattern')

    parser.add_argument('text',
                        metavar='str',
                        help='text to use in regex')

    parser.add_argument('-d',
                        '--debug',
                        help='flag to print debug info ',
                        action='store_true')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    pattern = args.pattern
    debug=args.debug

    if debug:
        print(f'text = "{text}"')
        print(f'pattern = "{pattern}"')

    # pattern= r'^(SUBJECT|FROM)'
    m = re.search(pattern, text)

    # print(m)

    if m:
        print(m.group(0))
        if ( len(m.groups())):
            if debug:
                print(f'matched "{m.group(1)}"')
    else:
        print('no match')


# --------------------------------------------------
if __name__ == '__main__':
    main()
