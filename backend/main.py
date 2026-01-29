# backend/main.py

import os
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from backend.utils import load_pdf_text
from backend.model import generate_text

app = FastAPI()

# Paths
UPLOAD_FOLDER = "data"
DOCUMENT_PATH = os.path.join(UPLOAD_FOLDER, "document.txt")

# Ensure the folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Pydantic model for question endpoint
class QuestionRequest(BaseModel):
    question: str

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file, save it, extract its text, and save as document.txt
    """
    file_path = os.path.join(UPLOAD_FOLDER, "uploaded.pdf")

    # Save the uploaded file
    content = await file.read()
    if not content:
        return {"error": "Empty file received"}
    with open(file_path, "wb") as f:
        f.write(content)

    # Extract text from PDF
    text = load_pdf_text(file_path)
    if not text.strip():
        return {"error": "No text found in PDF"}

    # Save extracted text
    with open(DOCUMENT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    return {"message": f"PDF uploaded successfully to {file_path}"}


@app.post("/summarize")
async def summarize_pdf():
    """
    Summarize the uploaded document
    """
    if not os.path.exists(DOCUMENT_PATH):
        return {"error": "No document found. Upload a PDF first."}

    with open(DOCUMENT_PATH, "r", encoding="utf-8") as f:
        document_text = f.read()

    if not document_text.strip():
        return {"error": "Document is empty"}

    prompt = f"""
Summarize the following document clearly and concisely:

{document_text}
"""
    summary = generate_text(prompt, max_tokens=600)
    return {"summary": summary}


@app.post("/ask")
async def ask_question(request: QuestionRequest):
    """
    Ask a question about the uploaded document
    """
    question = request.question.strip()
    if not question:
        return {"error": "Question cannot be empty"}

    if not os.path.exists(DOCUMENT_PATH):
        return {"error": "No document found. Upload a PDF first."}

    with open(DOCUMENT_PATH, "r", encoding="utf-8") as f:
        document_text = f.read()

    if not document_text.strip():
        return {"error": "Document is empty"}

    prompt = f"""
You are an AI assistant.
Answer the question using ONLY the document below.

Document:
{document_text}

Question:
{question}
"""
    answer = generate_text(prompt, max_tokens=400)
    return {"answer": answer}