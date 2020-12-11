#!/usr/bin/env python3
"""tests for gitlog.py"""

import os
from subprocess import getstatusoutput

prg = './gitlog.py'

def test_a():
    rv, out = getstatusoutput(f'{prg} lijst')
    # print(out)
    assert rv == 0
    expected= ('https://jira.ontwikkel.local/browse/HHOPPDEV-12345\n'
               'https://jira.ontwikkel.local/browse/HHOPPDEV-7722')
    assert out.strip() == expected