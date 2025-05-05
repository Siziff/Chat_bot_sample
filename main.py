from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import ChatRequest, ChatResponse
from character import get_blaze_reply
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Blaze Chat API", version="0.1")
session_history: list[dict] = []
MAX_HISTORY = 10 

# CORS для удобной отладки 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    global session_history

    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    reply = await get_blaze_reply(session_history, request.message)

    session_history.append({"role": "user", "content": request.message})
    session_history.append({"role": "assistant", "content": reply})

    session_history = session_history[-MAX_HISTORY:]

    return ChatResponse(reply=reply)