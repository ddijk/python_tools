from collections import defaultdict
def mysort(coll):
    coll.sort()
    return coll

def sortOnProp(coll, myFunc):
    coll.sort(key=myFunc)
    return coll

def sortOnProps(coll, primaryProp, secondaryProp):

    groups=defaultdict(list)

    for i in coll:
        groups[i[primaryProp]].append(i)

    result = []
    myFunc = lambda x: x[secondaryProp]
    for k in sorted(groups):
        coll = groups[k]
        coll.sort(key=myFunc)
        result.extend(coll)

    return result

