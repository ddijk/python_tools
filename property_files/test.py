#!/usr/bin/env python3

import os
import random
from subprocess import getoutput
import copy
import json
from props import escape_dollar

prg = './props.py'

def test_properties_1():
    """simple property file"""

    out = getoutput(f'{prg} -f input1').splitlines()
    assert out[0] == "{'key': 'val', 'key2': 'val', 'key3': 'val'}"

# --------------------------------------------------
def test_properties_2():
    """simple property file"""

    out = getoutput(f'{prg} -f input2').splitlines()
    assert out[0] == "{'key': 'val', 'key3': 'val', 'key2': 'val'}"

# --------------------------------------------------
def test_properties_3():
    """simple property file"""

    out = getoutput(f'{prg} -f input2').splitlines()

    actual = ''.join(map(convertQuotes, out[0]))

    assert json.loads(actual)== {'key': 'val', 'key3': 'val', 'key2': 'val'}


def test_dict_order_relevancy():
    assert {'a':'a1','b':'b1','c':'c1'} == {'b':'b1','a':'a1','c':'c1'}

def test_deepcopy():
    d1 = {'a':'a1'}
    d2 = copy.deepcopy(d1)
    d1['a']='a2'
    print(d1)
    print(d2)
    assert d1 != d2

def test_dollar():
    assert 'a\\$b' == escape_dollar('a$b')

def convertQuotes(c):
    if c == '"':
        return "'" 

    if c == "'":
       return '"' 

    return c