from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão com banco SQLite local
DATABASE_URL = "sqlite:///./chat_history.db"

# Cria a engine do banco e configura sessão
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

# Base para os modelos do SQLAlchemy
Base = declarative_base()

# Cria as tabelas com base nos modelos definidos
def create_db():
    from backend.models.message import ChatMessage, User
    Base.metadata.create_all(bind=engine)
