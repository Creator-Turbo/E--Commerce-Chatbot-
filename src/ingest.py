from langchain_astradb import AstraDBVectorStore
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEmbeddings  
from dotenv import load_dotenv
import os
import pandas as pd
from src.data_converter import dataconveter


load_dotenv()

HUGGINGFACEHUB_API_TOKEN=os.getenv("HUGGINGFACEHUB_API_TOKEN")
ASTRA_DB_API_ENDPOINT=os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN=os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE=os.getenv("ASTRA_DB_KEYSPACE")





def download_hugging_face_embeddings():
    # NEW (Updated)
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings

embeddings = download_hugging_face_embeddings()




