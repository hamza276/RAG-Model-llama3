# embedding.py

from sentence_transformers import SentenceTransformer

def get_embedding_model(model_name='all-MiniLM-L6-v2'):
    """
    Loads the sentence transformer model.

    Args:
        model_name (str): Name of the pre-trained model.

    Returns:
        SentenceTransformer: Loaded model.
    """
    model = SentenceTransformer(model_name)
    return model

def generate_embeddings(text, model):
    """
    Generates embeddings for the given text.

    Args:
        text (str): Input text.
        model (SentenceTransformer): Embedding model.

    Returns:
        list: List of embeddings.
    """
    sentences = text.split('\n')
    embeddings = model.encode(sentences, show_progress_bar=True)
    return embeddings, sentences
