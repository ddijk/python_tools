from sort import mysort
from sort import sortOnProp

def test_sort():
     a = ['aap','noo']
     assert a == mysort(a)

def test_sort2():
     a = ['noot','aap']
     assert ['aap','noot'] == mysort(a)


def test_sortDict():
     a = [{'name': 'lieve', 'date': 2008}, {'name': 'dick', 'date': 1973}, {'name':'jens', 'date': 2005}]
     expected = [{'name': 'dick', 'date': 1973}, {'name':'jens', 'date': 2005}, {'name': 'lieve', 'date': 2008}]

     assert sortOnProp(a, myFunc) == expected

def test_sortDictLambda():
     a = [{'name': 'lieve', 'date': 2008}, {'name': 'dick', 'date': 1973}, {'name':'jens', 'date': 2005}]
     expected = [{'name': 'dick', 'date': 1973}, {'name':'jens', 'date': 2005}, {'name': 'lieve', 'date': 2008}]

     assert sortOnProp(a, lambda x: x['date']) == expected

     
def myFunc(e):
    return e['date']
