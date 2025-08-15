from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

user_db={
    1:{"name":"Pushkar","age":26},
    2:{"name":"Shubham","age":26},
    3:{"name":"shrikant","age":27},
    4:{"name":"Mahesh","age":28},
    5:{"name":"Vijay","age":14}
}

class ValidateUser(BaseModel):
    name:str
    age:int


@app.post("/update/{user_id}")
def user_update(user_id:int,user:ValidateUser):
    if user_id in user_db:
        user_db[user_id]=user.dict()
        return {"Message":"User updated sucessfully","User":user_db}
    else:
        user_db[user_id]=user.dict()
        return {"Message":"User not found but created new one","User":user_db}
    
@app.delete("/delete/{user_id}")    
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        return {"Message":"User deleted Sucessfully","User":user_db}
    else:
        return {"Message":"User not found"}
