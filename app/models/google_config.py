import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

def get_google_embeddings():
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key is None:
        raise ValueError("Google API key not found in environment variables")
    
    return GoogleGenerativeAIEmbeddings(model="models/embedding-001")
