from fastapi import FastAPI
from model import generated_text, question_answer
import uvicorn

app = FastAPI()


class Response:
    status: int
    message: str
    error: str

@app.get("/health")
async def health():
    return "Gucci"

@app.get("/api/model/gpt2/{search}")
async def root (search):
    r = Response()
    r.message = generated_text(search)
    r.error = []
    r.status = 200
    return r

@app.get("/api/model/qa/{search}/{context}")
async def root (search, context):
    r = Response()
    r.message = question_answer(search, context)
    r.error = []
    r.status = 200
    return r

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)