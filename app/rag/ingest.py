from pathlib import Path
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def ingest_documents():

    csv_path = Path(__file__).resolve().parents[2] / "data" / "netflix_data.csv"

    loader = CSVLoader(
        file_path=str(csv_path),
        encoding="utf-8"
    )

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    return chunks