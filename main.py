
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

class Item(BaseModel):
    text:str
        
app = FastAPI()
translator_en_to_zh = pipeline("text-generation")

@app.get("/")
def root():
    return {"Hello": "World"}

@app.put("/translator/")
def translator(item: Item):
    return {"translator": translator_en_to_zh(item.text)}
