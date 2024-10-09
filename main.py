import logging
from fastapi import FastAPI
from app.api.pdf_chat import pdf_router



app = FastAPI(title="PDF Chat API using Gemini")

app.include_router(pdf_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the PDF Chat API using Gemini!"}
