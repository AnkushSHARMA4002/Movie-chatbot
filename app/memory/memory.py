from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

client = MongoClient(
    os.getenv("MONGO_URI")
)

db = client["movie_chatbot"]

chat_collection = db["chat_history"]


def save_message(
        user_id: str,
        conversation_id: str,
        role: str,
        content: str
):

    chat_collection.insert_one(
        {
            "user_id": user_id,
            "conversation_id": conversation_id,
            "role": role,
            "content": content,
            "timestamp": datetime.utcnow()
        }
    )


def get_recent_messages(
        conversation_id: str,
        limit: int = 10
):

    messages = list(
        chat_collection.find(
            {
                "conversation_id": conversation_id
            }
        ).sort(
            "timestamp",
            -1
        ).limit(limit)
    )

    messages.reverse()

    return messages


def get_first_question(
        conversation_id: str
):

    msg = chat_collection.find_one(
        {
            "conversation_id": conversation_id,
            "role": "user"
        },
        sort=[("timestamp", 1)]
    )

    if msg:
        return msg["content"]

    return None