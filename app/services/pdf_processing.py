from PyPDF2 import PdfReader
import uuid
import logging

logger = logging.getLogger(__name__)

async def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf.file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

async def process_pdf(pdf_docs):
    pdf_data = []
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf.file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            pdf_id = str(uuid.uuid4())

            metadata = {
                "pdf_id": pdf_id,
                "filename": pdf.filename,
                "page_count": len(pdf_reader.pages),
                "text": text
            }
            pdf_data.append(metadata)
            logger.info(f"PDF '{pdf.filename}' successfully processed.")
        except Exception as e:
            logger.error(f"PDF processed error: {str(e)}")
            raise

    return pdf_data

def get_text_chunks(text):
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks
