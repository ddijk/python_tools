#!/usr/bin/env python3
"""tests for gitlog.py"""

import os
from subprocess import getoutput

prg = './riedl.py'

pattern = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]'
def test_a():
    text = '12:34'
    out = getoutput(f'{prg} "{pattern}" "{text}"')
    # print(out)
    expected='12:34'
    assert out.strip() == expected

def test_b():
    text = '09:34'
    out = getoutput(f'{prg} "{pattern}" "{text}"')
    # print(out)
    expected='09:34'
    assert out.strip() == expected

def test_c():
    text = '9:34'
    out = getoutput(f'{prg} "{pattern}" "{text}"')
    # print(out)
    expected='9:34'
    assert out.strip() == expected


def test_invalid_input():
    text = '29:34'
    out = getoutput(f'{prg} "{pattern}" "{text}"')
    expected='no match'
    assert out.strip() == expected