from fastapi import APIRouter, File, Form, UploadFile, Request
from fastapi.responses import RedirectResponse
from langchain_community.vectorstores import Chroma
import uuid

from services.file_process import (
    savefile,
    load_split,
    vector_store,
    get_embedding,
)
from services.template import template
from services.rag import rag_logic
file_name=None
router = APIRouter()

chat_list = []


@router.post("/upload")
def upload(file: UploadFile = File(...)):
    global file_name
    # Save uploaded PDF
    file_name=file.filename
    path = savefile(file)

    # Load and split
    chunks = load_split(path)

    # Generate unique collection id
    collection_id = str(uuid.uuid4())

    # Create vector database
    vector_store(chunks, collection_id)

    # Redirect to chat page
    return RedirectResponse(
        url=f"/chat_page/{collection_id}",
        status_code=303,
    )


@router.get("/chat_page/{collection_id}")
def chat_page(request: Request, collection_id: str):
    return template.TemplateResponse(
        request=request,
        name="chat.html",
        context={
            "collection_id": collection_id,
            "chat": chat_list,
            "name":file_name
        },
    )


@router.post("/chat_page/{collection_id}")
def user_query(
    collection_id: str,
    query: str = Form(...),
):
    print("Collection ID:", collection_id)

    chat_list.append(query)

    # Load existing collection
    store = Chroma(
        collection_name=collection_id,
        embedding_function=get_embedding(),
        persist_directory=r"E:\pdf chatbot\PDF-Chatbot\backend\db",
    )

    retriever = store.as_retriever(
        search_kwargs={
            "k": 3
        }
    )

    result = rag_logic(retriever, query)

    chat_list.append(result)

    return RedirectResponse(
        url=f"/chat_page/{collection_id}",
        status_code=303,
    )