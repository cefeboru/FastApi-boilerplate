import os
from fastapi import FastAPI
import ptvsd

"""
Enable remote debugging
"""
if os.environ['ENVIRONMENT'] != 'PROD':
  ptvsd.enable_attach()

app = FastAPI()


@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
  return {"item_id": item_id, "q": q}