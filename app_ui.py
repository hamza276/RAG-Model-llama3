import streamlit as st
from load_pdf import extract_pdf_text
from vector_store import initialize_vector_store, add_document_to_index, search_similar
from query_llama import query_llama_api

def main_ui():
    st.title("Retrieval-Augmented Generation with LLaMA 3")

    # Load PDF from the specified path
    pdf_path = "C:/Users/hamza.k/Desktop/Deep Reinforcement Learning for Portfolio Optimization.pdf"
    text = extract_pdf_text(pdf_path)
    st.write("Your data is loaded!")  # Display message instead of PDF preview

    # Initialize vector store and populate with the document text
    index, model = initialize_vector_store()
    add_document_to_index(text, index, model)
    st.write("PDF content has been indexed for similarity search.")

    # User query
    query = st.text_input("Enter your query")
    if query:
        # Perform similarity search
        indices = search_similar(query, index, model)
        
        if not indices:
            # No relevant sections found, set response to irrelevant message
            response = "Your query is not relevant."
        else:
            # Extract relevant sections as context for LLaMA 3
            context_text = "\n\n".join([text.splitlines()[i] for i in indices if i < len(text.splitlines())])

            # Get response from LLaMA 3 with context
            response = query_llama_api(query + "\n\nContext:\n" + context_text)

            # Check if the response indicates irrelevance
            irrelevant_phrases = ["not explicitly defined", "based on the provided context", "look up additional resources"]
            if any(phrase in response for phrase in irrelevant_phrases):
                response = "Your query is not relevant."

        # Display the final response
        st.write("LLaMA 3 Response:")
        st.write(response)
