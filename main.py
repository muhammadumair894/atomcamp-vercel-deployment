from time import time
from fastapi import FastAPI, __version__

app = FastAPI()

@app.get("/")
async def root():
    return "Welcome to our Vercel Deployment"
    
@app.get("/atomcamp")
async def atomcamp():
    return "Hello this is our experiment endpoint"

@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}
