# ChatGPT-Powered PDF Assistant with Langchain & Streamlit

A conversational AI application that allows you to interact with PDF documents using OpenAI's LLM. Built as part of a tutorial project to demonstrate NLP skills, Langchain integration, and Streamlit UI development. Ideal for document analysis, Q&A, and chatbot functionalities.

![Architecture Overview](https://github.com/ugyenn-tsheringg/ChatPDF-RAG/blob/main/images/abstract_view.png)

## 🚀 Features
- Upload PDFs and extract text content.
- Split documents into manageable chunks for LLM processing.
- Generate embeddings and build a searchable index using Langchain.
- Ask questions in natural language and receive AI-powered answers.
- User-friendly interface built with Streamlit.

## 🔧 Technologies Used
- **Langchain**: Framework for LLM integration, text splitting, and embeddings.
- **OpenAI**: GPT model and API for generative responses.
- **Streamlit**: Frontend UI for PDF uploads and chat interface.
- **PyPDF2**: PDF text extraction.

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Install dependencies:
   ```bash
   pip install langchain openai streamlit pypdf2 python-dotenv
   
4. Set up your OpenAI API key in a .env file:
   ```bash
   OPENAI_API_KEY="your-api-key-here

## 🖥️ Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py

2. Upload a PDF file through the Streamlit interface.
3. Ask questions about the PDF content in the chatbox.
4. View the AI-generated responses in real-time.

## 🏗️ Architecture
Key Steps (Detailed View)
![Detailed Workflow](https://github.com/ugyenn-tsheringg/ChatPDF-RAG/blob/main/images/detailed_view.png)

### 1. PDF Processing:
   - Split PDF text into chunks.
   - Generate embeddings for each chunk.
   - Build a searchable index using Langchain.

### 2. Query Handling:
   - Convert user questions into embeddings.
   - Retrieve relevant text chunks from the index.
   - Generate answers using OpenAI's LLM.

### Tech Stack (Abstract View)
   - Backend: Langchain for data processing, OpenAI API for LLM.
   - Frontend: Streamlit for UI, chat interface, and PDF uploads.

<br>
<br>
<div align="center">
📄 License
MIT License. Feel free to adapt for your use case.

🔗 Connect with me on LinkedIn or GitHub.
</div>
