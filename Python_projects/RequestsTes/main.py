import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '8875e9e79197eaae92a997b5ac08d7b7'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_pokemon_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_pokemon_name = {
    "pokemon_id": "27235",
    "name": "Вагонг",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_pokemon_catch = {
    "pokemon_id": "27235"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon_create)
print(response_create.text)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon_name)
print(response_name.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon_catch)
print(response_catch.text)