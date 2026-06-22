# 🎬 Movie Chatbot

A smart movie recommendation chatbot that suggests movies based on user input using Natural Language Processing and similarity-based recommendation techniques.

---

## 🚀 Features

- 🎯 Personalized movie recommendations
- 💬 Chatbot-style interaction
- 🔍 Movie similarity search using ML techniques
- 📊 Uses movie dataset for intelligent suggestions
- ⚡ Fast response system
- 🧠 NLP-based query understanding

---

## 🛠️ Tech Stack

- Python 🐍
- Pandas
- NumPy
- Scikit-learn
- NLP (TF-IDF / Cosine Similarity)
- Streamlit / Flask (if applicable)

---
## Final Chain
User Query
↓
sanitize_input()
↓
MongoDB Memory
↓
Query Rewriter
↓
BM25 Retriever
+
Chroma Retriever
↓
EnsembleRetriever
↓
CrossEncoder Reranker
↓
Prompt Template
↓
Groq Llama 3
↓
Response
↓
Save Chats To MongoDB
↓
Logger

## 📂 Project Structure
