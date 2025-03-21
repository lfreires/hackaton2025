# Chatbot com FastAPI + Next.js

Este é um projeto de chatbot moderno, com frontend em **Next.js** e backend em **FastAPI**, utilizando **POO, boas práticas de engenharia de software**, e com suporte a múltiplos usuários com login.

---

## Funcionalidades

- Chat em tempo real com histórico
- Frontend 100% React (Next.js)
- Backend FastAPI com SQLite
- Múltiplos usuários com login (username)
- Histórico individual por usuário
- Persistência de mensagens com SQLAlchemy
- Estilo dark, responsivo e moderno

---

## Estrutura de pastas

```
chatbot_project/
│
├── backend/
│   ├── api/             # Endpoints FastAPI
│   ├── database/        # Banco de dados SQLite + SQLAlchemy
│   ├── models/          # Classes POO
│   ├── services/        # Lógica de negócio (ChatService, UserService)
│   └── main.py          # Inicializa FastAPI
│
├── frontend/
│   ├── components/      # Componentes React (ChatBox, Input, Mensagem)
│   ├── models/          # Classe Message (frontend)
│   ├── services/        # Comunicação com a API
│   └── pages/           # Página principal com login e chat
│
└── README.md
```

---

## Tecnologias utilizadas

- **Frontend:** React (Next.js)
- **Backend:** FastAPI
- **Banco de dados:** SQLite + SQLAlchemy
- **Estilo:** CSS inline + framer-motion (animações)
- **API:** REST

---

## Como rodar o projeto localmente

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/chatbot_project.git
cd chatbot_project
```

### 2. Instalar dependências do backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Instalar dependências do frontend

```bash
cd ../frontend
npm install
npm run dev
```

---

## Rotas principais da API

| Método | Rota             | Descrição                            |
|--------|------------------|--------------------------------------|
| POST   | `/users`         | Cria ou recupera um usuário          |
| POST   | `/chat`          | Envia mensagem e recebe resposta     |
| GET    | `/history/{id}`  | Retorna histórico de mensagens       |

---

## Exemplos de uso da API

### Criar/recuperar usuário

```json
POST /users
Body:
{
  "username": "freir"
}
```

### Enviar mensagem

```json
POST /chat
Body:
{
  "sender": "Usuário",
  "text": "Olá!",
  "user_id": 1
}
```

---

## Múltiplos usuários

- O usuário insere um nome ao entrar
- Cada nome tem um `user_id` único no banco
- O histórico de conversa é carregado com base nesse ID

---

## Requisitos para rodar

### `backend/requirements.txt`

```
fastapi
uvicorn
sqlalchemy
pydantic
```

---
