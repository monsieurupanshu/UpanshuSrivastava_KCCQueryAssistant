# 🌾 KCC Query Assistant

A fully local, multilingual AI assistant for answering agricultural queries using real Q&A pairs from government datasets (Krishi Call Center - KCC).

This project uses Retrieval-Augmented Generation (RAG) with **ChromaDB** and **Ollama** (`gemma:2b`) to run **completely offline** — no cloud, no API calls.

---

## 🚀 Features

- ✅ Local embeddings with `sentence-transformers` (`MiniLM`)
- ✅ Vector search using ChromaDB
- ✅ Local LLM response generation via Ollama (`gemma:2b`)
- ✅ Streamlit UI for easy Q&A interaction
- ✅ Graceful fallback when no context is found

---

## 🛠️ Technologies

- Python 3.10
- [sentence-transformers](https://www.sbert.net/)
- [ChromaDB](https://www.trychroma.com/)
- [Ollama](https://ollama.com/) + `gemma:2b`
- Streamlit

---

## 📂 Project Structure
- `app.py`  
  → Streamlit web UI to enter queries and show results

- `query_rag.py`  
  → Loads ChromaDB, retrieves top-k results, and calls Ollama for response

- `embed_store.py`  
  → Embeds `kcc_chunks.json` into ChromaDB and saves the vector store locally

- `KCC_data_process.ipynb`  
  → Jupyter notebook for cleaning and transforming raw KCC CSV data into Q&A format

- `kcc_chunks.json`  
  → Final processed Q&A dataset used for vector search

- `requirements.txt`  
  → List of Python packages needed to run the project

- `sample_queries.txt`  
  → Contains 10 test questions: 5 with answers, 5 without context

- `chroma_store/` *(not pushed to GitHub)*  
  → Auto-generated Chroma vector database directory (recreated by `embed_store.py`)
