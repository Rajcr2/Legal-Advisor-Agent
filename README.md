# Legal-Advisor-Agent

This project is an upgraded version of the previously developed **RAG-based Legal Advisor** --> https://github.com/Rajcr2/Legal-Advisor.

now, it is just enhanced with LangChain's Agentic AI capabilities.

### Features

1. Legal Document retrieval
2. Conversational LLM capabilities

### Procedure

1.   Create new directory **'Legal Advisor'**.
2.   Inside that directory/folder create new environment.
   
   ```
   python -m venv legaladv
   ```

  Now, activate this **'legaladv'** venv.
  
4.   Clone this Repository :

   ```
   git clone https://github.com/Rajcr2/LegalAdvisor.git
   ```
5.   Now, Install all mentioned required libraries in your environment.
6.   Firstly Store legal documents in PostgreSQL for that run following command.
   ```
   python Store.py
   ``` 
   When pdfs are succefully stored you will get output like below :

7.   Lets, generate vector Embeddings now. for that, Run following command :
   
    python Embeddings.py

8.   Now, we are almost done. Just Run **'streamlit run Frontend.py'** file from Terminal. To activate the UI Interface on your browser.
   
    streamlit run Frontend.py
   
   Ask any legal question like this **"What are the grounds for divorce under the Hindu Marriage Act, 1955 ?"** and get the **'legal Advice'**.

### Output

https://github.com/user-attachments/assets/2b45d4e0-4bdc-4372-86d7-365522d36d11

                           _____________________________________________________________

### Conclusion

The Legal advisor is ready which acts as **Mini AI Advocate** you will see better version soon. Stay Tuned.
