# 📄 PDF Chatbot

An AI-powered PDF chatbot built with **FastAPI**, **LangChain**, **ChromaDB**, and **Google Gemini**. Upload a PDF and ask natural language questions about its contents using Retrieval-Augmented Generation (RAG).

---

## ✨ Features

* 📄 Upload PDF documents
* ✂️ Automatic document chunking
* 🧠 Semantic search using ChromaDB
* 🤖 AI-powered question answering with Google Gemini
* 🔍 Retrieval-Augmented Generation (RAG)
* 💬 Clean chat interface built with HTML and Tailwind CSS
* 📚 Persistent vector database for uploaded documents

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Google Gemini

### Frontend

* HTML
* Tailwind CSS
* Jinja2 Templates

---

## 📁 Project Structure

```text
PDF-Chatbot/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── db/
│   └── main.py
│
├── frontend/
│   ├── templates/
│   ├── static/
│   └── uploads/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/PDF-Chatbot.git
cd PDF-Chatbot
cd .\backend\
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

```env
HUGGINGFACE_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your HUGGINGFACE API key.

---

### 5. Run the application

```bash
uvicorn backend.main:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

---

## 📖 How It Works

1. Upload a PDF document.
2. The PDF is loaded and split into chunks.
3. Chunks are converted into vector embeddings.
4. Embeddings are stored in ChromaDB.
5. When you ask a question:

   * Relevant chunks are retrieved.
   * The retrieved context is sent to Gemini.
   * The AI generates an answer based only on the retrieved context.

---

## 📌 Current Features

* PDF upload
* Vector database creation
* Semantic retrieval
* Question answering
* Chat interface
* Persistent storage

---

## 🚧 Planned Improvements

* Streaming AI responses
* Source citations
* Multi-PDF support
* Chat history persistence
* PostgreSQL integration
* User authentication
* Conversation memory
* Hybrid Search (BM25 + Vector Search)
* Reranking
* Docker support
* Cloud deployment

---

## 🤝 Contributing

Contributions are welcome. Feel free to open an issue or submit a pull request.

---

## 👨‍💻 Author

**Sourav Das**

If you found this project useful, consider giving it a ⭐ on GitHub.
