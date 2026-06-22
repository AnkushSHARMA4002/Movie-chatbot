from sentence_transformers import CrossEncoder
from app.rag.hybrid_retriever import retrieve

reranker_model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

def rerank_results(
    query: str,
    docs,
    top_k: int = 3
):

    if not docs:
        return []

    pairs = [
        [query, doc.page_content]
        for doc in docs
    ]

    scores = reranker_model.predict(
        pairs
    )

    ranked = sorted(
        zip(docs, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        doc
        for doc, score in ranked[:top_k]
    ]


if __name__ == "__main__":

    while True:

        query = input("\nQuery: ")

        if query.lower() in ["exit", "quit"]:
            break

        docs = retrieve(query)

        reranked_docs = rerank_results(
            query,
            docs,
            top_k=3
        )

        for i, doc in enumerate(reranked_docs, start=1):

            print(f"\nResult {i}\n")

            print(doc.page_content)