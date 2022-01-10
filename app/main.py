import pandas as pd

from typing import Optional
from datetime import time

from fastapi import FastAPI
from pydantic import BaseModel


from google.cloud import bigquery

client = bigquery.Client()


class Item(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello there!"}


@app.post("/postit")
async def add_post(item: Item):
    post = {"text": item.text}
    post = pd.DataFrame(post, index=[0])
    post.to_gbq("posts.post-1", if_exists="append")


@app.get("/parseit")
async def create_doc():
    query = "SELECT * FROM `blog-336513.posts.post-1`"
    return client.query(query).result().to_dataframe()
