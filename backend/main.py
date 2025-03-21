from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.endpoints import router
from backend.database.db import create_db

# 🚀 Criação do app FastAPI
app = FastAPI()

# ✅ Middleware de CORS — IMPORTANTE: isso vem logo após o app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ liberar tudo para testar
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Inclui todas as rotas da API
app.include_router(router)

# ✅ Cria o banco ao iniciar
@app.on_event("startup")
def startup():
    create_db()
