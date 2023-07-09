from fastapi import FastAPI

app = FastAPI()


@app.get("/dan/{text}")
async def readitem(text):
    return {"message": text}
@app.post("/up/{text}")
async def up(text):
    return {"message": text}