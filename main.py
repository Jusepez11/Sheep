from typing import Dict

from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep

app = FastAPI()


@app.get("/sheep/all", response_model=Dict[int, Sheep])
def read_all_sheep():
    return db.get_all_sheep()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    return db.get_sheep(id)

@app.put("/sheep/{id}", response_model=Sheep)
def update_sheep(id: int, sheep: Sheep):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep with this ID does not exists")
    db.data[id] = sheep
    return db.get_sheep(id)

@app.delete("/sheep/{id}", response_model=Sheep)
def delete_sheep(id: int):
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep with this ID does not exists")
    deleted = db.get_sheep(id)
    del db.data[id]
    return deleted

@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    db.data[sheep.id] = sheep
    return sheep