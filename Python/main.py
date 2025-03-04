import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '63964140fef2dbc31e93fab828bbe36b'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
          
body_create = {
    "name": "Бульбазавр",
    "photo_id": 3
}

body_update = {
    "pokemon_id": "250010",
    "name": "Бульба",
    "photo_id": 5
}

body_catch = {
    "pokemon_id": "250010"
}

response_create = requests.post(url = f'{URL}/pokemons',headers = HEADER, json = body_create)
print(response_create.text)

response_update = requests.put(url = f'{URL}/pokemons',headers = HEADER, json = body_update)
print(response_update.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball',headers = HEADER, json = body_catch)
print(response_catch.text)