from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os
import uvicorn
from dotenv import load_dotenv

# Add project root to path so we can import from 'agent'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.emlak_persona import generate_emlak_response
from agent.hotel_persona import generate_hotel_response

# Load env variables
load_dotenv()

app = FastAPI(title="Nexus AI Platform API", version="1.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Models for chat
class ChatRequest(BaseModel):
    user_id: str
    message: str
    model_type: str # e.g. "emlak" or "hotel"

# In-memory chat sessions
chat_sessions = {}

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    user_id = f"{request.user_id}_{request.model_type}"
    user_message = request.message
    model_type = request.model_type
    
    if user_id not in chat_sessions:
        chat_sessions[user_id] = []
        
    chat_history = chat_sessions[user_id]
    
    # Route request to specific agent
    if model_type.lower() == "emlak":
        bot_response = generate_emlak_response(user_message, chat_history)
    elif model_type.lower() == "hotel":
        bot_response = generate_hotel_response(user_message, chat_history)
    else:
        bot_response = "Lütfen geçerli bir asistan türü seçin (Emlak veya Hotel)."
    
    chat_sessions[user_id].append({"role": "user", "content": user_message})
    chat_sessions[user_id].append({"role": "assistant", "content": bot_response})
    
    return {"response": bot_response}

@app.get("/")
def serve_ui():
    html_path = os.path.join(static_dir, "index.html")
    if os.path.exists(html_path):
        return FileResponse(html_path)
    return {"status": "ok", "message": "Nexus AI çalışıyor. Arayüz için /static/index.html dosyası bekleniyor."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
