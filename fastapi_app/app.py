from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
async def hello():
    random_number = random.randint(1, 10000)
    return {"message": "Hello from FastAPI! ->"+ str(random_number)}