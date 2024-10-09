# PDF Chat API with FastAPI and Gemini

This project implements a simple PDF Chat API using **FastAPI** and **Google Gemini** for handling PDF uploads, processing, and answering questions based on PDF content. The system allows users to upload PDFs, extract their contents, and ask questions related to the uploaded PDF.

## Features

- Upload PDF files and extract text.
- Chunk the extracted text for processing.
- Store the text data in vector form (FAISS).
- Ask questions related to the uploaded PDF content via the Google Gemini - PRO API.

## Endpoints

### 1. Upload and Process PDF
- **Endpoint**: `/v1/pdf`
- **Method**: `POST`
- **Description**: Uploads one or more PDF files, processes them, and extracts their content.
  
### 2. Ask Question
- **Endpoint**: `/ask-question/{pdf_id}`
- **Method**: `POST`
- **Description**: Sends a question about a specific uploaded PDF and returns the answer.


## Setup and Installation

##### 1. Clone the repository:

   ```
   git clone https://github.com/YBSener/pdf-rag-fastapi-example.git
   cd pdf-rag-fastapi-example
   ```
##### 2. Create a virtual environment and activate it:
   ```
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```
##### 3. Install the required packages:
   ```
    pip install -r requirements.txt
   ```
##### 4. Create a `.env` file and add your Google API key:
   ```
    GOOGLE_API_KEY= "your-google-api-key"
   ```
### 5. Running the Application
   ```
    uvicorn main:app --reload
   ```


**Access the API documentation at http://127.0.0.1:8000/docs for Swagger UI.**


# Example Workflow

1. **Upload PDF**: Use the `/v1/pdf` endpoint to upload PDF file. The API will extract text from the PDF and return a `pdf_id` for each uploaded file.

   **Example Response**:

   ```json
   {
     "uploaded_pdfs": [
       {
         "pdf_id": "a2007da8-1a4c-4081-975d-62fe3538c35f",
         "filename": "Yigit_Batuhan_Sener_CV_2024.pdf",
         "page_count": 1,
         "text": "..."
       }
     ]
   }
   ```
In this example, the **pdf_id is "a2007da8-1a4c-4081-975d-62fe3538c35f"**.

2. Ask a Question: Use the /ask-question/{pdf_id} endpoint to ask questions related to the content of the uploaded PDF. Replace {pdf_id} with the pdf_id returned from the upload step.
   
   *Question : Who is he ?*
   
   **Example Response**:

   ```json
    {
      "answer": "Yigit Batuhan Sener is an AI R&D Engineer with over 3 years of industry experience specialized in AI and data analytics solutions."
    }
   ```





   
