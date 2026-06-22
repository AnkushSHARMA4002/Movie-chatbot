from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client["movie_chatbot"]

collection = db["chat_history"]


def save_message(
    user_id,
    conversation_id,
    role,
    content
):

    result = collection.insert_one(
        {
            "user_id": user_id,
            "conversation_id": conversation_id,
            "role": role,
            "content": content
        }
    )

    print("Inserted:", result.inserted_id)