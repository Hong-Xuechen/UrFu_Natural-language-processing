from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

class Item(BaseModel):
    context:str
    question:str
        
app = FastAPI()
nlp = pipeline("question-answering","distilbert-base-cased-distilled-squad")

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/question_answering")
def question_answering(item: Item):
    return {"context": item.context,"question_answering": nlp(question=item.question, context=item.context)}
