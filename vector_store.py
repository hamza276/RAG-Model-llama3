import faiss
from sentence_transformers import SentenceTransformer

def initialize_vector_store():
    """Initialize the FAISS vector store and sentence transformer model."""
    index = faiss.IndexFlatL2(384)  # Set dimension based on embedding model
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight embedding model
    return index, model

def add_document_to_index(text, index, model):
    """Add document text to the vector store."""
    embeddings = model.encode([text])
    index.add(embeddings)
    return index

def search_similar(query, index, model, top_k=3):
    """Retrieve similar documents based on the query."""
    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, top_k)

    # Filter out any invalid indices (-1) and low-similarity results
    filtered_indices = [idx for idx in indices[0] if idx != -1]
    return filtered_indices  # Returns an empty list if no relevant sections are found
