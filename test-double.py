#!/usr/bin/env python3
"""tests for double.py"""
import sys

import os
from subprocess import getoutput

prg = './double.py'

def test_a():
    out = getoutput(f'{prg} "xa aa "')
    expected= 'found double word: "aa"'
    sys.stderr.write("world\n")
    print("Dit gaat naar stdout", file=sys.stdout)
    print("Dit gaat naar stderr", file=sys.stderr)
    assert out.strip() == expected

def test_b():
    out = getoutput(f'{prg} "bb bb "')
    expected= 'found double word: "bb"'
    assert out.strip() == expected
