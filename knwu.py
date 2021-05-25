#!/usr/bin/env python3
"""
Author : dickdijk <dickdijk@localhost>
Date   : 2021-05-24
Purpose: Rock the Casbah
"""

import argparse
import requests
from requests.models import Response
import re
import math
import json
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # parser.add_argument('positional',
    #                     metavar='str',
    #                     help='A positional argument')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument( '-f', '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='credentials')

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on

    credentials=readCredentials(file_arg)

    if not credentials['username']:
        print('username is missing') 
    if not credentials['password']:
        print('password is missing') 

    if not credentials['username'] or not credentials['password']:
        print('username or password missing')
        return

    if flag_arg:
        print(f'str_arg = "{str_arg}"')
        print(f'int_arg = "{int_arg}"')
        print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
        print(f'flag_arg = "{flag_arg}"')

    url = 'https://mijn.knwu.nl'

    
    proxy = { "https": "https://localhost:1080"} if flag_arg else None
    verify = False if flag_arg else True

    print(f'using proxy {proxy}')
    session = requests.Session()

    response1b = session.get(f'{url}/login', proxies=proxy, verify=verify)
    if flag_arg:
        print(f'response on get login {response1b.status_code}')
    cookies1b = session.cookies.get_dict()
    if flag_arg:
       print(f'cookies van get login: {cookies1b}')

    # get token in HTML response

    token = findToken(response1b)

    if flag_arg:
        print(f'token is {token}')

    data = {'username': credentials['username'], 'password': credentials['password'], '_token': token }
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Cache-Control': 'no-cache', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15'}
    response2 = session.post(f'{url}/login', data=data, cookies=cookies1b, headers=headers, proxies=proxy, verify=verify, allow_redirects=False)

    cookies2 = session.cookies.get_dict()
    if response2.status_code != 302:
        print(f'Login failed: {response2.reason}')
        return

    response3 = session.get(f'{url}', cookies=cookies2, verify=verify, proxies=proxy)

    cookies3 = session.cookies.get_dict()
    if flag_arg:
        print(f'response on redirect {response3.status_code}')
        print(f'response on redirect {response3.reason}')
        print(f'cookies van redirect: {cookies3}')

    headers2 = { 'Accept' : 'application/json'}
    responseEvents = session.get(f'{url}/api/events?page=1&filter[discipline]=&filter[location]=&filter[type]=&filter[region]=&filter[state]=&filter[gender]=&filter[role]=&include[1]=organisation&include[2]=races.classification', cookies=cookies3, proxies=proxy, headers=headers2)

    if flag_arg:
        print(f'events response status {responseEvents.status_code}')
        print(f'events response message {responseEvents.reason}')

    events = responseEvents.json()
    total_number_races= events["meta"]["total"]
    per_page = events["meta"]["per_page"]

    nieuwelingenRaces = []
    
    nieuwelingenRaces.extend(filterRaces(r'[Nn]ieuweling.*\(M\)', events["data"]))
    [print(f'naam={r["name"]}') for r in nieuwelingenRaces]
    print(f'==============={len(nieuwelingenRaces)}')

    # first page already retrieved, so start at index '1'
    num_pages = math.ceil(total_number_races/per_page)
    for i in range(1, num_pages):
    # for i in range(1, 3):
        # pages start at index 1:
        next_page = i+1
        print(f"page {next_page}", end='\r' if i<num_pages-1 else '\n')
        responseEvents = session.get(f'{url}/api/events?page={next_page}&filter[discipline]=&filter[location]=&filter[type]=&filter[region]=&filter[state]=&filter[gender]=&filter[role]=&include[1]=organisation&include[2]=races.classification', cookies=cookies3, proxies=proxy, headers=headers2)
        events = responseEvents.json()
        nieuwelingenRaces.extend(filterRaces(r'[Nn]ieuweling.*\(M\)', events["data"]))
        [print(f'naam={r["name"]}') for r in nieuwelingenRaces]
        print(f'==============={len(nieuwelingenRaces)}')

    out_fh = open('out.txt', 'wt')
    for i in nieuwelingenRaces:
        datum = i["date"][0]
        out_fh.write(f'{i["name"]} op {datum} \n')
        print(f'{i["name"]} op {datum}')

    out_fh.close()


def filterRaces(catRegex, data):
    # filter out races for Nieuwelingen and that are 'scheduled' (='Definitief'):
    return  filter(lambda e: e['state'] == 'scheduled', filter(lambda x: filterCategory(catRegex, x), data))

def filterCategory(catRegex, e):
    if not 'races' in e:
        print(f'{e["name"]} bevat geen races')
        return False

    for cat_name in map(lambda y: y['name'], e['races']):
        if re.search(catRegex,cat_name):
            return True 

    return False

def findToken(response):
    tokenLine = filter(lambda s: s.find('_token')
                         != -1, map(bytes.decode, response.iter_lines()))

    tok = list(tokenLine)[0]
    m=re.match('.*value="(.+)["]', tok)

    return m.group(1)


def readCredentials(file):
    credentials = {}
    for line in file:

        items = line.rstrip().split('=')
        credentials[items[0]] = items[1]
    
    return credentials


# --------------------------------------------------
if __name__ == '__main__':
    main()
