from fastapi import FastAPI
from pydantic import BaseModel
from app.rag.chain import handle_user_query

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    user_id: str
    conversation_id: str

@app.get("/")
def home():
    return {
        "message": "Movie Chatbot Running"
    }

@app.post("/chat")
def chat(request: QueryRequest):

    response = handle_user_query(
        request.query,
        request.user_id,
        request.conversation_id
    )

    return {
        "response": response
    }