#!/usr/bin/env python3
from regex import matchCat
from regex import filterCategory

regex = r'[Nn]ieuweling(en)?'

def testMatch():
    event = createEvent('Nieuwelingen (M)') 
    assert filterCategory(regex, event)

def testMatch2():
    event = createEvent('Nieuwelingen)') 
    assert filterCategory(regex, event)

def testMatch3():
    event = createEvent('Nieuwelingen (M)') 
    assert filterCategory(regex, event)

def testMatch4():
    event = createEvent('Nieuweling (V)') 
    assert filterCategory(regex, event) == False

def testMatch5():
    event = createEvent('Nieuwelingen (M/V)') 
    assert filterCategory(regex, event)

def testMatch6():
    event = createEvent('nieuwelingen)')
    assert filterCategory(regex, event)

def testMatch7():
    event = createEvent('Nieuwelingen (V)')
    assert filterCategory(regex, event) == False

def testMatch8():
    event = createEvent('Nieuweling')
    assert filterCategory(regex, event)

def testMatch9():
    event = createEvent('Nieuwelingen ( V )')
    assert filterCategory(regex, event) == False

def testSkipVrouwenOnlyRace():
    event = createEvents('Nieuwelingen ( V )', 'Nieuwelingen')
    assert filterCategory(regex, event) 
#======================
def createEvent(cat):
    race ={ 'name': cat}
    return { 'races' : [race] }

def createEvents(cat1, cat2):
    race1 ={ 'name': cat1}
    race2 ={ 'name': cat2}
    return { 'races' : [race1, race2] }

