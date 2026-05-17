from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'message':"Welcome to FastAI"}

@app.get("/welcome")
def welcome(name: str):
    return{
        "message": f"Welcome to FastAPI Home page {name} !! How is your Preparation going on 🤔🤔😀 "
    }

if __name__ == '__main__':
    uvicorn.run(app, host = '127.0.0.1', port = '8000')

