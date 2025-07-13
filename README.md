# Legal-Advisor-Agent

This project is an upgraded version of the previously developed **RAG-based Legal Advisor** --> https://github.com/Rajcr2/Legal-Advisor.

now, it is just enhanced with LangChain's Agentic AI capabilities.

### Main Features

1. **Legal Document retrieval**
2. **Conversational LLM capabilities**

### Technologies Used

- **Agentic AI Framework** : LangChain
- **Large Language Model (LLM)** : Ollama with LLaMA3
- **Vector Store & Embeddings** : ChromaDB + OllamaEmbeddings (custom embedding via LLaMA3)
- **Frontend** : Streamlit
- **Storage** : PostgreSQL
- **Language** : Python 3.10+

### Installation

   ```
   ollama serve
   ollama run llama3
   pip install langchain langchain-chroma langchain-llama
   pip install psycopg2-binary
   pip install pdfplumber
   pip install puMupdf
   pip install chromadb
   pip install time
   pip install requests
   ```

### Procedure

1.   Create new directory **'Legal Advisor'**.
2.   Inside that directory/folder create new environment.
   
   ```
   python -m venv legaladv
   ```

  Now, activate this **'legaladv'** venv.
  
4.   Clone this Repository :

   ```
   git clone https://github.com/Rajcr2/Legal-Advisor-Agent.git
   ```
5.   Now, Install all mentioned required libraries in your environment.
6.   Firstly Store legal documents in PostgreSQL for that run following command.
   ```
   python Store.py
   ``` 
   ![Store_Agent](https://github.com/user-attachments/assets/80ddc855-c3b6-4350-ad1f-9cb1dfb432d3)
   
   When pdfs are succefully stored you will get output like below :

   ![Postgre Agent](https://github.com/user-attachments/assets/7f2896ed-9933-4235-8713-816c4a1cd8be)

7.   Lets, generate vector Embeddings now. for that, Run following command :
   
    python Embeddings.py

   ![image (6)](https://github.com/user-attachments/assets/b0e12939-fdaf-48c7-afc0-c02f20d24870)

8.   Now, we are almost done. Just Run **'streamlit run Frontend.py'** file from Terminal. To activate the UI Interface on your browser.
   
    streamlit run Frontend.py
   
   ![image (10)](https://github.com/user-attachments/assets/3432fd47-054c-48fb-8f34-038025af0d41)
   
   Ask any legal question like this **"What are the grounds for divorce under the Hindu Marriage Act, 1955 ?"** and get the **'legal Advice'**.
   
### Note 

💡 - Add more **relevant legal PDFs** and **regenerate the embeddings** regularly to enhance the accuracy and depth of legal responses.
  
### Output

https://github.com/user-attachments/assets/e9abca4d-914e-4a97-9055-b6f2a39f2ce0

### Conclusion

The Legal advisor is ready and functions as a **Mini AI Advocate**. 
Thanks for Reading.
