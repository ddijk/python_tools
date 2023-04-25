import sys
from knwu import login, url

def main():
    if len(sys.argv)<3:
        print("Geef als eerste arg de naam van de renner, en als tweede het oude aantal punten")
        sys.exit()

    naam = sys.argv[1]
    punten = int(sys.argv[2])
    print(f'Kijken of {naam} nog steeds {punten} punten heeft: ', end='')

    huidige_aantal = get_punten(naam)

    print('GEWIJZIGD') if punten != huidige_aantal else print(f'geen update, nog steeds {huidige_aantal}')

def get_punten(naam):
    with open('credentials') as creds:
       session, cookies3, proxy = login(creds) 
    headers = { 'Accept' : 'application/json'}

    klassement_url = 'https://mijn.knwu.nl/api/competitions/55/results?filter[competition]=55&filter[year]=2023&filter[race]=70695&filter[mode]=rank&filter[rank]=General&filter[user.name]=herw&include[0]=user&include[1]=license.organisation&permissions[0]=export&page=1&view=list'
    klassement = session.get(f'{klassement_url}', cookies=cookies3, proxies=proxy, headers=headers)
    renners = klassement.json()
    n = renners['data'][0]['points']
    #print(f'aantal punten {n}')
    return int(n)



if __name__ == '__main__':
    main()