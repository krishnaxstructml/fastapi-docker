from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'key' : 'value'}


@app.get('/ping')
def index():
    return {'message' : '200OK'}
