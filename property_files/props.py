#!/usr/bin/env python3
"""
Purpose: Normalize properties file with parameters of type ${my_param}
"""

import argparse

import re
import os
import copy


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='input1')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Normalize Properties file """

    args = get_args()
    bestand = args.file

    # bestand bevat alle properties en is gemaakt door
    # cat c.properties dd.properties > all.properties

    normalize_props =normalizeFile(bestand)
#    print(normalize_props)

    outputfile='dd.properties'
    fh = open(outputfile, 'wt')
    for k in normalize_props.keys():
        fh.write(f'{k}={normalize_props[k]}\n')

    print(f'Output naar "{outputfile}"')
    fh.close()

def is_valid_property(line):
    return not line.startswith('#') and line.find('=') != -1

def normalizeFile(propertiesFile):
    properties = {}
    for regel in filter(is_valid_property, map(str.strip, propertiesFile)):
        k, v = regel.split('=',maxsplit=1)
        properties[k] = v

    return normalize(properties)


def normalize(properties):
    result = copy.deepcopy(properties)
    for k in properties:
        result[k] = replace(properties[k], properties)

    return result if result == properties else normalize(result)


def replace(value, dict):
    pattern = re.compile(r'\${(.+?)}')
    match = re.search(pattern, value)
    if match:
        replacee = escape_dollar(match.group(0))
        return re.sub(replacee, dict[match.group(1)], value)
    else:
        return value


def escape_dollar(input):
    return ''.join(['\\$' if n == '$' else n for n in input])


# --------------------------------------------------
if __name__ == '__main__':
    main()
