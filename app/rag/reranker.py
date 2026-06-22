from sentence_transformers import CrossEncoder

reranker_model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

def rerank_results(query: str, documents: list, top_k: int = 3):

    if not documents:
        return []

    pairs = [
        [query, doc.page_content]
        for doc in documents
    ]

    scores = reranker_model.predict(pairs)

    ranked_docs = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        doc
        for doc, score in ranked_docs[:top_k]
    ]