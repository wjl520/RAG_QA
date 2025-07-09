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

3. 运行demo
```
python main.py
```

### 参考与致谢

- [LangChain](https://github.com/langchain-ai/langchain)
- [Faiss](https://github.com/facebookresearch/faiss)   
