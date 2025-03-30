from fastapi.testclient import TestClient
from main import app
from models.db import db
from models.models import Sheep

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200

    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_read_all_sheep():
    response = client.get("/sheep/all")

    assert response.status_code == 200

    assert len(response.json()) == len(db.data)

def test_add_sheep():
    new_sheep = {
        "id": 7,
        "name": "Luna",
        "breed": "Suffolk",
        "sex": "ewe"
    }

    response = client.post("/sheep/", json=new_sheep)
    assert response.status_code == 201
    assert response.json() == new_sheep

def test_update_sheep():
    og_sheep = {
        "id": 8,
        "name": "Luna",
        "breed": "Suffolk",
        "sex": "ewe"
    }

    new_sheep = {
        "id": 77,
        "name": "Marco",
        "breed": "kloffuS",
        "sex": "ram"
    }

    response = client.post("/sheep/", json=og_sheep)
    assert response.status_code == 201

    get_update_sheep = client.put("/sheep/8", json=new_sheep)
    assert get_update_sheep.status_code == 200
    assert get_update_sheep.json() == new_sheep

def test_delete_sheep():
    test_sheep = {
        "id": 700,
        "name": "Luna",
        "breed": "Suffolk",
        "sex": "ewe"
    }

    response = client.post("/sheep/", json=test_sheep)
    assert response.status_code == 201

    delete_response = client.delete("/sheep/700")
    assert delete_response.status_code == 200
    assert delete_response.json() == test_sheep
