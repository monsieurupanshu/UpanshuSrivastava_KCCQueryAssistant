from sentence_transformers import SentenceTransformer
import chromadb
import ollama

# Connect to vector DB
from chromadb.config import Settings

client = chromadb.PersistentClient(path="./chroma_store")

collection = client.get_collection(name="kcc_data")
embedder = SentenceTransformer("paraphrase-MiniLM-L6-v2")


def query_kcc(user_query, k=3):
    q_vec = embedder.encode(user_query).tolist()
    results = collection.query(query_embeddings=[q_vec], n_results=k)

    if not results['documents']:
        return "⚠️ No relevant data found."

    context = "\n".join(results['documents'][0])
    prompt = f"Use this info to answer:\n{context}\n\nQ: {user_query}"

    response = ollama.chat(model="gemma:2b", messages=[
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']

# Run in terminal
if __name__ == "__main__":
    while True:
        q = input("🔍 Ask your question: ")
        if q.lower() in ['exit', 'quit']:
            break
        print("🧠", query_kcc(q))
