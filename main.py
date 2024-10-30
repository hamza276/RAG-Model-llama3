import streamlit as st
from app_ui import main_ui  # Updated import

def main():
    st.set_page_config(page_title="RAG App with LLaMA 3")
    main_ui()

if __name__ == "__main__":
    main()
