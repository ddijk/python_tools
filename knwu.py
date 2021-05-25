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

    parser.add_argument( '-f', '--file',
                        help='A file with credentials to login to the site',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='credentials')

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag to enable debug logging',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.file
    debug_flag = args.on

    credentials=readCredentials(file_arg)

    if not credentials['username']:
        print('username is missing') 
    if not credentials['password']:
        print('password is missing') 

    if not credentials['username'] or not credentials['password']:
        print('username or password missing')
        return

    if debug_flag:
        print('using credentials file = "{}"'.format(file_arg.name if file_arg else ''))
        print(f'debug flag = "{debug_flag}"')

    url = 'https://mijn.knwu.nl'

    
    proxy = { "https": "https://localhost:1080"} if debug_flag else None
    verify = False if debug_flag else True

    print(f'using proxy {proxy}')
    session = requests.Session()

    response1b = session.get(f'{url}/login', proxies=proxy, verify=verify)
    if debug_flag:
        print(f'response on get login {response1b.status_code}')
    cookies1b = session.cookies.get_dict()
    if debug_flag:
       print(f'cookies van get login: {cookies1b}')

    # get token in HTML response

    token = findToken(response1b)

    if debug_flag:
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
    if debug_flag:
        print(f'response on redirect {response3.status_code}')
        print(f'response on redirect {response3.reason}')
        print(f'cookies van redirect: {cookies3}')

    headers2 = { 'Accept' : 'application/json'}
    responseEvents = session.get(f'{url}/api/events?view=list&page=1&filter[discipline]=&filter[location]=&filter[type]=&filter[region]=&filter[state]=&filter[gender]=&filter[role]=&include[1]=organisation&include[2]=races.classification', cookies=cookies3, proxies=proxy, headers=headers2)

    if debug_flag:
        print(f'events response status {responseEvents.status_code}')
        print(f'events response message {responseEvents.reason}')

    events = responseEvents.json()
    total_number_races= events["meta"]["total"]
    per_page = events["meta"]["per_page"]

    nieuwelingenRaces = []
    
    nieuwelingenRaces.extend(filterRaces(r'[Nn]ieuweling.*\(M\)', events["data"]))
    if debug_flag:
        [print(f'naam={r["name"]}') for r in nieuwelingenRaces]
        print(f'==============={len(nieuwelingenRaces)}')

    # first page already retrieved, so start at index '1'
    num_pages = math.ceil(total_number_races/per_page)
    for i in range(1, num_pages):
    # for i in range(1, 3):
        # pages start at index 1:
        next_page = i+1
        print(f"page {next_page}", end='\r' if i<num_pages-1 else '\n')
        responseEvents = session.get(f'{url}/api/events?view=list&page={next_page}&filter[discipline]=&filter[location]=&filter[type]=&filter[region]=&filter[state]=&filter[gender]=&filter[role]=&include[1]=organisation&include[2]=races.classification', cookies=cookies3, proxies=proxy, headers=headers2)
        events = responseEvents.json()
        nieuwelingenRaces.extend(filterRaces(r'[Nn]ieuweling.*\(M\)', events["data"]))
        if debug_flag:
            [print(f'naam={r["name"]} id={r["id"]}') for r in nieuwelingenRaces]
            print(f'==============={len(nieuwelingenRaces)}')

    out_fh = open('out.txt', 'wt')

    # to filter out duplicates. Het bleek dat sommige races op 2 pagina's terugkwamen
    processed_race_names=[]
    for i in nieuwelingenRaces:
        race_name = i["name"]
        if race_name in processed_race_names:
            print(f'already processed {race_name}')
            continue
        processed_race_names.append(race_name)
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
