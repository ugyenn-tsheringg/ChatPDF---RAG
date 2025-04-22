import streamlit as st

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

def display_architecture():
    st.title("Architecture")
    st.image("images/abstract_view.png", caption="System Architecture Diagram 1") 
    st.write('''This is the abstract overview of the architecture diagram. '
    'OpenAI LLM model (gpt-3.5-turbo) was used to reduce the embedding cost. '
    'OpenAI text embeddings was used to generate numerical embeddings and '
    'FAISS I used for vector store. ''')

    st.image("images/detailed_view.png", caption="System Architecture Diagram 2")
    st.write('''
    1. First the User uploads pdf, 2. Extract text from the pdf using PdfReader, 
    3. Split the texts into chunks, 4. Compute embeddings for each chunks, 
    5. Create vector store which wil be out knowledge base, 6. Users asks a question,
    7. Compute embeddings for the query, 8. Look for matching embeddings in knowledge base and
    take top three embeddings of the chunks (default)
    ''')
display_architecture()