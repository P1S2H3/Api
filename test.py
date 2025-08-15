from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get("/pushkar/shinde")

def add(a:int,b:int):
    return a+b

class Substractmodel(BaseModel):
    a:int
    b:int


def sub(a:int,b:int):
    return a-b

@app.post("/substract")
def substract(model:Substractmodel):
    return sub(model.a,model.b)



print(add(3,4))