import sys
from knwu import login 

def main():
    if len(sys.argv)<2:
        print("Geef als de naam van de renner als argument")
        sys.exit()

    naam = sys.argv[1]

    get_punten(naam)


def get_punten(naam):
    with open('credentials') as creds:
       session, cookies3, proxy = login(creds) 
    headers = { 'Accept' : 'application/json'}

    klassement_url = f'https://mijn.knwu.nl/api/competitions/55/results?filter[competition]=55&filter[year]=2023&filter[race]=70695&filter[mode]=rank&filter[rank]=General&filter[user.name]={naam}&include[0]=user&include[1]=license.organisation&permissions[0]=export&page=1&view=list'
    klassement = session.get(f'{klassement_url}', cookies=cookies3, proxies=proxy, headers=headers)
    renners = klassement.json()
    if not len(renners['data']):
        print(f'{naam} is niet bekend')
    else:
        if len(renners['data'])>1: 
            print('Meerdere renners gevonden:')
        for r in renners['data']:
            print(f"renner {r['user']['name']} heeft {r['points']} punten")



if __name__ == '__main__':
    main()