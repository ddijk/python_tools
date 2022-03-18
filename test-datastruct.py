
def test_add_default():
    expected = { 'noot': { 't1','t2','t3'},  'vuur': { 't1','t2'}} 
    assert convert([{'naam' : 'noot', 'type': 't1'}, {'naam': 'noot', 'type': 't2'}, {'naam': 'vuur', 'type': 't1'}, {'naam': 'vuur', 'type': 't2'}, {'naam': 'noot', 'type': 't1'}, {'naam': 'noot', 'type': 't3'}]) == expected 


def convert(d):
    result = {}
    for i in d:
        result.setdefault(i['naam'], set()).add(i['type']) 
        print('result',result)
    return result
