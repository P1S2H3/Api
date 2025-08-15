import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from euriai.langchain import EuriaiChatModel
import os 
from dotenv import load_dotenv
import PyPDF2

load_dotenv()

chat_model = EuriaiChatModel(
    api_key=os.getenv("EURI_API_KEY"),
    model="gpt-4.1-nano"
)

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "QA CHATBOT WITH GROQ"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user query accordingly."),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key, llm, temperature, max_tokens):
    os.environ["GROQ_API_KEY"] = api_key
    model = ChatGroq(model_name=llm, temperature=temperature, max_tokens=max_tokens)
    parser = StrOutputParser()
    chain = prompt | model | parser
    response = chain.invoke({"question": question})
    return response

st.title("Enhanced QA Chatbot with Groq")
st.sidebar.title("Settings")

api_key = st.sidebar.text_input("Enter your Groq API key here", type="password")
llm = st.sidebar.selectbox("Select Groq model", ["llama3-8b-8192", "llama3-70b-8192","gemma2-9b-it"])

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=200, max_value=500, value=150)

st.write("Go ahead and ask any question.")
user_input = st.text_input("You:")

if user_input and api_key:
    answer = generate_response(user_input, api_key, llm, temperature, max_tokens)
    st.write(answer)
elif not api_key:
    st.warning("Please enter your Groq API key.")
else:
    st.write("Please provide a query.")
