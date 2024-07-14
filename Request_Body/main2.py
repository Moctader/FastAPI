from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
app = FastAPI()

items_storage = {}


@app.post("/items/")    
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    items_storage[item.name] = item_dict
    return item_dict

@app.get("/items/")
async def get_item(name: str):
    return items_storage.get(name, {"message": f"Item '{name}' not found"})

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
