from sqlalchemy.orm import Session
from backend.models.message import ChatMessage, User
from backend.database.schemas import MessageCreate, UserCreate
from datetime import datetime

class ChatService:
    @staticmethod
    def save_message(db: Session, message_data, user_id: int):
        # Gera a resposta do bot
        resposta = f"Você disse: {message_data.text}"
        
        # Cria e salva a mensagem do bot
        bot_msg = ChatMessage(sender="Bot", text=resposta, user_id=user_id)
        db.add(bot_msg)
        db.commit()
        db.refresh(bot_msg)

        return bot_msg
    
    @staticmethod
    def get_messages(db: Session, user_id: int):
        return db.query(ChatMessage).filter(ChatMessage.user_id == user_id).order_by(ChatMessage.timestamp).all()


class UserService:
    @staticmethod
    def get_or_create_user(db: Session, username: str):
        user = db.query(User).filter(User.username == username).first()
        if not user:
            user = User(username=username)
            db.add(user)
            db.commit()
            db.refresh(user)
        return user
