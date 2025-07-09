from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv

load_dotenv()

# 1. 加载文本资料
loader = PyPDFLoader("docs/financial_term.pdf")
documents = loader.load()

# 2. 分块
"""
chunk_size: 500 string to a chunk
chunk_overlap: overlap 100 string between chunks.
"""
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = text_splitter.split_documents(documents)
print(f"docs: {docs[:1]}")
print(f"docs length: {len(docs)}")

# 3. Embedding 和 FAISS 检索库构建
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embedding)

# 4. 构建 QA 链
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
llm = ChatOpenAI(model="gpt-4", temperature=0)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # 可选：map_reduce, refine 等
    retriever=retriever,
    return_source_documents=True
)


query = "这款耳机是否支持蓝牙？"
result = qa_chain({"query": query})

print("回答：", result["result"])
print("参考资料：", [doc.metadata for doc in result["source_documents"]])
