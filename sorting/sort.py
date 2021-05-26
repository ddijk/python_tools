
def mysort(coll):
    coll.sort()
    return coll

def sortOnProp(coll, myFunc):
    coll.sort(key=myFunc)
    return coll

