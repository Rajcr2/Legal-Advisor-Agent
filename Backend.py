from langchain_chroma import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_ollama import ChatOllama, OllamaEmbeddings

def get_agent_chain(continue_chat=True):
    CHROMA_PATH = "./chroma_db_agent"
    COLLECTION_NAME = "llama_test_embeddings"

    embedding = OllamaEmbeddings(model="llama3")

    vectordb = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_PATH,
        embedding_function=embedding
    )

    retriever = vectordb.as_retriever()

    llm = ChatOllama(model="llama3")

    # Memory if required
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True) if continue_chat else None

    # Agent Chain Setup
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        verbose=True
    )

    return qa_chain
