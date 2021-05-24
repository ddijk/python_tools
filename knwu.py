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

    parser.add_argument( 'file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

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
    # pos_arg = args.positional

    credentials=readCredentials(file_arg)

    print('username is missing') if not credentials['username'] else print('username found')
    print('password is missing') if not credentials['password'] else print('password found')

    if not credentials['username'] or not credentials['password']:
        print('username or password missing')
        return
    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    # print(f'positional = "{pos_arg}"')

    url = 'https://mijn.knwu.nl'

    
    proxy = { "https": "https://localhost:1080"} if flag_arg else None

    print(f'using proxy {proxy}')
    session = requests.Session()
    # response = session.get(f'{url}', proxies=proxy, verify=False)

    # print(f'response on first get: {response.status_code}')

    # 'XSRF-TOKEN' and 'mijnknwu_session'
    # cookies = session.cookies.get_dict()

    # print(f'cookies van get: {cookies}')

    response1b = session.get(f'{url}/login', proxies=proxy, verify=False)
    print(f'response on get login {response1b.status_code}')
    cookies1b = session.cookies.get_dict()
    print(f'cookies van get login: {cookies1b}')

    # get token in HTML response

    token = findToken(response1b)

    print(f'token is {token}')

    data = {'username': credentials['username'], 'password': credentials['password'], '_token': token }
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Cache-Control': 'no-cache', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15'}
    response2 = session.post(f'{url}/login', data=data, cookies=cookies1b, headers=headers, proxies=proxy, verify=False, allow_redirects=False)


    cookies2 = session.cookies.get_dict()
    # print(f'response on post {response2.status_code}')
    # print(f'response on post {response2.reason}')
    # print(f'cookies van post: {cookies2}')
    # print(f'cookies van post: {requests.Response().cookies.get_dict()}')

    response3 = session.get(f'{url}', cookies=cookies2, verify=False, proxies=proxy)

    cookies3 = session.cookies.get_dict()
    print(f'response on redirect {response3.status_code}')
    print(f'response on redirect {response3.reason}')
    print(f'cookies van redirect: {cookies3}')

    headers2 = { 'Accept' : 'application/json'}
    responseEvents = session.get(f'{url}/api/events', cookies=cookies3, proxies=proxy, headers=headers2)

    print(f'events response status {responseEvents.status_code}')

    # print(f'{responseEvents.json()}')
    events = responseEvents.json()
    # print(f'events response {events.meta}')
    print(f'events response {events}')
    print(f'events response {events["meta"]}')

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
