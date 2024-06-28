from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def test():
    return {"message": "Hello World"}


@app.get("/chat_complettion/")
async def get_chat_completion():
    return {"message": "Hello World"}


@app.get("/simplification/")
async def get_spimplification():
    return {"message": "Hello World"}
