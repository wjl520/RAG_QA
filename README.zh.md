## RAG_QA
本项目旨在展示金融领域的数据预处理和RAG的构建流程。

- [English Version](README.md)  
- [中文文档](README.zh.md)

---

### RAG

基于 RAG（Retrieval-Augmented Generation）构建问答流程，可以将其划分为 4 个核心步骤：
- 文档加载
- 文本切分
- 向量化与检索
- 大模型生成回答。
```
用户问题 → 向量化 → FAISS 检索 Top-N → reranker 重排 → 拼接上下文 → LLM 回答
```
--- 
#### 检索算法
(1) 最近邻搜索
- 向量库     索引结构
- Faiss:    Flat, IVF, HNSW
- Milvus:   IVF+HNSW, PQ
- Weaviate: HNSW
- Qdrant:   HNSW

(2) 相似度计算
- Cosine
- Dot Product

#### 排序算法 (可选)
- BGE-Reranker
- MiniLM
- MonoT5

---

### 如何使用
1. 安装环境
```
pip install -r requirements.txt
```

2. 设置api-key

创建.env文件，将可用api-key放入。
```python
OPENAI_API_KEY=""
```

3. 样例代码
```python
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI

# 初始化组件
llm = ChatOpenAI(model="gpt-4", temperature=0)
embedding_model = OpenAIEmbeddings()
vectorstore = FAISS.load_local("faiss_index", embeddings=embedding_model)
retriever = vectorstore.as_retriever()

# 对话历史记忆
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 构建 Conversational RAG Chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

# 多轮对话调用
question = "IPO是什么？"
result = qa_chain.run(question)
print(result)

```

### 参考与致谢

- [LangChain](https://github.com/langchain-ai/langchain)
- [Faiss](https://github.com/facebookresearch/faiss)   
