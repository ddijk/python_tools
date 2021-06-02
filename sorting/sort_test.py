from sort import mysort
from sort import sortOnProp
from sort import sortOnProps

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
    
# multi level sort
def test_multi_level():
     a = [{'id': 1, 'date': 2008}, {'id': 2, 'date': 2008}, {'id': 3, 'date': 2010}, {'id': 4, 'date': 2008}, {'id': 5, 'date': 2005}]

     expected = [{'id': 5, 'date': 2005}, {'id': 1, 'date': 2008}, {'id': 2, 'date': 2008}, {'id': 4, 'date': 2008}, {'id':3, 'date': 2010}]

     assert sortOnProps(a, 'date', 'id') == expected

def test_multi_level_b():
     a = [{'id': 2, 'date': 2008}, {'id': 1, 'date': 2008}, {'id': 4, 'date': 2008}, {'id': 3, 'date': 2010}, {'id': 5, 'date': 2005}]

     expected = [{'id': 5, 'date': 2005}, {'id': 1, 'date': 2008}, {'id': 2, 'date': 2008}, {'id': 4, 'date': 2008}, {'id':3, 'date': 2010}]

     assert sortOnProps(a, 'date', 'id') == expected