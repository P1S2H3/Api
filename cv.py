from fastapi import FastAPI
from pydantic import BaseModel,EmailStr
app=FastAPI()
class VlaidateUserDetails(BaseModel):
    user_name:str
    user_email:EmailStr  
    user_password:str
def password(user_password):
    if len(user_password)<8:
        return 
    else:
        return True

def validate_user(user_name,user_email,user_password):
    if len(user_password)<8:
        return {"Error":"Enter valid passowrd whose len is greater than 8"}
    else:
        return True

@app.post("/validate")
def call_validation(model:VlaidateUserDetails):
    return validate_user(model.user_name,model.user_email,model.user_password)