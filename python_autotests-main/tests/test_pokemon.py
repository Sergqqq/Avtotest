import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = "387293567066abdac4f08281d8e46220"
HEADERS = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = 4489

def test_status_code_trainers():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRAINER_ID} ) 
    assert response.status_code  == 200

def test_status_code_trainers_myid():
    response_id = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRAINER_ID} ) 
    assert response_id.json()['data'][0]['id'] == '4489'