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
    response = generated_text(search)
    return response

@app.get("/api/model/qa/{search}/{context}")
async def root (search, context):
    response = question_answer(search, context)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)