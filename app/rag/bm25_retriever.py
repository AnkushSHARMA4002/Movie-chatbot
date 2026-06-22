from app.rag.ingest import ingest_documents
from langchain_community.retrievers import BM25Retriever

documents = ingest_documents()

bm25_retriever = BM25Retriever.from_documents(
    documents
)

bm25_retriever.k = 5