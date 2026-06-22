from pathlib import Path
from app.rag.ingest import ingest_documents
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

BASE_DIR = Path(__file__).resolve().parents[2]

chunks = ingest_documents()

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=str(BASE_DIR / "chroma_db")
)

print("Embeddings stored successfully")
print("Documents:", db._collection.count())