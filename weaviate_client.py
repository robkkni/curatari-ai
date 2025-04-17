import weaviate
import os
from dotenv import load_dotenv

load_dotenv()

client = weaviate.Client("http://localhost:8080")

def store_thought(text: str):
    client.data_object.create({"text": text}, class_name="Thought")

def retrieve_thoughts(query: str):
    return client.query.get("Thought", ["text"]).with_near_text({"concepts": [query]}).with_limit(5).do()
