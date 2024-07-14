from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/")
async def get_item(name: str, description: str, price: float, tax: float = None):
    return {"name": name, "description": description, "price": price, "tax": tax}