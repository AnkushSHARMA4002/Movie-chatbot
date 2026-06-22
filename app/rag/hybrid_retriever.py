from langchain_classic.retrievers import EnsembleRetriever
from app.rag.bm25_retriever import bm25_retriever
from app.rag.retriever import vector_retriever

ensemble_retriever = EnsembleRetriever(
    retrievers=[
        bm25_retriever,
        vector_retriever
    ],
    weights=[
        0.4,
        0.6
    ]
)

def retrieve(query: str):

    docs = ensemble_retriever.invoke(query)

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