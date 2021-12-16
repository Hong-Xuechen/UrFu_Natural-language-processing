
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

class Item(BaseModel):
    text:str
        
app = FastAPI()
translator_en_to_zh = pipeline("translation_en_to_zh")

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/translator/")
def translator(item: Item):
    return {"translator": translator_en_to_zh(item.text)}
