from sentence_transformers import SentenceTransformer
import json
import chromadb
from chromadb.config import Settings

# Load KCC Q&A data
with open("/Users/upanshusrivastava/Downloads/kcc_chunks.json", 'r') as f:
    data = json.load(f)

# Format as text chunks
documents = [item['text'] for item in data]
ids = [f"id_{i}" for i in range(len(documents))]

# Load embedding model
model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
embeddings = model.encode(documents, show_progress_bar=True, convert_to_numpy=True, batch_size=16)

# Store in ChromaDB

client = chromadb.PersistentClient(path="./chroma_store")

collection = client.create_collection(name="kcc_data")
batch_size = 5000
for i in range(0, len(documents), batch_size):
    collection.add(
        documents=documents[i:i+batch_size],
        embeddings=embeddings[i:i+batch_size].tolist(),
        ids=ids[i:i+batch_size]
    )


print("✅ Embeddings stored in ChromaDB.")
