import requests

url = f'https://pokeapi.co/api/v2/pokemon/2'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print ('хп', data['stats'][0]['base_stat'])
    print ('at', data['stats'][1]['base_stat'])
    print ('def', data['stats'][2]['base_stat'])
    print ('sp', data['stats'][5]['base_stat'])
else:
    print("Pikachu")