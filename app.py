import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Initialize the Google Gemini model
chat = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)

# Streamlit UI setup
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat GPT")

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content="You are a helpful assistant.")
    ]

def load_answer(question):
    st.session_state.sessionMessages.append(HumanMessage(content=question))
    assistant_answer = chat.invoke(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content

def get_text():
    input_text = st.text_input("You: ")
    return input_text

user_input = get_text()
submit = st.button('Generate')  

if submit:
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response)
