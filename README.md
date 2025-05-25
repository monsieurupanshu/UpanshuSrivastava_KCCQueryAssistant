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
