from dotenv import load_dotenv
from langchain_groq import ChatGroq

from app.rag.retriever import retrieve
from app.rag.reranker import rerank_results
from app.rag.query_rewriter import rewrite_query
from app.rag.prompt import prompt_template
from app.memory.mongo_memory import save_message

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


def handle_user_query(
    query: str,
    user_id: str = "",
    conversation_id: str = ""
):

    rewritten_query = rewrite_query(query)

    docs = retrieve(rewritten_query)

    if not docs:

        answer = "I could not find that information in the dataset."

        save_message(
            user_id=user_id,
            conversation_id=conversation_id,
            role="user",
            content=query
        )

        save_message(
            user_id=user_id,
            conversation_id=conversation_id,
            role="assistant",
            content=answer
        )

        return answer

    docs = rerank_results(
        rewritten_query,
        docs,
        top_k=3
    )

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = prompt_template.invoke(
        {
            "context": context,
            "question": query
        }
    )

    response = llm.invoke(prompt)

    answer = response.content

    save_message(
        user_id=user_id,
        conversation_id=conversation_id,
        role="user",
        content=query
    )

    save_message(
        user_id=user_id,
        conversation_id=conversation_id,
        role="assistant",
        content=answer
    )

    return answer


if __name__ == "__main__":

    while True:

        query = input("\nYou: ")

        if query.lower() in ["exit", "quit"]:
            break

        answer = handle_user_query(
            query=query,
            user_id="test_user",
            conversation_id="test_conversation"
        )

        print("\nBot:", answer)