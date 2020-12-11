#!/usr/bin/env python3
"""
Author : isc75529 <isc75529@localhost>
Date   : 2020-12-11
"""

import argparse

import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print JIRA issue nr ',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    # overzicht van alle gemergede issues tussen twee tags:
    # git log 2.18.0..2.19.0 | grep HHOPPDEV > git_log_release_2.19
    parser.add_argument('file',
                      help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.file

    jira_issues = set()

    pattern=r'(HHOPPDEV-\d{2,5})'
    for line in file_arg:

        match = re.search(pattern, line.strip())
        if match:
            jira_issues.add(match.group(1))

    jira_list = list(jira_issues)
    jira_list.sort()
    for issue in jira_list:
        print(f'https://jira.ontwikkel.local/browse/{issue}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
