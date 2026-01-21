from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.inference.chat import Chatbot

app = FastAPI(title="Custom AI Chatbot API")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

chatbot = Chatbot()

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = chatbot.generate_response(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Custom AI Chatbot API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
