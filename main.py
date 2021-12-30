from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

class Item(BaseModel):
    question:str
        
app = FastAPI()
nlp = pipeline("question-answering","distilbert-base-cased-distilled-squad")

context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question.
"""

@app.get("/")
def root():
    return {"Hello": "World"}

@app.put("/question_answering")
def question_answering(item: Item):
    return {"question_answering": nlp(question=item.question, context=context)}
