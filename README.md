# Retrieval-Augmented Generation with LLaMA 3 API for PDF-Based Querying

This project demonstrates a **Retrieval-Augmented Generation (RAG)** system that uses **LLaMA 3** to respond to user queries based on content from a specified PDF. The project indexes and searches the PDF for relevant sections and uses LLaMA 3 to generate context-aware answers. If a query is not relevant to the PDF, a custom message informs the user.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Example Queries](#example-queries)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

This project uses a pre-defined PDF document (`Deep Reinforcement Learning for Portfolio Optimization.pdf`) to answer user queries in a meaningful way by:
1. Extracting text from the PDF.
2. Indexing the content with a vector store for similarity-based retrieval.
3. Using LLaMA 3, an advanced language model, to generate responses based on relevant PDF content.

## Features

- **PDF Content Extraction**: Extracts and indexes PDF content for efficient retrieval.
- **Relevance-Based Responses**: Only responds to queries relevant to the PDF, otherwise displays "Your query is not relevant."
- **Streamlit UI**: Simple and interactive interface for user queries and responses.
- **Integration with LLaMA 3**: Uses the Groq LLaMA 3 API to generate context-aware responses.

## Prerequisites

- **Python 3.8+**
- **Groq API Key** for accessing LLaMA 3
- **PDF File**: Ensure the path to `Deep Reinforcement Learning for Portfolio Optimization.pdf` is correctly specified.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hamza276/RAG-Model-llama3.git
  
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Key and foder path**:
   Set up your Groq API key for LLaMA 3 and your own pdf file path by adding it to the `app_constraints.py` file:
   ```python
   API_KEY = "your_groq_api_key_here"
   pdf_path = "your_pdf_path"
   ```

## Usage

1. **Run the Application**:
   Start the Streamlit app with:
   ```bash
   streamlit run main.py
   ```

2. **Enter Your Query**:
   - Once the app is running, enter a question related to the PDF content in the text input field.
   - The system will either retrieve a relevant answer based on the PDF content or display "Your query is not relevant."

## Project Structure

```plaintext
.
├── main.py                    # Main file to run the Streamlit app
├── app_ui.py                  # Streamlit UI components
├── load_pdf.py                # Extracts text from the PDF file
├── vector_store.py            # Handles vector database operations
├── query_llama.py             # Queries LLaMA 3 using Groq API
├── requirements.txt           # Lists required packages
├── Deep Reinforcement Learning for Portfolio Optimization.pdf # Example PDF file
└── README.md                  # Project documentation
```

## How It Works

1. **PDF Extraction** (`load_pdf.py`):
   - Loads and extracts text from the specified PDF file.

2. **Indexing and Similarity Search** (`vector_store.py`):
   - Creates a vector store using FAISS and indexes the PDF content.
   - When a query is made, performs a similarity search to find relevant sections in the PDF.

3. **Query Handling** (`query_llama.py`):
   - Sends user queries to the LLaMA 3 API with relevant context from the PDF.
   - If the model’s response suggests irrelevance, displays "Your query is not relevant."

4. **Streamlit Interface** (`app_ui.py`):
   - Provides a user-friendly interface for entering queries and viewing responses.
   - Displays a message when no relevant response is found, ensuring a clear user experience.

## Example Queries

Try some of the following queries to interact with the system:
- "What is portfolio optimization?"
- "Describe the methodology used in this study."
- "What is the Latent Feature State Space module?"

For irrelevant queries, the system will respond with: "Your query is not relevant."

## Acknowledgments

This project uses:
- **LLaMA 3** from **Groq** for language model capabilities.
- **Streamlit** for building the interactive UI.
- **FAISS** and **SentenceTransformers** for vector storage and similarity search.

## Contributing

We welcome contributions to improve this project! If you'd like to contribute:

1. **Fork the Repository**: Click on the "Fork" button at the top right of the GitHub page to create your own copy of the repository.

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/yourusername/your-forked-repo.git
   cd your-forked-repo
   ```

3. **Create a New Branch**:
   - Always create a new branch for your contributions to keep the main branch clean.
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**:
   - Implement your changes or improvements to the code.
   - Make sure to test your changes thoroughly before submitting.

5. **Commit and Push**:
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request**:
   - Go to the original repository on GitHub.
   - Click on **Pull Requests** > **New Pull Request**.
   - Choose your branch and submit a pull request with a detailed description of your changes.

7. **Review**:
   - I will review your pull request, provide feedback if necessary, and merge it if everything looks good.

**Note**: Please ensure that your code follows the existing structure and style of the project. Contributions that improve functionality, add relevant features, or fix bugs are especially welcome!

Thank you for your interest in contributing!
