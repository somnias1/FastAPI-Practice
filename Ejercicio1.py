from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn

db = []


class City(BaseModel):
    name: str
    timezone: str


app = FastAPI()


@app.get("/cities")
async def get_cities():
    return db


@app.post("/cities/", response_model=City)
async def create_city(newcity: City):
    name = newcity.name
    timezone = newcity.timezone

    db.append(newcity.dict())
    city = {"name": name, "timezone": timezone}
    return city


if __name__ == "__main__":
    uvicorn.run("Ejercicio1:app")
