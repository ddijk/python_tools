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

# --------------------------------------------------

def main():
    response = requests.get(
        'https://www.thenorthface.nl/shop/nl/tnf-nl/base-camp-fuse-box-3kvr', stream=True)
    price_lines = filter(lambda s: s.find('itemPrices')
                         != -1, map(bytes.decode, response.iter_lines()))

    list(map(checkPrices, map(capturePrices, price_lines)))


def capturePrices(line):
    pattern = r'var itemPrices = ({.*});$'
    return re.search(pattern, line)


def checkPrices(match):
    prices = json.loads(match.group(1))
#                 for color in [{"c": "ASPHALT GREY/SUMMIT GOLD", "p": 130},{"c":"TNF BLACK", "p": 104}, {"c":"Wrought Iron-Tnf Black", "p": 130}]:
    for product in [{"color": "ASPHALT GREY/SUMMIT GOLD", "price": 130}, {"color": "TNF BLACK", "price": 104}]:
        print('-----------')
        print(f'kleur: {product["color"]}')
        currentPrice = prices['713173']['pricing']['7000000000000073250'][product["color"]]['highPriceNumeric']
        if currentPrice < product["price"]:
            print(f'PRIJS IS GEDAALD: {currentPrice}')
        if currentPrice == product["price"]:
            print(f'prijs is gelijk: {currentPrice}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
