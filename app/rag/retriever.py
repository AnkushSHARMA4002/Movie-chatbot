from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

BASE_DIR = Path(__file__).resolve().parents[2]

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=str(BASE_DIR / "chroma_db"),
    embedding_function=embeddings
)

vector_retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 5,
        "fetch_k": 20
    }
)

def retrieve(query: str):

    docs = vector_retriever.invoke(query)

    return docs


if __name__ == "__main__":

    while True:

        query = input("\nQuery: ")

        if query.lower() in ["exit", "quit"]:
            break

        docs = retrieve(query)

        for i, doc in enumerate(docs, start=1):

            print(f"\nResult {i}\n")

            print(doc.page_content)