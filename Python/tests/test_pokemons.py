import requests
import pytest


URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "63964140fef2dbc31e93fab828bbe36b"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = "22742"


def tests_status_code():
    response = requests.get(url=f"{URL}/trainers", params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200


def test_par_of_response():
    response_get = requests.get(url=f"{URL}/trainers", params={"trainer_id": TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == "Александр Ростов-на-Дону"
