import streamlit as st
import pickle
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS  # Updated import
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain_openai import ChatOpenAI 

with st.sidebar:
    st.title('LLM Chat App')

    st.markdown('''
    ## About 
    This app is an LLM-powered PDF chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [Langchain](https://www.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM Model   
    ''')

    # if st.button("Click here to check the Architecture"):
    #     st.switch_page("pages/architecture_page.py")

load_dotenv()  # Load environment variables 

def main():
    st.title("Upload to chat with your PDF")
    
    # Upload PDF file
    pdf = st.file_uploader("Upload your PDF here", type='pdf')

    if pdf is not None:
        pdf_name = pdf.name[:-4]  # Remove '.pdf' extension
        index_path = f"{pdf_name}_faiss_index"

        # Check if FAISS index already exists
        if os.path.exists(index_path):
            st.write("Embeddings found in Disk (Local Storage). Loading embeddings from disk...")
            embeddings = OpenAIEmbeddings()  # Needed for loading
            vectorstore = FAISS.load_local(
                index_path,
                embeddings,
                allow_dangerous_deserialization=True  # Required for security
            )
            st.success("Embeddings loaded successfully!")
        else:
            st.write("Generating embeddings (this may take a while)...")
            
            # Extract text from PDF
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            # Split text into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text)

            # Generate and save embeddings
            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
            vectorstore.save_local(index_path)  # Saves to folder
            st.success("Embeddings generated and saved!")

        #Accept user queries
        query = st.text_input("Enter your questions related to your PDF file")
        buttonclick = st.button("Generate Answer")
        #By default, k=3 (top 3 best chunks related to the query)
        if query or buttonclick:
            docs = vectorstore.similarity_search(query=query, k=3)
            llm = ChatOpenAI(model="gpt-3.5-turbo")
            chain = load_qa_chain(llm=llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question = query)
                print(cb)
            st.write(response)
    else:
        st.warning("No PDF uploaded. Please upload a file")


if __name__ == '__main__':
    main()