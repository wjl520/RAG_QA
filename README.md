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
```
python main.py
```

### 🙏 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [Faiss](https://github.com/facebookresearch/faiss)   
