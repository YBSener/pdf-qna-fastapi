from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.pdf_processing import process_pdf, get_text_chunks
from app.services.vector_db import get_vector_store
from app.services.gemini_chain import answer_question
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

pdf_router = APIRouter()

pdf_store = {}

@pdf_router.post("/v1/pdf")
async def upload_and_process_pdf(files: list[UploadFile] = File(...)):
    for file in files:
        if not file.filename.endswith(".pdf"):
            logger.warning(f"Invalid file type: {file.filename}")
            raise HTTPException(status_code=400, detail="Invalid file type")

    try:
        pdf_metadata = await process_pdf(files)

        combined_text = " ".join([pdf['text'] for pdf in pdf_metadata])

        pdf_id = pdf_metadata[0]['pdf_id']

        if pdf_id not in pdf_store:
            pdf_store[pdf_id] = {
                "metadata": pdf_metadata[0],  
                "text": combined_text
            }

        logger.info(f"PDF '{pdf_metadata[0]['filename']}' successfully processed and saved. PDF ID: {pdf_id}")
        return {"uploaded_pdfs": [pdf_metadata[0]]}  
    
    except Exception as e:
        logger.error(f"PDF processed error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An error occurred during PDF processing: {str(e)}")

@pdf_router.post("/ask-question/{pdf_id}")
async def ask_question(pdf_id: str, question: str = Form(...)):
    if not question.strip():  
        logger.warning("Empty question.")
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    if pdf_id not in pdf_store:
        raise HTTPException(status_code=404, detail="PDF not found")

    try:
        pdf_data = pdf_store[pdf_id]
        combined_text = pdf_data["text"]

        response = await answer_question(question)
        
        logger.info(f"Question processed successfully: {question}")
        return {"answer": response}
    
    except Exception as e:
        logger.error(f"Question processing error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Question processing error: {str(e)}")
