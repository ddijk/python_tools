#!/usr/bin/env python3
"""
Date   : 2020-11-26
Purpose: Rock the Casbah
"""

import argparse
from string import Template


def upper(s): 
    return s.upper()

def strip(s):
    return s.strip()
# --------------------------------------------------
def main():
    """Make a jazz noise here"""


    def is_valid_property(line):
        return not line.startswith('#') and line.find('=') != -1
 
    props = {}
    for line in filter(is_valid_property, map(str.strip, open('all.properties', 'rt').readlines())):
        key, value = line.split('=', maxsplit=1)
        props[key] = value
        # print(f'key={key} en value is {value}')
#    print(props)
    
    for k in props:
         print(f'{k}={props[k]}')
    # print(''.join(map(str, map(len, ['a','b','noot']))))
    # print(''.join(map(str.lower, ['aBC ','b','noot'])))





# --------------------------------------------------
if __name__ == '__main__':
    main()



