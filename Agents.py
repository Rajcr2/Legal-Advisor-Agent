from Backend import get_agent_chain
from langchain_ollama import ChatOllama
import streamlit as st

def get_langchain_agent(continue_chat=True):

    qa_chain = get_agent_chain(continue_chat=continue_chat)
    llm = ChatOllama(model="llama3") 

    # Wrapper to handle inputs and fallback
    def agent_wrapper(input_data):
        if isinstance(input_data, str):
            user_query = input_data
            result = qa_chain.run({"question": user_query})
        elif isinstance(input_data, dict) and "query" in input_data:
            user_query = input_data["query"]
            result = qa_chain.run({"question": user_query})
        else:
            return "❌ Invalid input provided."

        # Fallback if result is poor or uncertain
        if not result or "i don't know" in result.lower() or len(result.strip()) < 50:
            return (
                "⚠️ I couldn't find enough information in the uploaded documents.\n"
                "Please consider adding more documents related to this topic.\n"
                f"The topic '{user_query}' is widely known."
            )

        return result

    return agent_wrapper
