#coding=utf-8
#文件名称(File Name)        :main.py
#开发人员(Author)           :洪学辰（Hong Xuechen）
#开发时间(China Date:GMT+8) :2021/12/9 15:20
#开发工具(IDE)              :PyCharm
#联系作者(Contact author)   :hong_xuechen@163.com

#Run the command in the terminal (uvicorn main:app --reload )
# uvicorn main:app --reload   : 打开服务器(Open the server)
# http://127.0.0.1:8000/docs  : 交互式API文档(Interactive API documentation)
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

class Item(BaseModel):
    text:str
        
app = FastAPI()
translator_en_to_zh = pipeline("translation_en_to_zh", "Helsinki-NLP/opus-mt-en-zh")

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/translator/")
def translator(item: Item):
    return {"translator": translator_en_to_zh(item.text)}
