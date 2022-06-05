from fastapi import FastAPI
import uvicorn #ASGI

app = FastAPI()

# index or root path -- important -- homepage basically -- automatically opens up
@app.get('/')
def index():
    return {'message':'Welcome'}

# another functionality - Welcome page
@app.get('/Welcome')
def get_name(name:str):
    return {'message' : 'Welcome ' + name}



