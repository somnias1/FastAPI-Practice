from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn

import requests

db = []

TIMEZONE_URL = f"http://worldtimeapi.org/api/timezone/"


class City(BaseModel):
    continent: str
    name: str
    timezone: str


app = FastAPI()


@app.get("/cities")
async def get_cities():
    city_list = []
    for city in db:
        req = requests.get(TIMEZONE_URL + city["continent"] + "/" + city["timezone"])
        print(TIMEZONE_URL + city["continent"] + "/" + city["timezone"])
        hora = req.json()["datetime"]
        city_list.append(
            {"name": city["name"], "timezone": city["timezone"], "current_time": hora}
        )
    return city_list


@app.get("/cities/{id}", response_model=City)
async def get_city(id: int):
    city = db[id - 1]
    req = requests.get(TIMEZONE_URL + city["continent"] + "/" + city["timezone"])
    hora = req.json()["datetime"]
    val = {
        "continent": city["continent"],
        "name": city["name"],
        "timezone": city["timezone"],
        "current_time": hora,
    }
    return val


@app.post("/cities/", response_model=City)
async def create_city(city: City):
    name = city.name
    timezone = city.timezone
    continent = city.continent

    db.append(city.dict())
    city = {"name": name, "timezone": timezone, "continent": continent}
    return city


@app.delete("/cities/{id}")
def delete_city(city_id: int):
    db.pop(city_id - 1)
    return {"Exito": "Ciudad eliminada"}


if __name__ == "__main__":
    uvicorn.run("AdvAPI:app")
