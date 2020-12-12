#!/usr/bin/env python3
"""tests for double.py"""

import os
from subprocess import getoutput

prg = './double.py'

def test_a():
    out = getoutput(f'{prg} "aa aa "')
    expected= 'found double word: "aa"'
    assert out.strip() == expected

def test_b():
    out = getoutput(f'{prg} "bb bb "')
    expected= 'found double word: "bb"'
    assert out.strip() == expected