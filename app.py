import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Lamgsmith Tracking
import os 
from dotenv import load_dotenv 
# os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']= "true"
os.environ['LANGCHAIN_PROJECT'] ="QnA Chatbot"

# Prompt Template
prompt= ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question: {question}")
    ]
)


def generate_response(question, api_key, llm, temperature, max_tokens):
    # openai.api_key = api_key
    # llm = ChatOpenAI(model =llm)
    llm = ChatGroq(
        api_key=api_key,
        model=llm,
        temperature=temperature,
        max_tokens=max_tokens
    )
    output_parser = StrOutputParser()
    chain = prompt |llm|output_parser
    answer = chain.invoke({'question': question} )
    return answer

# Title of the app
st.title("Enhanced Q&A Chatbot with Groq")

# Side bar to select models
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter you Groq API key:", type ="password")

# Drop down to select various Groq models 
llm = st.sidebar.selectbox("Select a model from Groq model list",["openai/gpt-oss-20b", "deepseek-r1-distill-llama-70b", "gemma2-9b-it"])

# adjust response parameter 
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value = 300, value=150)

# main interface for user input 
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, api_key, llm, temperature,max_tokens)
    st.write(response)
else:
    st.write("Please provide the query")
