from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import shutil
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


embedding = None

def get_embedding():
    global embedding
    if embedding is None:
        embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding

def savefile(file):
    path=os.path.join(r"E:\pdf chatbot\PDF-Chatbot\frontend\uploads",file.filename)
    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return path

def load_split(path):
    docs=PyPDFLoader(path)
    docs=docs.load()
    spliter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=150
    )
    chunks=spliter.split_documents(docs)
    os.remove(path)
    return chunks

def vector_store(chunks, collection_id):
    store = Chroma.from_documents(
        documents=chunks,
        embedding=get_embedding(),
        collection_name=collection_id,
        persist_directory=r"E:\pdf chatbot\PDF-Chatbot\backend\db"
    )

    return store