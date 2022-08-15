import requests

def abil(poke):
    for i in poke['abilities']:
        print(i['ability']['name'])

def main():
    global pokemon
    pokemon = str(input('Pokemon: '))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res=requests.get(api)
    poke=res.json()
    abil(poke)

if __name__ == '__main__':
    main()