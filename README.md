# Qwen3 PDF Assistant

A **FastAPI + Streamlit** application that allows users to **upload PDF documents** and either **summarize** them or **ask questions** about their content using the **Qwen3 language model**.

---

## Features

- Upload a PDF and extract its text automatically.
- Summarize the uploaded PDF clearly and concisely.
- Ask questions about the PDF and get answers based solely on the document content.
- Lightweight, locally runnable, and fully portfolio-ready.

---

## Project Structure

```

Qwen3-PDF-Assistant/
├── backend/
│   ├── main.py       # FastAPI backend
│   ├── model.py      # Qwen3 model loading and text generation
│   ├── utils.py      # PDF text extraction
├── frontend.py       # Streamlit frontend
├── requirements.txt  # Python dependencies
├── README.md

````

---

## Requirements

- Python 3.11+
- `requirements.txt` contains all dependencies:
  - FastAPI, Uvicorn
  - Streamlit
  - PyTorch
  - Transformers
  - PyPDF2
  - Requests

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/AlinaMuradyan/Qwen3-PDF-Assistant.git
cd Qwen3-PDF-Assistant
````

2. **Create a virtual environment and activate it:**

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

3. **Install dependencies from `requirements.txt`:**

```bash
pip install -r requirements.txt
```

* This will install all necessary packages including FastAPI, Streamlit, PyTorch, Transformers, PyPDF2, and Requests.

---

## How to Run

### 1. Start the backend

```bash
uvicorn backend.main:app --reload --workers 1
```

* The backend will run on: `http://127.0.0.1:8000`
* Handles PDF upload, text extraction, summarization, and Q&A.

### 2. Start the frontend

```bash
streamlit run frontend/frontend.py
```

* Streamlit will open a browser window where you can interact with the app.
* Upload your PDF, then choose **Summarize** or **Ask Question**.

---

## How It Works

1. **Upload PDF**

   * The PDF is saved in the `data/` folder.
   * Text is extracted and stored in `document.txt`.

2. **Summarize PDF**

   * Sends the extracted text to the Qwen3 model.
   * Returns a concise summary.

3. **Ask Question**

   * Sends the question and the document text to Qwen3.
   * Returns an answer based **only on the PDF content**.

---

## Notes

* The `data/` folder is ignored in Git to avoid pushing large PDFs.
* Make sure your system has enough RAM to load the Qwen3 model locally.

  * For lower-memory setups, consider using a smaller Qwen model.
* Streamlit ↔ FastAPI communication uses proper `multipart/form-data` to ensure uploaded PDFs are received correctly.

---

## License

This project has educational purpose.

---

## Author

**Alina Muradyan**
[GitHub](https://github.com/AlinaMuradyan)
