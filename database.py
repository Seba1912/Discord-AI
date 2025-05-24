# database.py
# Manages interactions with MongoDB Atlas storing data in the cloud.
# This stores most common questions to enhance the interactions speed.

from pymongo import MongoClient
from config import MONGODB_URI
from datetime import datetime

client = MongoClient(MONGODB_URI)
db = client.rok_discord_bot

def log_interaction(user_id, question, answer, rok=False):
    db.logs.insert_one({
        "user_id": user_id,
        "question": question,
        "answer": answer,
        "rok_related": rok,
        "timestamp": datetime.utcnow()
    })

def get_cached_answer(query):
    return db.cache.find_one({"query": query})

def save_cached_answer(query, answer):
    db.cache.insert_one({
        "query": query,
        "answer": answer,
        "timestamp": datetime.utcnow()
    })
