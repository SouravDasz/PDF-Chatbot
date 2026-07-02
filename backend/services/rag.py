# from chromadb import PersistentClient
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from services.llm import model
parser=StrOutputParser()
template =PromptTemplate(
    template="""
You are a helpful AI assistant.

Use only the information provided in the context below to answer the user's question.

If the context does not contain enough information to answer the question, reply only:
"I don't know."

Context:
{context}

Question:
{question}

Answer:
""",
    input_variables=["context", "question"]
)

def rag_logic(retirver,query):
    retirved_documnet=retirver.invoke(query)
    context="\n".join( documnet.page_content for documnet in retirved_documnet)
    chain=template | model | parser
    result=chain.invoke({"context":context,"question":query}) 
    return result


# def clear_db():
#     client = PersistentClient(
#         path=r"E:\pdf chatbot\PDF-Chatbot\backend\db"
#     )

#     collections = client.list_collections()

#     for collection in collections:
#         client.delete_collection(collection.name)

#     print("Database cleared successfully")