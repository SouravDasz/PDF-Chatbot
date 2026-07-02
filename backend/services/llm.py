from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("HUGGINGFACE_API_KEY")

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    max_new_tokens=512,
    temperature=0.2,
    huggingfacehub_api_token=api_key
)
model=ChatHuggingFace(llm=llm)