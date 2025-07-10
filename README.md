## RAG_QA
This project aims to preprocss the dataset for Question Answering in financial domain and show RAG question-answering workflow.

- [English Version](README.md)  
- [中文文档](README.zh.md)

---

### RAG Pipeline
The RAG (Retrieval-Augmented Generation) question-answering workflow can be divided into four core steps:
- Document Loading
- Text Splitting
- Vectorization & Retrieval
- Answer Generation with a Large Language Model.

#### Retrieval Algorithm
(1) ANN Search
- Faiss: Flat, IVF, HNSW
- Milvus: IVF+HNSW, PQ
- Weaviate: HNSW
- Qdrant: HNSW

(2) Similarity Calculation
- Cosine
- Dot Product

#### Rerank Algorithm (optional)
- BGE-Reranker
- MiniLM
- MonoT5


### How to Use
1. install env
```
pip install -r requirements.txt
```

2. api-key setting

create .env file，put api-key into .env。
```python
OPENAI_API_KEY=""
```

3. run demo in main.py
```python
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI

# init components
llm = ChatOpenAI(model="gpt-4", temperature=0)
embedding_model = OpenAIEmbeddings()
vectorstore = FAISS.load_local("faiss_index", embeddings=embedding_model)
retriever = vectorstore.as_retriever()

# conversation history memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# create Conversational RAG Chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

# multi-turn conversation
question = "What is the IPO?"
result = qa_chain.run(question)
print(result)

```

---

### 🙏 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Faiss](https://github.com/facebookresearch/faiss)   
