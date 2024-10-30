# embedding.py

from sentence_transformers import SentenceTransformer

def get_embedding_model(model_name='all-MiniLM-L6-v2'):

    model = SentenceTransformer(model_name)
    return model

def generate_embeddings(text, model):

    sentences = text.split('\n')
    embeddings = model.encode(sentences, show_progress_bar=True)
    return embeddings, sentences
