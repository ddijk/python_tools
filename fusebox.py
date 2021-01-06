#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2021-01-05
Purpose: Price checker
"""

import argparse
import requests
import re
import json
from io import StringIO


# --------------------------------------------------
def main():
    response = requests.get('https://www.thenorthface.nl/shop/nl/tnf-nl/base-camp-fuse-box-3kvr', stream=True)
    pattern = r'var itemPrices = ({.*});$'
    n = 0;
    for line in response.iter_lines():
        n += 1
        s = line.decode() 
        f =  s.find('itemPrices')
        if f != -1:
            m =  re.search(pattern, s)
            if m:
                 prices = json.load(StringIO(m.group(1)))
#                 for color in [{"c": "ASPHALT GREY/SUMMIT GOLD", "p": 130},{"c":"TNF BLACK", "p": 104}, {"c":"Wrought Iron-Tnf Black", "p": 130}]:
                 for color in [{"c": "ASPHALT GREY/SUMMIT GOLD", "p": 130},{"c":"TNF BLACK", "p": 104} ]:
                     print('-----------')
                     print(f'kleur: {color["c"]}')
                     handle(prices, color["c"], color["p"])


def handle(prices, color, previousPrice):
     currentPrice = (prices['713173']['pricing']['7000000000000073250'][color]['highPriceNumeric'])
    
     if currentPrice < previousPrice:
         print(f'PRIJS IS GEDAALD: {currentPrice}') 
     if currentPrice == previousPrice:
         print(f'prijs is gelijk: {currentPrice}') 
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
