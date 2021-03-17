from typing import Optional
from datetime import time

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    daet: str
    description: str


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello there!"}

@app.post("/items/")
async def create_item(item: Item):
    return item