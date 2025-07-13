import streamlit as st
from Agents import get_langchain_agent

# Streamlit Page
st.set_page_config(page_title="LangChain Agent Chatbot", layout="centered")
st.title("🧑‍⚖️ Legal Advisor Chatbot")

# Conversation mode
continue_chat = st.toggle("Enable Conversation Memory", value=True)

@st.cache_resource(show_spinner=False)
def load_agent():
    return get_langchain_agent(continue_chat=continue_chat)

agent_executor = load_agent()

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.form("chat_form", clear_on_submit=True):
    user_question = st.text_input("Ask your legal question:", key="user_input")
    submitted = st.form_submit_button("Get Legal Advice")

if submitted and user_question:
    st.session_state.chat_history.append(("user", user_question))

    with st.spinner("Agents Collaborating ..."):
        response = agent_executor(user_question)

    st.session_state.chat_history.append(("assistant", response))


col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Clear Chat"):
        st.session_state.chat_history = []

if st.session_state.chat_history:
    #st.markdown("## Chat History")
    for speaker, msg in st.session_state.chat_history:
        if speaker == "user":
            st.markdown(
                f"""
                <div style='text-align: right; margin-bottom: 12px;'>
                    <div style='display: inline-block; background-color: #dcf8c6; padding: 10px 15px; border-radius: 15px; max-width: 75%;'>
                        {msg}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else: 
            st.markdown(
                f"""
                <div style='text-align: left; margin-bottom: 12px;'>
                    <div style='display: inline-block; background-color: #f1f0f0; padding: 10px 15px; border-radius: 15px; max-width: 75%;'>
                        {msg}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown(
    """
    **💡 Tip:** Try asking questions like:  
    - "Can I be evicted without notice?"  
    - "What are my rights under BNSS?"  
    If your question isn't covered, the chatbot will inform you.
    """,
    unsafe_allow_html=True,
)
