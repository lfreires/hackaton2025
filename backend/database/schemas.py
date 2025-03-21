from pydantic import BaseModel
from datetime import datetime

# 📥 Requisição para criar mensagem
class MessageCreate(BaseModel):
    sender: str
    text: str
    user_id: int

# 📤 Resposta de uma mensagem
class MessageResponse(BaseModel):
    id: int
    sender: str
    text: str
    timestamp: datetime

    model_config = {
        "from_attributes": True  # Pydantic v2 (substitui orm_mode)
    }

# 📥 Requisição para criar usuário
class UserCreate(BaseModel):
    username: str

    model_config = {
        "from_attributes": True
    }

# 📤 Resposta do usuário (com ID!)
class UserResponse(BaseModel):
    id: int
    username: str

    model_config = {
        "from_attributes": True
    }
