from enum import Enum
from fastapi import FastAPI

# predefined path parameter values for /models/{model_name}
class ModelName (str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get('/')
async def root():
  return{ "message": "hello" }

@app.get('/items/{item_id}')
async def read_item(item_id: int):
  return { "item_id" : item_id }

@app.get('/users/me')
async def read_user_me():
  return { "user_id": "current user" }

@app.get('/users/{user_id}')
async def read_user(user_id: str):
  return { "user_id": user_id }

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
  if model_name is ModelName.alexnet:
    return { "model_name": model_name}
  
  if model_name is ModelName.resnet:
    return { "model_name": model_name}
  
  return { "model_name" : model_name }