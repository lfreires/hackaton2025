from fastapi import APIRouter, Depends
from pydantic import BaseModel
from backend.services.chat_service import ChatService, UserService
from backend.database.db import SessionLocal
from backend.models.message import ChatMessage, User
from backend.database.schemas import MessageCreate, UserCreate, UserResponse
from typing import List

router = APIRouter()

# 📦 Dependência de banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 📥 Schema interno da requisição ao /chat
class ChatRequest(BaseModel):
    message: str
    user_id: int

# 📤 Resposta da API /chat
class ChatResponse(BaseModel):
    sender: str
    text: str

# ✅ Endpoint: criar ou buscar usuário
@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db=Depends(get_db)):
    return UserService.get_or_create_user(db, user.username)

# ✅ Endpoint: enviar mensagem
@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: MessageCreate, db=Depends(get_db)):
    print("Recebido:", request)

    # Salva a mensagem do usuário
    user_msg = ChatMessage(sender=request.sender, text=request.text, user_id=request.user_id)
    db.add(user_msg)
    db.commit()

    # Gera e salva a resposta do bot
    bot_msg = ChatService.save_message(db, request, request.user_id)

    return ChatResponse(sender=bot_msg.sender, text=bot_msg.text)

# ✅ Endpoint: histórico por usuário
@router.get("/history/{user_id}", response_model=List[ChatResponse])
def get_chat_history(user_id: int, db=Depends(get_db)):
    try:
        print(f"🔍 Buscando histórico do usuário ID {user_id}")
        messages = ChatService.get_messages(db, user_id)
        print(f"📦 Mensagens encontradas: {len(messages)}")
        return [{"sender": msg.sender, "text": msg.text} for msg in messages]
    except Exception as e:
        print("❌ ERRO NO HISTORY:", e)
        raise e

