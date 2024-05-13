import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '8875e9e79197eaae92a997b5ac08d7b7'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4039'

def test_status_code():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_get.status_code == 200

def test_response_name():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == 'Nikita'