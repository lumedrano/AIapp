from fastapi import FastAPI
from model import generated_text, question_answer
import uvicorn

app = FastAPI()


@app.get("/api/model/gpt2")
async def root (user_input):
    response = generated_text(user_input)
    return response

@app.get("/api/model/qa")
async def root (user_input, context):
    response = question_answer(user_input, context)
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)