from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

def rewrite_query(query: str):

    prompt = f"""
Rewrite the user query into a standalone search query.

Rules:
- Preserve meaning.
- Expand abbreviations if necessary.
- Do not answer the question.
- Return only the rewritten query.

User Query:
{query}
"""

    response = llm.invoke(prompt)

    return response.content.strip()