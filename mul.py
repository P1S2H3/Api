from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()


def mul(a,b):
    return a*b

class Multiplication(BaseModel):
     a:int
     b:int
@app.post("/multiplication")
def validatemul(model:Multiplication):
     return mul(model.a,model.b)

