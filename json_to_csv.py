from collections import defaultdict
import pandas as pd
from pathlib import Path
import json
import sys

def convert(filename):
    
    d = defaultdict(list)
    
    with open(filename) as f:
        regels = json.loads(f.read())
    
    for i in regels:
        for k, v in i.items():
            d[k].append(v)
    
    df = pd.DataFrame(d)
    
    output_filename=filename[0:filename.rindex('.')] + '.csv'
    
    df.to_csv(Path(output_filename), index=False)
    print(f'Done. Output file is {output_filename}')

def main():
    if len(sys.argv) < 2:
        print('Geef JSON filenaam als arg')
        return
    else:
        filename = sys.argv[1]

    print(f'Processing {filename}')
    convert(filename)
    

if __name__=='__main__':
    main()
