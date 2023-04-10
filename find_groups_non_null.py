import re
import sys
from collections import Counter

def main():
    if len(sys.argv) < 2:
        filename = 'testfile'
    else:
        filename = sys.argv[1]

    i =0
    print(f'start, using file {filename}')
    for line in getline(filename):
        quantities =  re.findall('DECL_QTY=([-]?\d+\.\d+)', line)
        if ( len(quantities) < 3):
            print('Geen 3 groepen gevonden:')
            print(line)
            break

        c = Counter(quantities)
        if not c['0.0']==2:
            print(f'Raar geval: {line}')
        else:
            i = i+1 
    print(f'end, aantal groepjes van 3: {i}')


def getline(filename):
    with open(filename) as f:
        for line in f:
            yield line

if __name__ == '__main__':
    main()
