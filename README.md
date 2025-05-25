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
  → Contains 9 test questions, 5 without context  
    - 🧪 **Note on Test Questions**  
      This file includes **3 test queries with valid KCC context** and **2 queries without matching context** to demonstrate fallback behavior.  
      👉 **Refer to the demo video** for input/output examples and expected responses for all 5.


---

## ▶️ How to Run the Project

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Ollama with local LLM

- `chroma_store/` *(not pushed to GitHub)*  
  → Auto-generated Chroma vector database directory (recreated by `embed_store.py`)

```bash
ollama run gemma:2b
```
>>> Send a message (/? for help)

- Press Ctrl + D to exit the interactive session and move on to the next step.


### 3. Run the Streamlit app

```bash
streamlit run app.py
```

- This will launch the app in your default browser.
If it doesn't open automatically, visit: http://localhost:8501

---

## 📽️ Demo Video  
🔗 [Click here to watch demo](https://drive.google.com/file/d/1hglyiJi6P-5Uyz4OPLm6l1qOybW-3vSn/view?usp=sharing)  <!-- Replace # with actual video link -->

Includes:
- ✅ Local Ollama + ChromaDB startup
- ✅ 3–5 working queries using KCC context
- ✅ 2–3 fallback examples (no context matched)
- ✅ All responses generated **100% offline**



