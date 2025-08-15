from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
app=FastAPI()

class Calculator(BaseModel):
    a:int
    b:int
    operation: Literal["add", "sub","div","mul"] 

p
    

def calculator(a,b,operation):
    if operation=="mul":
        return a*b
    elif operation=="div":
        if b==0:
            return {"error":"number can not be devide by zero"}
        else:
            return a/b
    elif operation=="add":
        return a+b
    elif operation=="sub":
        return a-b
    else:
        return {"error":"invalid operation"}
    

@app.post("/calculator")
def validcalculator(model:Calculator):
    
    return calculator(model.a,model.b,model.operation)